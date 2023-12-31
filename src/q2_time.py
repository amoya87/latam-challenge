import json
from collections import Counter
from typing import List, Tuple

from memory_profiler import profile

from util import extract_emojis


@profile
def q2_time(file_path: str) -> List[Tuple[str, int]]:
    """
    Extract top-10 emojis from a JSON file containing tweets.

    Args:
        file_path (str): The path to the JSON file containing tweet data.

    Returns: List[Tuple[str, int]]: A list of at most 10 tuples with the most
    frequent emojis where each tuple contains an emoji and its frequency of
    appearance, ordered in descending order of frequency.
    """
    # Create a dictionary to count objects by timestamps
    emoji_count = Counter()

    with open(file_path, encoding="utf-8") as f:
        for line in f:
            try:
                doc = json.loads(line)
                text = doc["content"]
                emojis_found = extract_emojis(text)
                # Count the frequency of each emoji
                emoji_count.update(emojis_found)
            except (json.JSONDecodeError, KeyError) as e:
                # Handle JSON decoding errors or missing keys
                print(f"Error processing line: {line.strip()}. Error: {e}")

        # Find the top 10 emojis
        top_10_emojis = emoji_count.most_common(10)

        return top_10_emojis
