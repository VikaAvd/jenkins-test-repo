# Financial Data Processing & Billing System Automated Tests

This project contains automated tests using PyTest and pymssql to verify data in a Microsoft SQL Server database for a Financial Data Processing & Billing System. The tests validate critical data by executing SQL queries against tables in the TRN database.

## Table of Contents
- [Overview](#overview)
- [Test Cases Description](#test-cases-description)
- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Tests](#running-the-tests)
- [CI/CD Integration](#CI/CD-Integration)
- [Troubleshooting](#troubleshooting)

## Overview
This project uses PyTest along with pymssql to connect to a SQL Server instance, execute queries, and validate data. It ensures that key data from the system is accurate and meets business requirements.

## Test Cases Description
The project implements six test cases (two per table):

**Employees Table:**
- **TC_EMPLOYEE_COUNT:** Verifies that the total number of employees in the `[hr].[employees]` table is greater than zero.
- **TC_EMPLOYEE_AVG_SALARY:** Verifies that the average salary in the `[hr].[employees]` table is within an expected range (e.g., between 1000 and 20000).

**Jobs Table:**
- **TC_JOBS_MIN_LESS_THAN_MAX:** Confirms that for each job in `[hr].[jobs]`, the `min_salary` is less than the `max_salary`.
- **TC_JOBS_UNIQUE_TITLES:** Ensures that every job title in `[hr].[jobs]` is unique (i.e., no duplicate titles).

**Locations Table:**
- **TC_LOCATIONS_NOT_NULL_CITY:** Validates that the `city` column in the `[hr].[locations]` table does not contain NULL values.
- **TC_LOCATIONS_COUNTRY_ID_LENGTH:** Checks that the `country_id` in the `[hr].[locations]` table is exactly 2 characters long.

## Prerequisites
- **Python 3.8+** (Tested with Python 3.12)
- **PyTest**
- **pymssql**
- **pytest-html** (for generating an HTML report, optional)
- A running **Microsoft SQL Server** instance with the `TRN` database and `hr` schema.
- A SQL Server login with the necessary permissions.
- Docker installed on your system for running Jenkins.

## Project Structure
```bash
pytest_db_tests/
├── tests/
│   ├── conftest.py          # PyTest fixture for DB connection
│   ├── test_employees.py    # Tests for the employees table
│   ├── test_jobs.py         # Tests for the jobs table
│   └── test_locations.py    # Tests for the locations table
├── db_connection.py         # Helper function for database connection (using pymssql)
├── requirements.txt         # List of required Python packages
├── README.md                # Project documentation (this file)
├── Jenkinsfile              # Jenkins pipeline script for CI/CD
└── output/                  # Folder where test reports are generated
```

## Installation
1. **Clone the Repository**  
- `git clone https://github.com/VikaAvd/jenkins-test-repo.git`
- `cd jenkins-test-repo`

2. **Install Python Dependencies:** 
Ensure you have Python installed, then run:
- `pip install --break-system-packages -r requirements.txt`

## Configuration
1. **Database Connection**
Open db_connection.py and update the connection string with your SQL Server settings. For example:
- SERVER: If running locally from a Docker container, use host.docker.internal\\SQLEXPRESS01
- DATABASE: TRN
- UID: {your login} (e.g., robot)
- PWD: {your password} (e.g. Vika_password123)

2. **Git Repository Branch Structure:**  
The repository follows a Git Flow approach with three main branches:
- **main**: Production-ready code.
- **develop**: Integration branch for merging features.
- **feature-branch**: Used for feature development.
New features are merged into develop via pull requests, and once tested, develop is merged into main for deployment.

## Running the Tests
- To run all tests from the project root use one of the options below:
   - `pytest`
   - `pytest -rbA`
   - `pytest -vv`
 
- To generate an HTML report, run:
   - `pytest --html=output/report.html --self-contained-html`
   - After running the tests with `pytest --html=output/report.html --self-contained-html`, open output/report.html in your web browser to view the detailed test report.

## CI/CD Integration
The project is integrated with Jenkins using a Jenkinsfile stored in the repository. The pipeline consists of:
- Checkout: Retrieves code from GitHub.
- Install Dependencies: Installs Python packages.
- Run Tests: Executes the tests using PyTest.
- Deploy (CD): Merges the develop branch into main and pushes the updated main branch to GitHub.

## Troubleshooting

Connection Issues:
If you receive errors verify that:
- pymssql is installed and your database connection parameters are correct.
- SQL Server Connectivity: Ensure TCP/IP is enabled and the correct server information is configured in db_connection.py.
- SQL Server Browser is running.
- Permissions: Confirm that the user has the required permissions on the TRN database.

Test Failures:
- Review the console output and generated reports for error details.
- Check your SQL queries and database connection settings for any discrepancies.
- Check and update the connection parameters in db_connection.py.

CI/CD Issues:
- Verify that Jenkins can access GitHub (e.g., correct credentials and webhook configuration).








