#!/usr/bin/env python3

import pandas as pd

def main():

    csv_loaded = pd.read_csv("challenge/data/companies.csv")

    print(csv_loaded.head(5).tail(1))


def check():

    return 1
    
if __name__ == "__main__":

    main()
