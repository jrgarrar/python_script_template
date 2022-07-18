# Python Script Template

### Overview

Python scripts are handy tools for common, repetitive tasks. This directory contains simple examples that can be tailored to specific project needs.

```
00_basic_cli_script        A simple command line script.   
01_data_pipeline           Ingest, modify, and output data.
02_file_templater          Create repetitive, similar files by passing in parameters.
03_api_accessor            Issue GET, POST, and other HTTP commands to the internet.
04_simple_api              Create a barebones API.
05_graph_generator         Create a graph, for use as a dashboard or visual.
06_excel_cleaner           Manipulate Excel data from the command line.
07_sql_wrapper             (TBD) Wrap SQL commands in a script.
08_install_tool            (TBD) Install software dependencies using a script.
09_test_suite              (TBD) Execute a series of tests.
```


### Main Technical Stack

| Tool   | Description                               |
| ------ | ----------------------------------------- |
| python | A scripting programming language.         |
| pip    | The package manager for Python libraries. |


### Helpful Tools

| Tool       | Description                                                                                                    |
| ---------- | -------------------------------------------------------------------------------------------------------------- |
| black      | An automatic code formatter. Ensures consistent style.                                                         |
| unittest   | One of several testing frameworks. Can be used to create a regression test suite.                              |
| virtualenv | A virtual environment manager. Can be used to reproduce an exact Python environment (language + dependencies). |
| poetry     | An extension of virtualenv and pip that simplifies version management.                                         |