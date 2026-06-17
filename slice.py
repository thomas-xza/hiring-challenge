#!/usr/bin/env python3

import json
import re

import pandas as pd

import implementation_db_calls as db_calls


def main():

    csv_loaded = pd.read_csv("challenge/data/companies.csv")

    with open('challenge/mocks/enrichment_responses.json', 'r', encoding='utf-8') as file:
        mocks = json.load(file)
    
    print(csv_loaded.head(5).tail(1))

    # initialise_tables("monolith.db")

    contacts_merged = {}

    for business in resp_res:

        merge_res = true

        while merge_res = True:

            contacts, merge_res = merge_new_contact_data(contacts)

        contacts_merged[business] = contacts


def merge_new_contact_data(contacts: list[dict[str, dict[str, str]]]) -> list[dict[str, dict[str, str]]]:

    ##  Takes set of new contact data for 1 business, merges data
    ##  sources where possible, scores.

    for i, c in enumerate(contacts):

      for j, c2 in enumerate(contacts):

        if i != j:

          merge_plan = [names_compare(c, c2),
                        phones_compare(c, c2),
                        name_email_compare(c, c2)]

          if sum(merge_plan) > 0:

            confidence = sum(merge_plan) * 5

            new_contact = merge_two_contacts(c, c2, confidence)

            new_contact_set = []

            for k, c in enumerate(contacts):

                if k != i and k != j:

                    new_contact_set = new_contact_set + [contact]

            new_contact_set = [new_contact] + new_contact_set

            return new_contact_set, True

    return contacts, False


def merge_contacts(c1: dict[str, str], c2: dict[str, str], conf: int) -> dict[str, str]:

    c_new = dict(c1)
    
    for k, v in c2.items():

        if k not in c_new.keys():

            c_new[k] = v

    if "confidence" not in c_new.keys():

        c_new["confidence"] = conf

    else:

        c_new["confidence"] += conf

    return c1


def extract_data(c: dict[str, str], attr) -> str:

    if attr in c.keys():

        return c[attr]

    return null
        

def names_compare(c1: dict[str, str], c2: dict[str, str]) -> int:

    n1, n2 = extract_data(c1, "name").lower(), extract_data(c2, "name").lower()

    if n1 == null or n2 == null

      return 0

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

    n1 = extract_data(c1, "name").lower()

    e1 = extract_data(c2, "email").lower().split('@')[0]
    
    if n1 == null or e1 == null

      return 0

    if n1 == n2:
        
      return 1

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


def extract_name_core_components(n: str) -> str:

    titles = r"^(?:mrs|ms|mr|dr|prof|mx)\.?\s+"

    n_no_title = re.sub(titles, "", n)

    n_final = n_no_title.replace('.', '').split(' ')

    n_final_no_whitespace = tuple(map(
        lambda x: x.replace(' ', ''),
        n_final
    ))

    return (n_final_no_whitespace[0], n_final_no_whitespace[-1])

    
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
