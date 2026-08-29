# Product Recommendation System — Master Roadmap

**Project Type:** Standalone ML / Recommendation System  
**Dataset Direction:** Retailrocket e-commerce dataset (broad behavioral marketplace data)  
**Primary Goal:** Build a generalized e-commerce recommendation engine capable of recommending products across a broad catalog using user behavior, product metadata, and hybrid ranking signals.

---

# Phase 0 — Project Definition & Scope

### 0.1 Problem Definition
- [x] Define the recommendation problem as personalized Top-K product recommendation.
- [x] Define primary users, products, interactions, and recommendation scenarios.
- [x] Define implicit vs. explicit feedback strategy.
- [x] Define cold-start requirements.
- [x] Define the distinction between training catalog and production-scale catalog.

### 0.2 Success Criteria
- [x] Define offline recommendation metrics.
- [x] Define business-oriented metrics.
- [x] Define latency and serving expectations.
- [x] Define minimum viable model and final target model.

### 0.3 Project Architecture
- [x] Define end-to-end ML architecture.
- [x] Define data ingestion pipeline.
- [x] Define feature/data storage strategy.
- [x] Define candidate-generation layer.
- [x] Define ranking layer.
- [x] Define recommendation API.
- [x] Define frontend/demo architecture.
- [x] Define monitoring and evaluation architecture.

---

# Phase 1 — Dataset Acquisition & Data Understanding

## 1.1 Dataset Acquisition
- [x] Obtain Retailrocket dataset.
- [x] Select relevant marketplace-wide data components.
- [x] Keep the original extracted CSV files under `data/raw/`.
- [x] Keep `data/processed/` reserved for derived/cleaned datasets.
- [x] Avoid modifying the raw source files.
- [x] Preserve reproducibility of dataset selection.
- [x] Create isolated Python virtual environment.
- [x] Install Phase 1 data/ML dependencies.
- [x] Install Jupyter/JupyterLab/Notebook and `ipykernel`.
- [x] Register the `recommendation-system` Jupyter kernel.
- [x] Freeze the current environment into `requirements.txt`.
- [x] Verify raw file integrity, schemas, sizes, and readable samples.
- [x] Complete dataset acquisition audit before locking Phase 1.1.

## 1.2 Dataset Inventory
- [x] Inspect behavioral interaction file (`events.csv`).
- [x] Inspect product-property files (`item_properties_part1.csv`, `item_properties_part2.csv`).
- [x] Inspect category hierarchy (`category_tree.csv`).
- [x] Inventory property IDs and property-value structure.
- [x] Determine which product properties can represent category, price, brand, description, or other product attributes.
- [x] Inspect timestamp coverage and timestamp semantics across files.
- [x] Inspect user/item identifier relationships.
- [x] Inspect product/category relationships where available.
- [x] Document exact schemas, row counts, file sizes, and key fields.
- [x] Create the Phase 1.2 dataset inventory report.

### Phase 1.2 Scope Note

The Retailrocket dataset does not expose separate `price`, `brand`, or `description` columns in the raw schema. Product metadata is represented through the generic `property` / `value` structure, so those concepts must be discovered and mapped from the available property IDs rather than assumed in advance.

The inventory will therefore establish the actual semantic structure of the raw product-property data before any feature engineering or cleaning begins.

### Planned Inventory Outputs

```text
notebooks/
└── 02_dataset_inventory.ipynb

docs/
└── dataset_inventory.md
```

No transformed dataset will be created during Phase 1.2. The purpose is to understand and document the raw data only.

## 1.3 Data Profiling
- [x] Measure number of users.
- [x] Measure number of products.
- [x] Measure number of interactions.
- [x] Measure interactions per user.
- [x] Measure interactions per product.
- [x] Analyze long-tail distribution.
- [x] Analyze category distribution.
- [x] Analyze rating distribution if a rating-like property is identified during inventory.
- [x] Analyze temporal distribution.
- [x] Measure sparsity of the user-item matrix.

## 1.4 Data Quality
- [x] Detect missing values.
- [x] Detect duplicate interactions.
- [x] Detect invalid product/user IDs.
- [x] Detect inconsistent metadata.
- [x] Analyze anomalous ratings/interactions.
- [x] Establish data-cleaning rules.

---

# Phase 2 — Data Engineering & Recommendation Dataset

## 2.1 Interaction Modeling
- [x] Define interaction types.
- [x] Define interaction weights.
- [x] Implicit-feedback approach
- [x] Construct user-item interaction records.
- [x] Decide how ratings/reviews contribute to preference signals.
- [x] Define negative/unknown interactions where appropriate.

## 2.2 User Dataset
- [x] Build user interaction history.
- [x] Aggregate user activity.
- [x] Create user-level statistics.
- [x] Create recency/frequency signals.
- [x] Define active/inactive users.

## 2.3 Product Dataset
- [x] Build canonical product table.
- [x] Clean/normalize category, brand, price, description, and product features where available.
- [x] Create product-level statistics.

## 2.4 Training Dataset & Splits
- [x] Create leakage-safe temporal train/validation/test splits.
- [x] Build final user-item training representation.
- [x] Save reproducible train/validation/test datasets.

---

# Phase 3 — Recommendation Modeling

## 3.1 Baselines
- [x] Build popularity baseline.
- [x] Build simple similar-item baseline.
- [x] Evaluate baseline Top-K quality.

## 3.2 Content-Based Recommendation
- [x] Build product representation from available metadata/features.
- [x] Build similarity search and Top-K recommendations.
- [x] Evaluate content-based recommendations.
- [x] Support new products where metadata is available.

## 3.3 Collaborative Filtering
- [ ] Build sparse user-item interaction matrix.
- [ ] Implement collaborative filtering / matrix-factorization baseline.
- [ ] Generate Top-K personalized recommendations.
- [ ] Compare collaborative performance with baselines.

## 3.4 Hybrid Recommendation Engine
- [ ] Combine collaborative, content, popularity, and recency signals.
- [ ] Build candidate generation.
- [ ] Build ranking/scoring layer.
- [ ] Add basic diversity and repetition controls.
- [ ] Select the strongest practical hybrid approach.

---

# Phase 4 — Evaluation & Edge Cases

## 4.1 Recommendation Evaluation
- [ ] Evaluate Precision@K, Recall@K, NDCG@K, and Hit Rate@K.
- [ ] Measure catalog/user coverage and diversity.
- [ ] Analyze popularity bias and long-tail performance.
- [ ] Compare baseline, content, collaborative, and hybrid models.

## 4.2 Cold Start & Error Analysis
- [ ] Define new-user recommendation strategy.
- [ ] Define new-product recommendation strategy.
- [ ] Analyze sparse-user and sparse-product failures.
- [ ] Document model limitations and final findings.

---

# Phase 5 — Final Model & Serving

## 5.1 Final Training
- [ ] Freeze the final feature/preprocessing pipeline.
- [ ] Train and save the final recommendation model/artifacts.
- [ ] Save required encoders, embeddings, indexes, and configuration.

## 5.2 Recommendation API
- [ ] Implement personalized Top-K endpoint.
- [ ] Implement similar-product endpoint.
- [ ] Implement cold-start/fallback behavior.
- [ ] Add validation, error handling, and latency measurement.

---

# Phase 6 — Frontend & Deployment

## 6.1 Product Recommendation Experience
- [ ] Build product discovery UI.
- [ ] Build personalized recommendations and similar-product views.
- [ ] Connect frontend to the recommendation API.

## 6.2 Deployment
- [ ] Deploy API/model service.
- [ ] Deploy frontend.
- [ ] Test production recommendation flows and latency.

## 6.3 Monitoring
- [ ] Monitor API health, latency, and errors.
- [ ] Monitor recommendation coverage/diversity/popularity.
- [ ] Define basic data/model degradation signals.

---

# Phase 7 — Documentation & Portfolio Lock

## 7.1 Documentation
- [ ] Finalize README and architecture documentation.
- [ ] Document dataset, preprocessing, models, evaluation, API, and deployment.
- [ ] Add architecture/recommendation pipeline visuals.

## 7.2 Final Verification
- [ ] Verify repository structure and reproducibility.
- [ ] Verify notebooks, API, frontend, and deployment.
- [ ] Verify no sensitive credentials are committed.

## 7.3 Project Lock
- [ ] Final model and metrics recorded.
- [ ] Demo/deployment URL finalized.
- [ ] GitHub repository finalized.
- [ ] Resume/LinkedIn-ready project summary finalized.

---

# Final Target Architecture

```text
Retailrocket Data
      │
      ├── User Interactions ──→ User Representation
      │
      └── Product Metadata ───→ Product Representation
                    │
                    ▼
            Candidate Generation
                    │
                    ▼
              Hybrid Ranking
                    │
                    ▼
              Policy / Filtering
                    │
                    ▼
                 Top-K
                    │
                    ▼
            Recommendation API
                    │
                    ▼
               Frontend Demo
                    │
                    ▼
          Evaluation & Monitoring
```

# Definition of Done

The project is complete when:

- [ ] Personalized Top-K recommendations work.
- [ ] Content + collaborative + fallback signals are combined appropriately.
- [ ] New users and new products have defined strategies.
- [ ] Recommendations are evaluated with ranking and system-level metrics.
- [ ] Final model is exposed through an API.
- [ ] Working frontend/demo is deployed.
- [ ] Documentation and repository are reproducible and portfolio-ready.
