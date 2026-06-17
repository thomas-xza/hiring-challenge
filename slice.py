#!/usr/bin/env python3

import json
import re

import pandas as pd

import slice_db_calls as db_calls


def main():

    csv_loaded = pd.read_csv("challenge/data/companies.csv")

    with open('challenge/mocks/enrichment_responses.json', 'r', encoding='utf-8') as file:
        mocks = json.load(file)
    
    print(csv_loaded.head(5).tail(1))

    # initialise_tables("monolith.db")

    contacts_merged = {}


def merge_maximally(
        multi_business_contacts_set: dict[str, list[dict[str, dict[str, str]]]]
        ) -> dict[str, list[dict[str, dict[str, str]]]]:

    new_multi_business_contacts_set = {}

    for business, contacts in multi_business_contacts_set.items():

        merge_res = True

        contacts_new = adjust_source_data_structure(dict(contacts))

        while merge_res == True:

            contacts_new, merge_res = merge_new_contact_data(contacts_new)

        new_multi_business_contacts_set[business] = contacts_new

    return new_multi_business_contacts_set


def adjust_source_data_structure(contacts: list[dict[str, dict[str, str]]]) -> list[dict[str, dict[str, str]]]:

    contacts_new = dict(contacts)
    
    for k, v in contacts.items():

        # print(contacts[k])

        contacts_new[k]["sources"] = [contacts[k]["source_url"]]

        contacts_new[k].pop("source_url", None)

    return contacts_new


def merge_new_contact_data(contacts: list[dict[str, dict[str, str]]]) -> list[dict[str, dict[str, str]]]:

    ##  Takes set of new contact data for 1 business, merges data
    ##  providers where possible, scores.

    for i, provider_1 in enumerate(contacts):

      for j, provider_2 in enumerate(contacts):

        c = contacts[provider_1]

        c2 = contacts[provider_2]

        if i != j:

 #          print(c, c2)

          merge_plan = [names_compare(c, c2),
                        phones_compare(c, c2),
                        name_email_compare(c, c2)]

          if sum(merge_plan) > 0:

            confidence = sum(merge_plan) * 5

            new_contact = merge_contacts(c, c2, confidence)

            new_contact_set = {}

            for _, provider_3 in enumerate(contacts):

                if provider_3 != provider_1 and provider_3 != provider_2:

                    new_contact_set[provider_3] = contacts[provider_3]

            new_contact_set[f"{provider_1}-{provider_2}"] = new_contact

            return new_contact_set, True

    return contacts, False


def merge_contacts(c1: dict[str, str], c2: dict[str, str], conf: int) -> dict[str, str]:

    c_new = dict(c1)
    
    for k, v in c2.items():

        if k not in c_new.keys():

            c_new[k] = v

    if "confidence" not in c_new.keys():

        c_new["confidence"] = 70 + conf

    else:

        c_new["confidence"] += conf

    for source in c2["sources"]:

        if source not in c_new["sources"]:

            c_new["sources"] = c_new["sources"] + [source]

    c_new.pop("provider_confidence", None)

    c_new.pop("source_url", None)

    return c_new


def extract_data(c: dict[str, str], attr) -> str:

    if attr in c.keys():

        return c[attr]

    return None
        

def names_compare(c1: dict[str, str], c2: dict[str, str]) -> int:

    n1, n2 = extract_data(c1, "name"), extract_data(c2, "name")

    if n1 is None or n2 is None:

      return 0

    else:

        n1, n2 = n1.lower().replace('.', ''), n2.lower().replace('.', '')

    if n1 == n2:
        
      return 1

    name_cc = extract_name_core_components(n1)

    matches = 0

    for comp in name_cc:

        n2_initials = [word[0] for word in n2.split(' ')]

        if len(comp) == 1 and comp in n2_initials:

            matches += 1

            n2_initials = []  ##  Only accept 1 initial max.

        elif len(comp) > 1 and comp in n2:

            matches += 1

    if matches == 2:

        return 1
            
    return -1


def name_email_compare(c1: dict[str, str], c2: dict[str, str]) -> int:

    n1, e1 = extract_data(c1, "name"), extract_data(c2, "email")
    
    if n1 is None or e1 is None:

      return 0

    else:

        n1, e1 = n1.lower(), e1.lower().split('@')[0]

    n1cc = extract_name_core_components(n1)

    matches = 0

    n1cc_initials = [word[0] for word in n1cc]

    for comp in n1cc:

        if len(comp) > 1 and comp in e1:

            matches += 1

        elif len(comp) == 1 and comp in n1cc_initials:

            matches += 1

            n1cc_initials = []
                        
    if matches >= 1:

        return 1
            
    return -1


def extract_name_core_components(n: str) -> tuple[str]:

    titles = r"^(?:mrs|ms|mr|dr|prof|mx)\.?\s+"

    n_no_title = re.sub(titles, "", n)

    n_final = n_no_title.replace('.', '').split(' ')

    n_final_no_whitespace = tuple(map(
        lambda x: x.replace(' ', ''),
        n_final
    ))

    return (n_final_no_whitespace[0], n_final_no_whitespace[-1])


def phones_compare(c1: dict[str, str], c2: dict[str, str]) -> int:

    p1, p2 = extract_data(c1, "phone"), extract_data(c2, "phone")

    if p1 is None or p2 is None:

      return 0

    else:

        p1, p2 = p1.lower().replace('.', ''), p2.lower().replace('.', '')

    if p1 == p2:
        
      return 1

  
def compliance_check_new_contacts(
        new_contacts: list[dict[str, dict[str, str]]]) -> list[dict[str, dict[str, str]]]:

    ##  Check new contact data for compliance before storing to
    ##  database. Filters out non-compliant contacts.

    pass

    
def calculate_initial_confidence_value(contact_record: dict[str, dict[str, str]]) -> int:

    pass


def select_target_contact(
        db_records: list[dict[str, dict[str, str]]]) -> dict[str, dict[str, str]]:

    ##  Takes a set of potential contacts, extracts best candidate.

    ##  This is a more a function for contacts after they have been
    ##  organised from the various sources and written to the
    ##  database, and then read from, which is beyond the scope of
    ##  this challenge. Also it is not particularly complex, just
    ##  order by role.

    pass


if __name__ == "__main__":

    main()
