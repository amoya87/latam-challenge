import json
import os
import sys
import unittest

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
                "date": None,
                "content": None,
                "user": None,
                "mentionedUsers": None,
            },
            {
                "date": None,
                "content": None,
                "user": None,
                "mentionedUsers": None,
            },
            {
                "date": None,
                "content": None,
                "user": None,
                "mentionedUsers": None,
            },
            {
                "date": None,
                "content": None,
                "user": None,
                "mentionedUsers": None,
            },
            {
                "date": None,
                "content": None,
                "user": None,
                "mentionedUsers": None,
            },
            {
                "date": None,
                "content": None,
                "user": None,
                "mentionedUsers": None,
            },
            {
                "date": None,
                "content": None,
                "user": None,
                "mentionedUsers": None,
            },
            {
                "date": None,
                "content": None,
                "user": None,
                "mentionedUsers": None,
            },
            {
                "date": None,
                "content": None,
                "user": None,
                "mentionedUsers": None,
            },
        ]
        # Convert JSON data to escaped lines
        lines = [json.dumps(data) for data in test_data]
        with open("test_data.json", "w") as file:
            for line in lines:
                file.write(line + "\n")

        self.expected_dates = []

        self.expected_emojis = []

        self.expected_mentions = []

    def tearDown(self):
        # Delete test file after testing
        import os

        os.remove("test_data.json")
