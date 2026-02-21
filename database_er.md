ER diagram:              
                   LOCATION
               ┌───────────┐
               │LocationID │
               │City       │
               │State      │
               │GeoIndex   │
               └─────┬─────┘
                     │ 1
                     │
                     │ M
                  PROPERTY
               ┌────────────┐
               │PropertyID  │
               │Address     │
               │City        │
               │State       │
               │ZipCode     │
               │SqFt        │
               └─────┬──────┘
                     │1
                     │
                     │M
               PRICE_HISTORY
               ┌─────────────┐
               │HistoryID    │
               │SaleDate     │
               │SalePrice    │
               └─────────────┘


PROPERTY M ───────< FORECAST >────── M MARKET_DATA
             ┌────────────┐
             │ForecastID  │
             │Predicted$  │
             │Confidence  │
             └────────────┘

              
| Attribute       | Type         |
| --------------- | ------------ |
| PropertyID (PK) | Identifier   |
| Address         | Mandatory    |
| City            | Mandatory    |
| State           | Mandatory    |
| ZipCode         | Mandatory    |
| Bedrooms        | Single-value |
| Bathrooms       | Single-value |
| SquareFootage   | Single-value |
| YearBuilt       | Optional     |


| Attribute       | Type                                |
| --------------- | ----------------------------------- |
| LocationID (PK) | Identifier                          |
| City            | Mandatory                           |
| State           | Mandatory                           |
| Region          | Optional                            |
| GeoIndex        | Mandatory (Location-based indexing) |

| Attribute          | Type         |
| ------------------ | ------------ |
| MarketID (PK)      | Identifier   |
| InterestRate       | Mandatory    |
| InflationRate      | Mandatory    |
| HousingDemandIndex | Single-value |
| MarketDate         | Mandatory    |

| Attribute              | Type       |
| ---------------------- | ---------- |
| HistoryID (Partial PK) | Identifier |
| PropertyID (FK)        | Mandatory  |
| SaleDate               | Mandatory  |
| SalePrice              | Mandatory  |

| Attribute       | Type       |
| --------------- | ---------- |
| ForecastID (PK) | Identifier |
| PropertyID (FK) | Mandatory  |
| MarketID (FK)   | Mandatory  |
| PredictedPrice  | Mandatory  |
| ForecastDate    | Mandatory  |
| ConfidenceScore | Optional   |


relationships: 
LOCATION (1) ───────────────< PROPERTY (M)     description: One location can contain many properties.
Each property belongs to exactly one location. 1 to many type

PROPERTY (1) ───────────────< PRICE_HISTORY (M) description: Each property can have many price history records.
PRICE_HISTORY is a weak entity. 1 to many type

PROPERTY (M) ───< FORECAST >─── (M) MARKET_DATA description: Many properties are analyzed using many market datasets.
FORECAST stores predicted pricing results and analytics output. many to many type 

PROPERTY (1) ─────────────── (1) INVESTMENT_PROFILE description: Each property has exactly one investment profile containing ROI, risk rating, and investment classification. 1 to 1 type