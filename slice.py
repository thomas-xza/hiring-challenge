#!/usr/bin/env python3

import json

import pandas as pd

import sqlite3

import implementation_db_calls as db_calls


def main():

    csv_loaded = pd.read_csv("challenge/data/companies.csv")

    with open('challenge/mocks/enrichment_responses.json', 'r', encoding='utf-8') as file:
        mocks = json.load(file)
    
    print(csv_loaded.head(5).tail(1))

    new_contacts = organise_new_contacts_data(mocks)

    # initialise_tables("monolith.db")


def organise_new_contacts_data(contacts: list[dict[str, dict[str, str]]]) -> list[dict[str, dict[str, str]]]:

    ##  Takes set of new contact data, merges data sources where
    ##  possible, scores.

    
    
    
def compliance_check_new_contacts(
        new_contacts: list[dict[str, dict[str, str]]]) -> list[dict[str, dict[str, str]]]:

    ##  Check new contact data for compliance before storing to
    ##  database. Filters out non-compliant contacts.

    
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
