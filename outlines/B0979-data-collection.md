# B0979 — Data Collection
**Program:** Data Analytics (DA)  
**Hours:** 100 hrs (5 weeks)  
**Delivery:** Online Instructor-Guided

---

## Description

Students explore the first stage of the data analytics pipeline: acquiring, extracting, and preparing data from a variety of sources. Topics include manual data entry and validation, web scraping, working with APIs, database querying (SQL), and introduction to data collection with Python. Students develop practical skills for obtaining real-world datasets and assessing their quality.

---

## Learning Outcomes

**Outcome 1: Identify and evaluate data sources and collection methods**
- Distinguish between primary and secondary data sources
- Describe common data collection methods: surveys, observational data, APIs, web scraping, databases
- Evaluate data sources for relevance, reliability, recency, and potential bias
- Identify privacy, copyright, and ethical considerations in data collection
- Document a data collection plan for a given analytical goal

**Outcome 2: Collect and validate data from structured and semi-structured sources**
- Design and create data entry forms with appropriate validation rules
- Import and inspect structured data (CSV, Excel, JSON) using spreadsheet tools
- Identify and address common data quality issues: missing values, duplicates, inconsistent formatting
- Apply basic data-cleaning transformations in a spreadsheet environment
- Summarise a dataset's key characteristics using descriptive statistics

**Outcome 3: Query relational databases to extract data**
- Describe the relational model and the role of SQL
- Write `SELECT` statements with `WHERE`, `ORDER BY`, and `LIMIT`
- Use aggregate functions: `COUNT`, `SUM`, `AVG`, `MIN`, `MAX` with `GROUP BY`
- Join two or more tables using `INNER JOIN` and `LEFT JOIN`
- Export query results for downstream analysis

**Outcome 4: Retrieve data from web sources using APIs and web scraping**
- Explain how web APIs work (HTTP, endpoints, JSON responses)
- Make authenticated and unauthenticated API requests using a REST client or Python `requests`
- Parse JSON API responses to extract target fields
- Apply basic web scraping concepts using Python (`BeautifulSoup` or equivalent)
- Respect `robots.txt`, rate limits, and terms of service when scraping

**Outcome 5: Automate data collection using Python**
- Write Python scripts to read and write CSV and JSON files
- Use `pandas` to load, inspect, and filter tabular data
- Automate repetitive data extraction tasks with loops and functions
- Combine data from multiple sources into a single dataset
- Document and share a data collection script with clear comments

---

## Assessment

| Assessment | Description | Weight |
|---|---|---|
| Assignment 1: Data Sources & Collection Plan | Evaluate two data sources; document a collection plan for an analytical question | 15% |
| Assignment 2: Data Entry & Quality | Design a data entry form; collect a small dataset; clean and validate it | 20% |
| Assignment 3: SQL Data Extraction | Write SQL queries against a provided database to answer analytical questions | 25% |
| Assignment 4: API Data Collection | Retrieve data from a public API; parse and save the response | 20% |
| Assignment 5: Python Automation | Write a Python script that collects, combines, and exports a dataset | 20% |

**Minimum passing grade:** 70%

### Assessment → Outcome Mapping

| Assessment | LO1 Sources | LO2 Structured | LO3 SQL | LO4 APIs | LO5 Python |
|---|:---:|:---:|:---:|:---:|:---:|
| Assignment 1 | ✓ | | | | |
| Assignment 2 | | ✓ | | | |
| Assignment 3 | | | ✓ | | |
| Assignment 4 | | | | ✓ | |
| Assignment 5 | | | | | ✓ |

---

## Course Schedule

| Week | Module | Assignment Due |
|---|---|---|
| Week 1 | Module 1 — Data Sources and Collection Methods (20 hrs) | Assignment 1 — End of Week 1 |
| Week 2 | Module 2 — Structured Data and Quality (20 hrs) | Assignment 2 — End of Week 2 |
| Week 3 | Module 3 — SQL Data Extraction (20 hrs) | Assignment 3 — End of Week 3 |
| Week 4 | Module 4 — APIs and Web Scraping (20 hrs) | Assignment 4 — End of Week 4 |
| Week 5 | Module 5 — Python Data Collection Automation (20 hrs) | Assignment 5 — End of Week 5 |

---

### Module 1 — Data Sources and Collection Methods (Week 1)

**Topics:**
- The data analytics pipeline: where collection fits
- Primary vs secondary data; structured vs unstructured
- Survey design, observational data, sensor data, transaction data
- Evaluating sources: CRAAP test and equivalents
- Privacy legislation overview: PIPEDA / provincial privacy acts
- Data ethics: consent, anonymisation, minimisation

---

### Module 2 — Structured Data and Quality (Week 2)

**Topics:**
- Spreadsheet data entry: validation rules, drop-downs, constraints
- Importing CSV and JSON into Excel / Google Sheets
- Common quality issues: NULLs, duplicates, encoding errors, type mismatches
- Descriptive statistics for data profiling: mean, median, mode, range, distribution
- Data cleaning operations: `TRIM`, `PROPER`, `IF`, `VLOOKUP`

---

### Module 3 — SQL Data Extraction (Week 3)

**Topics:**
- Relational model: tables, rows, columns, primary and foreign keys
- `SELECT`, `FROM`, `WHERE`, `ORDER BY`, `LIMIT`
- Aggregate functions and `GROUP BY` / `HAVING`
- `INNER JOIN`, `LEFT JOIN`, multi-table queries
- Subqueries and CTEs (intro)
- Exporting results to CSV

**Tools:** DB Browser for SQLite; provided sample databases

---

### Module 4 — APIs and Web Scraping (Week 4)

**Topics:**
- HTTP: methods, status codes, headers
- REST API concepts: endpoints, query parameters, authentication (API key, Bearer token)
- Making requests with Postman or `curl`
- Parsing JSON responses: accessing nested fields
- Web scraping concepts: HTML structure, CSS selectors, `BeautifulSoup`
- Ethical and legal constraints: `robots.txt`, rate limiting, ToS

---

### Module 5 — Python Data Collection Automation (Week 5)

**Topics:**
- Python environment setup: Anaconda / `venv`, `pip`
- Reading and writing CSV and JSON with built-in `csv` / `json` modules
- Introduction to `pandas`: `read_csv`, `DataFrame`, `head`, `describe`, `loc`/`iloc`
- Loops and functions for repetitive extraction
- Combining datasets: `pd.concat`, `pd.merge`
- Script documentation: comments, docstrings, README

---

## Required Materials

- **Software:** Python 3.x (Anaconda distribution recommended); DB Browser for SQLite; Postman; Excel or Google Sheets
- **Equipment:** Laptop/Computer

---

## Academic Policies

- **Grading:** Minimum 70% to pass
- **Attendance:** Active participation is tracked
- **Copyright:** Unauthorized copies of course materials are a violation of the Copyright Act and may constitute academic misconduct
- See the [Robertson College Student Guide](https://www.robertsoncollege.com/help/student-resources/student-guide/) for full policies
