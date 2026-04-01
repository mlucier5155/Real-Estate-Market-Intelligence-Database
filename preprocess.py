import csv
import random
from datetime import datetime, timedelta

# Helpers
def random_date():
    start = datetime(2020, 1, 1)
    end = datetime(2025, 1, 1)
    return start + (end - start) * random.random()

# LOCATION
with open("data/location.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["LocationID","City","State","Region","GeoIndex"])
    for i in range(100):
        writer.writerow([f"L{i}", "City"+str(i), "FL", "Region"+str(i%5), f"GI{i}"])

# ZIP_CODE
with open("data/zipcode.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["ZipCode","City","State"])
    for i in range(100):
        writer.writerow([f"33{i:03}", "City"+str(i), "FL"])

# PROPERTY
with open("data/property.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["PropertyID","Address","ZipCode","Bedrooms","Bathrooms","SquareFootage","YearBuilt","LocationID"])
    for i in range(100):
        writer.writerow([
            f"P{i}",
            f"{i} Main St",
            f"33{i:03}",
            random.randint(1,5),
            random.randint(1,4),
            random.randint(800,3000),
            random.randint(1990,2022),
            f"L{i}"
        ])

# PRICE_HISTORY
with open("data/price_history.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["PropertyID","HistoryID","SaleDate","SalePrice"])
    for i in range(100):
        writer.writerow([
            f"P{i}",
            "H1",
            random_date().date(),
            random.randint(200000,600000)
        ])

# MARKET_DATA
with open("data/market.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["MarketID","InterestRate","InflationRate","HousingDemandIndex","MarketDate"])
    for i in range(100):
        writer.writerow([
            f"M{i}",
            round(random.uniform(3.0,7.0),2),
            round(random.uniform(1.0,4.0),2),
            random.randint(60,100),
            random_date().date()
        ])

# FORECAST
with open("data/forecast.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["ForecastID","PropertyID","MarketID","PredictedPrice","ForecastDate","ConfidenceScore"])
    for i in range(100):
        writer.writerow([
            f"F{i}",
            f"P{i}",
            f"M{i}",
            random.randint(250000,700000),
            random_date().date(),
            round(random.uniform(0.7,0.95),2)
        ])