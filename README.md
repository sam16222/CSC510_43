[![Build](https://github.com/sam16222/CSC510_43/actions/workflows/python-app.yml/badge.svg)](https://github.com/sam16222/CSC510_43/actions/workflows/python-app.yml)
[![DOI](https://zenodo.org/badge/529913763.svg)](https://zenodo.org/badge/latestdoi/529913763)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)
![GitHub](https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white)
# Fall '22 CSC 510 (Group 43)
This repository is created to showcase the different concepts learned through our coursework as part of CSC 510 offered in Fall '22 at NC State University.

## Introduction
A Python application to read CSV files and generate summaries of columns (medians and standard deviation for numerics; mode and entropy for symbolic columns).

## Homeworks
|Homework| Status| Task|
|:------:|:------|:------|
|HW2     |&check;|Get this going for the `Num` and `Sym` class (below) and the tests cases `the`, `sym`, `num`, `bignum`.|
|HW3     |&check;|Get this going for the `Cols`, `Row`, `Data` class and the test cases `eg.csv, eg.data, eg.stats`.|
|HW4     |&cross;|Add all the bling from HW1. Also, add post-commit hooks to auto run all the test cases, the code coverage checks (if your language supports then), and the documentation generators.  For more on what kinds of documentation is acceptable, see [the web site from lecture1](https://user-images.githubusercontent.com/29195/130997647-d933884e-8e5c-4f0c-a367-6a5d69bb1df1.png).|
|HW5     |&cross;|For five other groups from cs510 (picked at random), apply the Project1 [rubric](https://github.com/txt/se22/blob/main/docs/proj1.md#rubric).  Important note: whatever scores you offer, these will **not** change the other group's scores.|

## Installation
This repository does not use any dependencies and you only need python 3.6 or above installed to run the application.

## Post commit hooks
Every developer needs to install post commit hooks at their end. To do so, take the latest pull from main and run the following
3 commands:
    1. git config core.hooksPath .githooks
    2. cd .githooks
    3. chmod +x post-commit

## Instructions
Make sure you are in the base folder.<br><br>
Run the tests by typing the following in the terminal:
```bash
cd tests
python engine.py
```

## Meet the Team
![Team](assets/team_edit.png)
