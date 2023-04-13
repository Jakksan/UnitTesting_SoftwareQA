# STQA-Testing-Program

[![Coverage Status](https://coveralls.io/repos/github/Jakksan/UnitTesting_SoftwareQA/badge.svg?branch=main(Coverage Status)!:https://coveralls.io/github/Jakksan/UnitTesting_SoftwareQA?branch=main)]

note that for some reason, 3 lines are being marked as not covered by the test cases, even though I know they are

## Project Description
* This project is a web application that will calculate BMI based on values provided by a user. 
* The goal of this project was to learn about setting up test environments
* To ensure the test cases cover all lines of code, coverage and coveralls are used. You can see the status of current coverage at the top of this readme.

## Setup and Installation Guide
1. Install [python](https://www.python.org/downloads/) & [pip](https://pip.pypa.io/en/stable/installation/)
2. Clone this repository
3. From within a command line, run `pip install -r requirements.txt` at the root of the repository

## Execution Instructions
1. From your command line, navigate to `src/flaskr/Webapp/` then type `flask run`
2. From your web browser of choice, navigate to http://127.0.0.1:5000

## Local Testing Instructions
1. From your command line, navigate to `src/`
2. run `coverage run -m pytest tests`
3. run `coverage report` or for in-browser viewing `coverage html` then click on the index.html file inside of the newly generated `src/htmlcov/` folder
