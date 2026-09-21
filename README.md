# GitHub Profile Fetcher

A small tool that fetches public GitHub profiles and saves a summary report.

## What it does

- Takes a list of GitHub usernames
- Fetches each profile from the GitHub public API
- Prints a summary and writes it to report.txt
- Handles missing users without crashing

## Requirements

    pip install requests

## Usage

Edit the names list in fetcher.py, then run:

    python fetcher.py

## Example output

    Hossein Khalafian - 4 repos
    Linus Torvalds - 12 repos
    Guido van Rossum - 28 repos

## Tests

    pip install pytest
    pytest
