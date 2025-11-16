# Payslip XML 2.0 schema validation with pytest
This repository has tests for validating multiple XMLs against XSD schema.

## 1. Structure:
```

├── data
  ├── invalid
  ├── valid
├── schemas
├── helper.py
├── test_xsd_validation.py

```
- In the 'invalid' folder you can find xmls with invalid data, similarly in the 'valid' folder you can find the valid data. 
- In the 'schemas' folder you can find the file with the actual schema.

## 2. Test Plan:
- Validating correct xmls against schema and encoding --> 2 tests passed
- Validating incorrect xmls against schema and encoding --> 2 tests failed in which:
  A. Structural Errors (missing required) elements, unexpected elements)
  B. Datatype violations (wrong type)
  C. Enumeration (invalid enum value)
  D. Encoding ( should match to SO-8859-15)
  

## 3. Requierements:
Packages in requirements file can be installed with:
`pip install -r requierements.txt`

## 4. Running the tests:
`pytest -v` (more details) or `pytest -q`

