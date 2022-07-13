# Excel Cleaner Template

### Overview

```
.
┣ input/            # Place input data here
┣ output/           # Output data is automatically generated here
┗ excel_cleaner.py  
```

A simple example of how to extract the tabs of an Excel file into their own spreadsheets.

### Setup

`$pip install -r requirements.txt`

### Author's Notes

Some particularly large libraries like `pandas` may have optional dependencies. For example, the `openpyxl` library allows `pandas` to interact with Excel files, but does not come installed by default.