import json
from collections import Counter, defaultdict
from datetime import datetime
from typing import List, Tuple


def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    # Create a dictionary to count objects by date and name
    date_name_count = defaultdict(Counter)
    with open(file_path, encoding="utf-8") as f:
        for line in f:
            try:
                doc = json.loads(line)
                date = datetime.fromisoformat(doc["date"]).date()
                timestamp = int(
                    datetime.combine(date, datetime.min.time()).timestamp()
                )
                name = doc["user"]["username"]
                date_name_count[timestamp][name] += 1
            except (json.JSONDecodeError, KeyError) as e:
                # Handle JSON decoding errors or missing keys
                print(f"Error processing line: {line.strip()}. Error: {e}")

    # Find the 10 dates with the most objects
    top_10_dates = sorted(
        date_name_count,
        key=lambda dat: sum(date_name_count[dat].values()),
        reverse=True,
    )[:10]

    # For each date in the top 10, find the most common name
    result = []
    for date in top_10_dates:
        common_name = date_name_count[date].most_common(1)[0][0]
        date_time = datetime.utcfromtimestamp(date)
        result.append((date_time.date(), common_name))

    return result