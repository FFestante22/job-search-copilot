# 🚀 Job Search Copilot: Automated Job Board Scraper & Filter

## 📖 Overview
Finding the right job in the IT sector often involves sifting through hundreds of postings that don't match specific legal or contractual requirements. **Job Search Copilot** is a Python-based automation tool built to streamline the job-hunting process in the Spanish Tech market. 

It automatically scrapes job descriptions from URLs, analyzes the text, and filters out non-viable roles (like Freelance, B2B, or autonomous work), allowing the user to focus strictly on standard employment contracts (cuenta ajena) that align with specific work permit requirements.

## 🎯 The Problem it Solves
Manual job filtering is a time-consuming bottleneck. Many tech job boards lack strict filters for contract types, leading to wasted time reading descriptions for roles that ultimately require self-employment (autónomo) status.

## 💡 The Solution
This script acts as a personal assistant that:
1. **Extracts:** Takes a job posting URL and automatically scrapes the title, company, and full description.
2. **Analyzes:** Runs a keyword-based logic filter to detect "red flags" (e.g., *freelance*, *facturar*, *B2B*).
3. **Organizes:** Approves viable job offers and exports them into a structured Pandas DataFrame (CSV/Excel) for easy follow-up tracking.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Data Manipulation:** `pandas`
* **Web Scraping:** `requests`, `BeautifulSoup4`
* **Date Management:** `datetime`

## 🚀 Features (Current & Upcoming)
- [x] Keyword filtering logic to discard freelance/B2B roles.
- [x] DataFrame structuring for application tracking.
- [ ] Automated web scraping from URLs (In Progress).
- [ ] Follow-up alert system based on application dates.
- [ ] Automated export to `.csv`.

## 👨‍💻 About the Author
Developed by **Facundo Festante**, Digital Project Manager & IT Operations Specialist, to bridge the gap between technical automation and efficient project management.
