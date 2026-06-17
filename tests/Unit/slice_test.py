#!/usr/bin/env python3

import unittest
import json

import slice as sl

class Test_implementation(unittest.TestCase):

    def setUp(self):
        
        with open('challenge/mocks/enrichment_responses.json', 'r', encoding='utf-8') as file:
            self.mocks = json.load(file)

        # print(self.mocks)
    
    def test_name_match_1(self):
        self.assertEqual(
            sl.names_compare(
                self.mocks["Cedar Ridge Plumbing LLC"]["registry"],
                self.mocks["Cedar Ridge Plumbing LLC"]["listing"]
            ), 1)
        
    def test_name_match_2(self):
        self.assertEqual(
            sl.names_compare(
                self.mocks["Harbor Light Electric"]["listing"],
                self.mocks["Harbor Light Electric"]["registry"]
            ), 1)
        
    def test_name_match_3(self):
        self.assertEqual(
            sl.names_compare(
                self.mocks["Ironclad Welding Shop"]["registry"],
                self.mocks["Ironclad Welding Shop"]["listing"]
            ), -1)
        
    def test_name_match_4(self):
        self.assertEqual(
            sl.names_compare(
                self.mocks["Lakeside Auto Glass"]["listing"],
                self.mocks["Lakeside Auto Glass"]["enrichment"]
            ), 0)

    def test_name_email_match_1(self):
        self.assertEqual(
            sl.name_email_compare(
                self.mocks["Lakeside Auto Glass"]["listing"],
                self.mocks["Lakeside Auto Glass"]["enrichment"]
            ), 1)
        
    def test_name_email_match_2(self):
        self.assertEqual(
            sl.name_email_compare(
                self.mocks["Ironclad Welding Shop"]["listing"],
                self.mocks["Ironclad Welding Shop"]["enrichment"]
            ), 1)
        
    def test_name_email_match_3(self):
        self.assertEqual(
            sl.name_email_compare(
                self.mocks["Ironclad Welding Shop"]["registry"],
                self.mocks["Ironclad Welding Shop"]["enrichment"]
            ), -1)
        
    def test_name_email_match_4(self):
        self.assertEqual(
            sl.name_email_compare(
                self.mocks["Ironclad Welding Shop"]["registry"],
                self.mocks["Ironclad Welding Shop"]["listing"]
            ), 0)
        
    def test_phones_match_1(self):
        self.assertEqual(
            sl.phones_compare(
                self.mocks["Sunbelt Roofing Co"]["listing"],
                self.mocks["Sunbelt Roofing Co"]["enrichment"]
            ), 1)
        
    def test_phones_match_2(self):
        self.assertEqual(
            sl.phones_compare(
                self.mocks["Bayview Auto Repair"]["registry"],
                self.mocks["Bayview Auto Repair"]["enrichment"]
            ), 0)
        
if __name__ == '__main__':
    unittest.main()
