import datetime
import json
import os
import sys
import unittest

from parameterized import parameterized

# Get the full path to the 'src' directory
src_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "src")
)

# Add 'src' to Python path
sys.path.append(src_path)

from src import q1_memory, q1_time, q2_memory, q2_time, q3_memory, q3_time


class TestSuit(unittest.TestCase):
    def setUp(self):
        # Prepare the data
        # Create a test JSON file with dummy data
        test_data = [
            {
                "date": "2021-02-24T09:22:11+00:00",
                "content": "🙏",
                "user": {"username": "Alberto"},
                "mentionedUsers": [
                    {"username": "LATAM321"},
                    {"username": "LATAM_CHI"},
                ],
            },
            {
                "date": "2021-02-24T09:22:11+00:00",
                "content": "😂🙏text👀text",
                "user": {"username": "Moya"},
                "mentionedUsers": None,
            },
            {
                "date": "2021-02-24T09:22:11+00:00",
                "content": "🙏",
                "user": {"username": "Loustaunau"},
                "mentionedUsers": None,
            },
            {
                "date": "2021-02-24T09:22:11+00:00",
                "content": "🙏",
                "user": {"username": "Alberto"},
                "mentionedUsers": [
                    {"username": "LATAM_CHI"},
                    {"username": "LATAM321"},
                    {"username": "LATAMAirlines"},
                ],
            },
            {
                "date": "2021-02-25T09:22:08+00:00",
                "content": "👀 text😂",
                "user": {"username": "Moya"},
                "mentionedUsers": None,
            },
            {
                "date": "2021-02-25T09:22:09+00:00",
                "content": "🙏",
                "user": {"username": "Moya"},
                "mentionedUsers": None,
            },
            {
                "date": "2021-02-25T09:22:10+00:00",
                "content": "😂",
                "user": {"username": "Moya"},
                "mentionedUsers": [{"username": "LATAM_CHI"}],
            },
            {
                "date": "2021-02-25T09:22:11+00:00",
                "content": "dfasgh ghfjkshjg gfsdhg",
                "user": {"username": "Alberto"},
                "mentionedUsers": None,
            },
            {
                "date": "2021-02-25T09:22:11+00:00",
                "content": "💚",
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

        self.expected_emojis = [("🙏", 5), ("😂", 3), ("👀", 2), ("💚", 1)]

        self.expected_mentions = [
            ("LATAM_CHI", 3),
            ("LATAM321", 2),
            ("LATAMAirlines", 1),
        ]

    def tearDown(self):
        # Delete test file after testing
        import os

        os.remove("test_data.json")

    @parameterized.expand(
        [
            ("memory", q1_memory.q1_memory),
            ("time", q1_time.q1_time),
        ]
    )
    def test_q1(self, param, function):
        # Call the function with the test JSON file
        result = function("test_data.json")

        # Checks if the result is a list of tuples with the correct format
        for _date, name in result:
            self.assertIsInstance(_date, datetime.date)
            self.assertIsInstance(name, str)

        # Check that the dates in the result are in the correct order
        dates = [date.strftime("%Y-%m-%d") for date, _ in result]

        self.assertEqual(dates, self.expected_dates, f"{param}: test failure")

    @parameterized.expand(
        [
            ("memory", q2_memory.q2_memory),
            ("time", q2_time.q2_time),
        ]
    )
    def test_q2(self, param, function):
        # Call the function with the test JSON file
        results = function("test_data.json")

        # Verification of expected results
        self.assertEqual(
            results, self.expected_emojis, f"{param}: test failure"
        )

    @parameterized.expand(
        [
            ("memory", q3_memory.q3_memory),
            ("time", q3_time.q3_time),
        ]
    )
    def test_q3(self, param, function):
        # Call the function with the test JSON file
        results = function("test_data.json")

        # Verification of expected results
        self.assertEqual(
            results, self.expected_mentions, f"{param}: test failure"
        )
