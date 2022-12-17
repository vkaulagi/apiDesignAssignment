import unittest
from unittest.mock import patch
import inventory_client

class InventorySystemTests(unittest.TestCase):

    @patch('inventory_client.Client')
    def testGetBookTitles(self, client):
        client.getTitles.return_value = ['first_book']
        isbnList = [100]
        response = client.getTitles(isbnList)
        assert len(response) != 0
        print(response)
        self.assertEqual(response[0], "first_book")

    # Live server test
    def testGetBookTitlesLiveServer(self):
        client = inventory_client.Client()
        isbnList = [100]
        response = client.getTitles(isbnList)
        assert len(response) != 0
        print(response)
        self.assertEqual(response[0], "first_book")