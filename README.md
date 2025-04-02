# Assignment-01

## Author
name: Yani Tao  
Computing ID：yanitao

---

## Assignment Description

This assignment consists of three main tasks completed on an EC2 instance. The purpose is to gain familiarity with the Linux environment, system configuration, shell scripting, and Python scripting for data processing.

---

## Task Overview

### Task 1: Check Operating System Version, Hardware Configuration, and Jupyter Notebook Installation

- Used basic Linux shell commands to output system information to text files:
  - OS release → `_output/os.txt`
  - CPU info → `_output/cpu.txt`
  - Memory info → `_output/mem.txt`
- Verified installation versions of `pip3` and `jupyter`:
  - pip3 version → `_output/pip3.txt`
  - jupyter version → `_output/jupyter.txt`

---

### Task 2: Counting Python in StackOverflow Posts (Shell)

- Downloaded a ZIP dataset from Google Drive.
- Wrote a shell script named `count_python.sh` which:
  - Counts the number of lines containing the word `"python"` in the extracted CSV files.
  - Is located in the `_output/` folder.
- Execution command:
  ```bash
  chmod +x _output/count_python.sh
  ./_output/count_python.sh

### Task 3: Counting GitHub in StackOverflow Posts (Python)

- Wrote a Python script count_github.py which:
  - Counts the number of lines containing the word "GitHub" in all extracted CSV files using pandas.
  - Is located in the _output/ folder.
- The script can be run with:
  python3 _output/count_github.py
