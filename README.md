# Marketing Campaign Analysis

## Overview
This project provides a detailed analysis of a retail marketing campaign dataset using **SQL (via SQLite in Python)** and **Excel pivot tables & charts**. The analysis focuses on promotion performance, market size impact, weekly sales trends, and store age effects to provide actionable business insights.

---

## Dataset
- **File:** `data/marketing_campaigns.csv`  
- **Rows:** 548  
- **Columns:** 
  - `MarketID` — Unique identifier for each market  
  - `LocationID` — Store location ID  
  - `Promotion` — Promotion identifier  
  - `SalesInThousands` — Sales in thousands of dollars  
  - `MarketSize` — Small, Medium, Large  
  - `AgeOfStore` — Store age in years  
  - `Week` — Week number of the observation  

---

## Analysis Highlights

### 1. Promotion Performance
- **Promotion A** achieved the highest average sales.  
- **Promotion C** performed moderately, while **Promotion B** had the lowest performance.  

![Promotion Performance](images/promotion_performance.png)

---

### 2. Weekly Sales Trends
- All promotions show consistent sales trends over time.  
- **Promotion A** maintains momentum, showing strong sustainability.  

![Weekly Trends](images/weekly_trends.png)

---

### 3. Market Size Impact
- **Large markets** recorded the highest average sales.  
- **Small markets** show more variability in sales performance.  

![Market Size Performance](images/market_size_performance.png)

---

## How to Run SQL Analysis
1. Open terminal and navigate to the repository folder.  
2. Run the Python analysis script:
```bash
python sql_analysis/analysis.py

