import json
from collections import Counter
from typing import List, Tuple


# @profile
def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    """
    Extracts the 10 most mentioned usernames in tweets from a JSON file.

    Args:
        file_path (str): The path to the JSON file containing tweet data.

    Returns: List[Tuple[str, int]]: A list of at most 10 tuples with the most
    mentioned usernames where each tuple contains a username and its mention
    frequency, sorted descending by number of mentions.
    """
    # We use a Counter to count mentions of each username
    mention_counter = Counter()
    with open(file_path, encoding="utf-8") as f:
        for line in f:
            try:
                doc = json.loads(line)
                mentioned_users = doc.get("mentionedUsers", [])
                if mentioned_users:
                    mentions = [
                        mention["username"].encode("ascii")
                        for mention in mentioned_users
                    ]
                    # Count the frequency of each mention
                    mention_counter.update(mentions)
            except (json.JSONDecodeError, KeyError) as e:
                # Handle JSON decoding errors or missing keys
                print(f"Error processing line: {line.strip()}. Error: {e}")

    # Find the top 10 mentions
    top_10_byte = mention_counter.most_common(10)
    top_10_mentions = [(e[0].decode("ascii"), e[1]) for e in top_10_byte]

    return top_10_mentions
