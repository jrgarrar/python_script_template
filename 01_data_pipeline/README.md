# Data Pipeline Template

### Overview

```
.
┣ input/            # Place input data here
┣ output/           # Output data is automatically generated here
┗ process_data.py  
```

A simple example of how to create a data pipeline in Python using Pandas.

The `process_data.py` script ingests a CSV file, adds a column, and outputs the result

### Setup

`$pip install -r requirements.txt`

### Author's Notes

The `pandas` library is a staple in the Data Science community for cleaning and manipulating data sources.

The `numpy` library runs underneath, and can be used directly for performance-sensitive tasks.

I've used these tools in more complex pipelines, including a lengthy setup that ingested decades worth of govt. survey data, reconciled the schemas, and output the result in an analytics-friendly format. Their syntax takes some getting used to, particularly for developers who are used to R.