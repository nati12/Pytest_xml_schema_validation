import pytest
from pathlib import Path
from lxml import etree
#import re
from helper import (
    EXPECTED_ENCODING, get_encoding, fail_encoding
)
#EXPECTED_ENCODING = "ISO-8859-15"


#Using fixtures for schema objects to avoid reloading them for each test
#Scoping fixtures at module level for better performance
#Print error logs when validation fails for easier debugging
#Using parametrize for testing multiple XML files efficiently
#Testing both valid and invalid cases to ensure validation works correctly
@pytest.fixture(scope="module")
def xsd_schema():
    """Loading and parsing the XSD schema for all tests"""
    schema_doc = etree.parse('schemas/PayslipXML_v2.0_schema_NEW_07_2023.xsd')
    return etree.XMLSchema(schema_doc)
    
# Multiple XMLs
xml_valid_files = list(Path("data/valid").glob("*.xml"))
xml_invalid_files = list(Path("data/invalid").glob("*.xml"))

@pytest.mark.parametrize("xml_file", xml_valid_files, ids=lambda x: x.name)
def test_xml_files_valid_and_encoding(xml_file, xsd_schema):
    """Validating encoding"""
    declared = get_encoding(xml_file)
    if declared != EXPECTED_ENCODING:
        fail_encoding(xml_file.name, declared, EXPECTED_ENCODING)

    """Validating XMLs against schema"""
    xml_doc = etree.parse(str(xml_file))
    is_valid = xsd_schema.validate(xml_doc)

    # Adding readable error logs
    if not is_valid:
        pytest.fail(f"Validation failed: {xsd_schema.error_log}")

@pytest.mark.parametrize("xml_file", xml_invalid_files, ids=lambda x: x.name)
def test_xml_files_invalid_and_encoding(xml_file, xsd_schema):
    """Validating encoding"""
    declared = get_encoding(xml_file)
    if declared != EXPECTED_ENCODING:
        fail_encoding(xml_file.name, declared, EXPECTED_ENCODING)

    """Validating against schema"""
    xml_doc = etree.parse(str(xml_file))
    
    with pytest.raises(etree.DocumentInvalid) as exc:
        xsd_schema.assertValid(xml_doc)
    print(f"\nValidation errors for {xml_file.name}: \n{exc.value.error_log}")
    raise


