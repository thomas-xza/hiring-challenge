#!/usr/bin/env python3

def write_to_database(db_name:str):

    ##  Takes values from various sources, writes them to the
    ##  business_entities and contacts tables within the database.
    ##  Will calculate initial confidence value before writing.

    pass


def initialise_tables(db_name: str):

    ##  Setup the tables for which new added will be added (SQLite3
    ##  for prototype purposes, but could be scaled to a more
    ##  heavyweight DB engine).
    
    conn = sqlite3.connect(db_name)

    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS business_entities (
    business_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    government_company_number TEXT UNIQUE,
    date_added TEXT DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS contacts (
    contact_id INTEGER PRIMARY KEY AUTOINCREMENT,
    business_id TEXT NOT NULL,
    name TEXT,
    role TEXT,
    phone TEXT,
    email TEXT,
    address TEXT,
    provider_confidence INTEGER,
    source TEXT NOT NULL,
    FOREIGN KEY (business_id) REFERENCES business_entities (business_id)
    )
    ''')

    conn.commit()

    print("Database and 2 tables created successfully!")

    conn.close()

    
def generate_sample_table_output(db_name: str):

    ##  Not sure exactly what the data structure of the output comes
    ##  back as, after an SQL statement is made, so it would be good
    ##  to find out.
    ##  However, it could always be refit into a preferred data
    ##  structure, so this is a bit redundant.

    ##  Ultimately it could definitely be mapped to a standard
    ##  key-value, where the key is the unique ID column of a table,
    ##  and the values are the other columns of the same table.

    pass


if __name__ == "__main__":

    main()
