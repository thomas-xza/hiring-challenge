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

    # initialise_tables("monolith.db")


def select_target_contact(
        db_records: list[dict[str, dict[str, str]]]) -> dict[str, dict[str, str]]:

    ##  Takes a set of potential contacts, extracts best candidate.

    pass


def compliance_check_new_contacts(
        new_contacts: list[dict[str, dict[str, str]]]) -> list[dict[str, dict[str, str]]]:

    ##  Check new contact data for compliance before storing to
    ##  database. Filter out non-compliant contacts.

    
def calculate_initial_confidence_value(contact_record: dict[str, dict[str, str]]) -> int:

    pass


if __name__ == "__main__":

    main()
