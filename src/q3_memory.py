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
