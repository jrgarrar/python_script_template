# Python Script Template

### Overview

Python scripts are handy tools for common, repetitive tasks, such as:

* Creating templated files
* Performing routine maintenance
* Generating reports


### Setup

1. Install [Python](https://www.python.org/downloads/).

2. Copy this directory.

3. Modify `script.py` to do what you need.

4. Run `python script.py <your_arguments>` to execute the script from the command line.


### Main Technical Stack

| Tool   | Description                               |
| ------ | ----------------------------------------- |
| Python | A scripting programming language.         |
| Pip    | The package manager for Python libraries. |


### Helpful Tools

| Tool       | Description                                                    |
| ---------- | -------------------------------------------------------------- |
| Pandas     | Read and write to most filetypes, including Excel.             |
| Jinja      | Quick and easy templating tool.                                |
| Matplotlib | Generate image files from data.                                |
| Black      | An automatic Python formatter to ensure consistent code style. |
| Venv       | Pin your Python version                                        |


```
# Example Installation
$ pip install pandas
```

```
# Example Usage in File
import pandas

pandas.read_csv('some_filename')
```

### Advanced Usage

***black***

Use `black *.py` to auto-format all Python files in the directory.

***venv***

Use `sh env_setup.sh` to create a version of Python local to this directory. Python packages will be installed here, rather than across your entire system.

***requirements.txt***

Use `pip freeze > requirements.txt` to create a file that lists all dependencies, as well as their versions.

Use `pip -r requirements.txt` to install those dependencies.

