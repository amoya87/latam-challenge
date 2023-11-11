import json
from collections import Counter
from typing import List, Tuple


def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    # We use a Counter to count mentions of each username
    mention_counter = Counter()
    with open(file_path, encoding="utf-8") as f:
        for line in f:
            try:
                doc = json.loads(line)
                mentioned_users = doc.get("mentionedUsers", [])
                if mentioned_users:
                    mentions = [
                        mention["username"] for mention in mentioned_users
                    ]
                    # Count the frequency of each mention
                    mention_counter.update(mentions)
            except (json.JSONDecodeError, KeyError) as e:
                # Handle JSON decoding errors or missing keys
                print(f"Error processing line: {line.strip()}. Error: {e}")

    # Find the top 10 mentions
    top_10_mentions = mention_counter.most_common(10)

    return top_10_mentions
