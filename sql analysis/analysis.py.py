import pandas as pd
import sqlite3

def run_queries(connection, queries):
    """Execute a list of SQL queries and display results."""
    for desc, query in queries:
        print(f"--- {desc} ---")
        result = pd.read_sql_query(query, connection)
        print(result)
        print("\n" + "-"*80 + "\n")
        result.to_csv(f"output_{desc.replace(' ', '_')}.csv", index=False)

if __name__ == "__main__":

  
    df = pd.read_csv("marketing_campaigns.csv")


    conn = sqlite3.connect(":memory:")

    
    df.to_sql("marketing_campaigns", conn, index=False, if_exists="replace")
    print("CSV loaded successfully!\n")

    #SQL queries
    queries = [
        ("Sample Records", "SELECT * FROM marketing_campaigns LIMIT 10;"),
        ("Data Completeness",
         "SELECT COUNT(*) as total_records, "
         "COUNT(DISTINCT MarketID) as unique_markets, "
         "COUNT(DISTINCT LocationID) as unique_locations, "
         "COUNT(DISTINCT Promotion) as promotion_types, "
         "MIN(week) as start_week, MAX(week) as end_week "
         "FROM marketing_campaigns;"),
        ("Missing Values",
         "SELECT SUM(CASE WHEN MarketID IS NULL THEN 1 ELSE 0 END) as missing_market, "
         "SUM(CASE WHEN Promotion IS NULL THEN 1 ELSE 0 END) as missing_promotion, "
         "SUM(CASE WHEN SalesInThousands IS NULL THEN 1 ELSE 0 END) as missing_sales "
         "FROM marketing_campaigns;"),
        ("Promotion Performance",
         "SELECT Promotion, COUNT(*) as num_observations, "
         "ROUND(AVG(SalesInThousands), 2) as avg_sales, "
         "ROUND(MIN(SalesInThousands), 2) as min_sales, "
         "ROUND(MAX(SalesInThousands), 2) as max_sales, "
         "ROUND(SUM(SalesInThousands), 2) as total_sales "
         "FROM marketing_campaigns "
         "GROUP BY Promotion "
         "ORDER BY avg_sales DESC;")
    ]

    run_queries(conn, queries)
    
    conn.close()
