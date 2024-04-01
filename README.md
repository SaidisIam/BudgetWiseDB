# Book store

## How to run
pip install -r  .\requirements.txt

## Description

This project is a Python application for managing personal financial statistics. It allows users to track their income, expenses, and savings over time. The application provides functionalities such as viewing all statistics, searching for statistics by user's full name, adding new income entries, and adding new users.

## Features

View all financial statistics
Search financial statistics by user's full name
Add new income entries
Add new users
## Installation

Clone the repository to your local machine.
Install the required dependencies using pip install -r requirements.txt.
Set up your PostgreSQL database and update the configuration file (conf.py) with your database credentials.
Run the main.py file to start the application.
## Usage

Run the main.py file.
Choose the desired command (1 for Statistics, 2 for Users, 3 to exit).
Depending on the command chosen, select the appropriate sub-command to view statistics, search for users, add income, add users, etc.
Follow the prompts to interact with the application.
## Database Schema

The application uses the following tables in the PostgreSQL database:

users: Stores information about users such as full name, username, email, password, and balance.
income: Stores income entries with details such as user ID, amount, source, and event date.
expenses: Stores expense entries with details such as user ID, amount, category, and event date.