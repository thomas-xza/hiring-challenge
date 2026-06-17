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

    def test_merge_contacts_1(self):

        contacts = sl.adjust_source_data_structure(self.mocks["Sunbelt Roofing Co"])

        self.assertEqual(
            sl.merge_contacts(
                contacts["listing"],
                contacts["enrichment"],
                5
            ),
            {'name': None, 'phone': '+1-480-555-0133', 'email': 'office@sunbeltroofingaz.com', 'confidence': 75, 'sources': ['mock://listing/sunbelt-roofing', 'mock://enrichment/sunbelt-roofing']}
        )

    def test_merge_contacts_2(self):

        contacts = sl.adjust_source_data_structure(self.mocks["Cedar Ridge Plumbing LLC"])

        self.assertEqual(
            sl.merge_contacts(
                contacts["registry"],
                contacts["listing"],
                5
            ),
            {'name': 'Daniel Ortega', 'role': 'Owner', 'phone': '+1-402-555-0148', 'confidence': 75, 'sources': ['mock://registry/ne/cedar-ridge-plumbing', 'mock://listing/cedar-ridge-plumbing']}
        )
        
    def test_merge_contacts_3(self):

        contacts = sl.adjust_source_data_structure(self.mocks["Pioneer Landscaping Inc"])

        # print(sl.merge_contacts(
        #         contacts["listing"],
        #         contacts["enrichment"],
        #         5
        #     ))
        
        self.assertEqual(
            sl.merge_contacts(
                contacts["listing"],
                contacts["enrichment"],
                5
            ),
            {'name': 'Maria Gomez', 'phone': '+1-208-555-0175', 'sources': ['mock://listing/pioneer-landscaping', 'mock://enrichment/pioneer-landscaping'], 'email': 'maria@pioneerlandscaping.com', 'confidence': 75}
        )

    def test_merge_new_contact_data_1(self):

        contacts = sl.adjust_source_data_structure(self.mocks["Cedar Ridge Plumbing LLC"])

        # print(sl.merge_new_contact_data(
        #         self.mocks["Cedar Ridge Plumbing LLC"]
        #     ))

        self.assertEqual(
            len(sl.merge_new_contact_data(
                contacts
            )), 2
        )
        

    def test_merge_new_contact_data_2(self):

        contacts = sl.adjust_source_data_structure(self.mocks["Pioneer Landscaping Inc"])
        
        self.assertEqual(
            len(sl.merge_new_contact_data(
                self.mocks["Pioneer Landscaping Inc"]
            )), 2
        )

        
    def test_merge_maximally_1(self):

        merge_max_res = sl.merge_maximally(
                self.mocks
            )
        
        self.assertEqual(
            len(merge_max_res["Pioneer Landscaping Inc"]), 1
        )
        
    def test_merge_maximally_2(self):

        merge_max_res = sl.merge_maximally(
                self.mocks
            )

        print(merge_max_res)

        self.assertEqual(
            len(merge_max_res["Brookside Veterinary Clinic"]), 1
        )
        
        self.assertEqual(
            len(merge_max_res["Ironclad Welding Shop"]), 2
        )
        
       
    def test_merge_maximally_3(self):

        merge_max_res = sl.merge_maximally(
                self.mocks
            )

        self.assertEqual(
            len(merge_max_res["Coastal Breeze Pool Service"]), 2
        )
        
        
if __name__ == '__main__':
    unittest.main()
