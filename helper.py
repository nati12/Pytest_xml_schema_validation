import pytest
from pathlib import Path
from lxml import etree
import re

EXPECTED_ENCODING = "ISO-8859-15"

def get_encoding(xml_file):
    with open(xml_file, "rb") as f:
        first_line = f.readline()
    match = re.search(rb'encoding=[\'"](.*?)[\'"]', first_line)
    print(first_line)
    return match.group(1).decode("ascii") if match else None

def fail_encoding(xml_file, declared, expected):
    pytest.fail(
        f"[ENCODING ERROR]\n"
        f"  File: {xml_file}\n"
        f"  Declared: {declared}\n"
        f"  Expected: {expected}\n"
    )