from resources import swearwords
import re
from difflib import SequenceMatcher


def censor_text(text, banned_words):
    for word in banned_words:
        pattern = re.compile(r'\b' + re.escape(word) + r'\b', re.IGNORECASE)
        text = pattern.sub('▂' * len(word), text)
        
    return text


def is_safe(text, banned_words):
    for word in banned_words:
        pattern = re.compile(r'\b' + re.escape(word) + r'\b', re.IGNORECASE)
        if re.search(pattern, text):
            return False
    return True


def check(word, blacklist):
    return SequenceMatcher(None, word, blacklist).ratio()
