import re

def check_format(str):
    pattern = r'^\d{2}:\d{2}:\d{2}$'
    return re.match(pattern, str) is not None