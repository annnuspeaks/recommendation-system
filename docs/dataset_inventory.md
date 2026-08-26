# Dataset Inventory

## Dataset

**Dataset:** Retailrocket e-commerce dataset

**Purpose:** Product Recommendation System

The raw dataset is stored under:

```text
data/raw/
├── category_tree.csv
├── events.csv
├── item_properties_part1.csv
└── item_properties_part2.csv
```

Raw files are kept unchanged. Derived/processed data will be stored separately under `data/processed/`.

---

## 1. File Inventory

| File | Approx. Size | Rows |
|---|---:|---:|
| `events.csv` | 89.87 MB | 2,756,101 |
| `item_properties_part1.csv` | 461.88 MB | 10,999,999 |
| `item_properties_part2.csv` | 389.99 MB | 9,275,903 |
| `category_tree.csv` | 0.01 MB | 1,669 |

---

## 2. Schemas

### `events.csv`

```text
timestamp
visitorid
event
itemid
transactionid
```

Key fields:

- `timestamp` — event time
- `visitorid` — user/visitor identifier
- `event` — behavioral interaction type
- `itemid` — product identifier
- `transactionid` — transaction identifier where applicable

Observed event types:

```text
view
addtocart
transaction
```

---

### `item_properties_part1.csv`

```text
timestamp
itemid
property
value
```

### `item_properties_part2.csv`

```text
timestamp
itemid
property
value
```

These files contain product metadata in a generic property/value representation rather than separate raw columns for concepts such as price, brand, or description.

---

### `category_tree.csv`

```text
categoryid
parentid
```

The category tree contains **1,669 category records** and **25 root categories**.

---

## 3. Behavioral Interaction Inventory

The interaction data contains three principal behavioral signals:

```text
view
addtocart
transaction
```

These will form the basis of the project's implicit-feedback recommendation formulation.

---

## 4. Identifier Relationships

Verified from the raw data:

```text
Unique items in events:          235,061
Unique items in properties:      417,053
Event items with properties:     185,246
Event items without properties:   49,815
```

This establishes that the event and product-property datasets have substantial item overlap, while also containing items present in event data without corresponding observed properties.

---

## 5. Product / Category Structure

The category hierarchy is provided separately through `category_tree.csv`.

The raw product-property data uses the generic:

```text
itemid
property
value
```

structure.

A category-related property was identified in the product-property data, allowing category information to be associated with products through the property/value representation. The exact semantic mapping will be preserved and further validated during later feature engineering rather than assumed from column names.

---

## 6. Timestamp Coverage

Timestamps are present in both behavioral events and product-property records.

The timestamps will be used later for:

- temporal analysis
- chronological train/validation/test splitting
- recency features
- time-aware recommendation evaluation

Timestamp semantics and exact conversion will be handled during the data-engineering phase.

---

## 7. Inventory Conclusion

The raw dataset provides the core entities required for the recommendation system:

```text
Users
  ↓
Behavioral Events
  ↓
Products
  ↓
Product Properties
  ↓
Categories
```

The dataset is sufficiently structured to proceed to deeper profiling and data-engineering work.

No transformations were performed as part of this inventory report.
