# Introduction

This anaylsis expands on [this reddit post](https://old.reddit.com/r/nba/comments/1kv1i7j/data_analysis_who_are_the_most_conventional_and/) by /u/refreshing_yogurt where they breakdown which votes/voters are the most conventional (and vice versa) compared to the rest of the group for the 2024-2025 All NBA votes. 

All NBA voting is conducted by a global panel of sportswriters and broadcasters each season. Typically, each category has a first, second, and third slot. Each slot carrys 5 points for first, 3 for second, and 1 for third place respectively. 

Inspired by [Baraa Khatib Salkini](https://github.com/DataWithBaraa) I've decided to start a Data Engineering project. 
This project is set out as a means of maintaining and enhancing my Data Engineering Skills. These include:
- maintaining a git repository
- Python Development (Pandas)
- Designing a Modern Data Warehouse with Medallion Architecture
- SQL Development for maintaining and providing data for analysis reporting/dashboards
- ETL (Extract, Transform, Load) workflows for populating and transforming data into the data warehouse
- Data visualization

## Data Sources

Dataset fpr the ballot counts have been provided via the NBA Communications article found [here](https://pr.nba.com/voting-results-2024-25-nba-regular-season-awards/). These PDF files have been manually converted to CSV files via [tabula](https://tabula.technology/), as each varied with page size, columns, and titles. 

## Methodology

### Tools Used

- git for version control
- Python for data manipulation, storage, computing
- Postgresql for SQL
- PowerPI (free) for data visualization

### Data Archictecture

For this project I want to utilize a Medallion Architecture for the data:
- Source Data: NBA Award Ballots
- Bronze Layer: Raw, unprocessed Data from source
    - Objective: Trace and debug
    - Object Type: Pandas Dataframe, SQL Table
    - Transformation: None, data remains as-is
- Silver Layer: Clean and standardized Data
    - Objective: Prepare Data for Analysis
    - Object Type: Panda's Dataframe, SQL Table
    - Transformation: Clean, standardize, normalize
- Gold Layer: Consumable, report ready data
    - Objective: Provide data to be consumed for reporting and analytics
    - Object Type: SQL View
    - Transformation: Aggregation, Logic and Rules
- Target Data: Local DB to house the data
