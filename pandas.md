### Brief Tutorial on Pandas Library in Python
**Pandas** is a powerful and versatile library for data manipulation and analysis. It provides two main data structures: `Series` and `DataFrame`.

---

### 1. **Getting Started**
```python
import pandas as pd
```

### 2. **Pandas Data Structures**
#### **Series**
A `Series` is a one-dimensional labeled array.

```python
data = [10, 20, 30, 40]
s = pd.Series(data, index=['a', 'b', 'c', 'd'])
print(s)
```

#### **DataFrame**
A `DataFrame` is a two-dimensional labeled data structure.

```python
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}
df = pd.DataFrame(data)
print(df)
```

---

### 3. **Reading and Writing Data**
- **Read a CSV file**
  ```python
  df = pd.read_csv("data.csv")
  ```
- **Write to a CSV file**
  ```python
  df.to_csv("output.csv", index=False)
  ```

---

### 4. **Exploring the Data**
- **View the first/last few rows**
  ```python
  print(df.head())   # First 5 rows
  print(df.tail())   # Last 5 rows
  ```
- **Get basic info about the DataFrame**
  ```python
  print(df.info())
  print(df.describe())  # Summary statistics for numerical columns
  ```

---

### 5. **Data Selection and Filtering**
- **Select a column**
  ```python
  print(df["Name"])  # Returns a Series
  ```
- **Select multiple columns**
  ```python
  print(df[["Name", "Age"]])
  ```
- **Filter rows**
  ```python
  filtered_df = df[df["Age"] > 30]
  print(filtered_df)
  ```

---

### 6. **Data Cleaning**
- **Handle missing values**
  ```python
  df.fillna(0, inplace=True)  # Replace NaN with 0
  df.dropna(inplace=True)     # Drop rows with NaN
  ```
- **Rename columns**
  ```python
  df.rename(columns={"Name": "FullName"}, inplace=True)
  ```

---

### 7. **Data Aggregation and Grouping**
- **Group by a column**
  ```python
  grouped = df.groupby("City")["Age"].mean()
  print(grouped)
  ```
- **Aggregate multiple metrics**
  ```python
  agg = df.groupby("City").agg({"Age": ["mean", "max"], "Name": "count"})
  print(agg)
  ```

---

### 8. **Merging and Joining**
- **Merge two DataFrames**
  ```python
  df1 = pd.DataFrame({"ID": [1, 2], "Name": ["Alice", "Bob"]})
  df2 = pd.DataFrame({"ID": [1, 2], "Age": [25, 30]})
  merged = pd.merge(df1, df2, on="ID")
  print(merged)
  ```

---

### 9. **Visualization**
- **Plotting with Pandas**
  ```python
  df["Age"].plot(kind="hist")  # Histogram
  df.plot(x="Age", y="SpendingScore", kind="scatter")  # Scatter plot
  ```

---

### 10. **Advanced Operations**
- **Apply custom functions**
  ```python
  df["AgeCategory"] = df["Age"].apply(lambda x: "Adult" if x >= 18 else "Minor")
  ```
- **Pivot tables**
  ```python
  pivot = df.pivot_table(values="SpendingScore", index="City", columns="Gender", aggfunc="mean")
  print(pivot)
  ```

---

This tutorial provides an overview of essential Pandas functionalities. Try applying these concepts to your dataset!
