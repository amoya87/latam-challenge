import datetime
import json
import os
import sys
import unittest

from src import q1_memory

# Get the full path to the 'src' directory
src_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "src")
)

# Add 'src' to Python path
sys.path.append(src_path)


class TestSuit(unittest.TestCase):
    def setUp(self):
        # Prepare the data
        # Create a test JSON file with dummy data
        test_data = [
            {
                "date": "2021-02-24T09:22:11+00:00",
                "content": None,
                "user": {"username": "Alberto"},
                "mentionedUsers": None,
            },
            {
                "date": "2021-02-24T09:22:11+00:00",
                "content": None,
                "user": {"username": "Moya"},
                "mentionedUsers": None,
            },
            {
                "date": "2021-02-24T09:22:11+00:00",
                "content": None,
                "user": {"username": "Loustaunau"},
                "mentionedUsers": None,
            },
            {
                "date": "2021-02-24T09:22:11+00:00",
                "content": None,
                "user": {"username": "Alberto"},
                "mentionedUsers": None,
            },
            {
                "date": "2021-02-25T09:22:08+00:00",
                "content": None,
                "user": {"username": "Moya"},
                "mentionedUsers": None,
            },
            {
                "date": "2021-02-25T09:22:09+00:00",
                "content": None,
                "user": {"username": "Moya"},
                "mentionedUsers": None,
            },
            {
                "date": "2021-02-25T09:22:10+00:00",
                "content": None,
                "user": {"username": "Moya"},
                "mentionedUsers": None,
            },
            {
                "date": "2021-02-25T09:22:11+00:00",
                "content": None,
                "user": {"username": "Alberto"},
                "mentionedUsers": None,
            },
            {
                "date": "2021-02-25T09:22:11+00:00",
                "content": None,
                "user": {"username": "Alberto"},
                "mentionedUsers": None,
            },
        ]
        # Convert JSON data to escaped lines
        lines = [json.dumps(data) for data in test_data]
        with open("test_data.json", "w") as file:
            for line in lines:
                file.write(line + "\n")

        self.expected_dates = ["2021-02-25", "2021-02-24"]

        self.expected_emojis = []

        self.expected_mentions = []

    def tearDown(self):
        # Delete test file after testing
        import os

        os.remove("test_data.json")

    def test_q1(self):
        # Call the function with the test JSON file
        result = q1_memory.q1_memory("test_data.json")

        # Checks if the result is a list of tuples with the correct format
        for _date, name in result:
            self.assertIsInstance(_date, datetime.date)
            self.assertIsInstance(name, str)

        # Check that the dates in the result are in the correct order
        dates = [date.strftime("%Y-%m-%d") for date, _ in result]

        self.assertEqual(dates, self.expected_dates)