## Day 1 — Dataset Explorer

### Dataset
- Dataset: Titanic
- Rows: 891
- Original columns: 12
- Cleaned columns: 13

### Data Quality
- Age: 177 missing values → filled with median (28)
- Embarked: 2 missing values → filled with mode (S)
- Cabin: 687 missing values → retained and transformed into a `Deck` feature
- Deck: 0 missing values after transformation

### EDA Findings
- 577 male and 314 female passengers
- Overall survival rate: 38.4%
- Female survival rate: 74.2%
- Male survival rate: 18.9%
- 1st-class survival rate: 63.0%
- 2nd-class survival rate: 47.3%
- 3rd-class survival rate: 24.2%

### Concepts Learned
- Pandas DataFrame
- `shape`
- `columns`
- `info()`
- `isnull().sum()`
- `describe()`
- `value_counts()`
- `groupby()`
- `mean()`
- Matplotlib bar charts
- Missing-value handling
- Feature extraction
- Saving cleaned datasets with `to_csv()`