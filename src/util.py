import re
from typing import List


def extract_emojis(text: str) -> List[str]:
    """
    Extract emojis from the given text using a regex pattern.
    We consider emojis
    # https://unicode.org/emoji/charts/full-emoji-list.html
    # https://symbl.cc/en/unicode/table/#enclosed-alphanumeric-supplement

    Args:
        text (str): The text from which emojis will be extracted.

    Returns:
        List[str]: A list of emojis found in the text.
    """

    emoji_pattern = re.compile(r"[\U0001F300-\U0001FAFF]", flags=re.UNICODE)
    return emoji_pattern.findall(text)
