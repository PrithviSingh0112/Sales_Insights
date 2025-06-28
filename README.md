![image](https://github.com/user-attachments/assets/842df8fb-42ac-4bd0-b708-98692a08d6d9)# 📊 Sales Insights Report

This project provides a data-driven analysis of sales performance across different product categories using Python and Pandas. It includes detailed profitability evaluations and identifies key factors influencing sales trends.

## 🚀 Project Overview

The goal is to derive actionable insights from sales data by analyzing:
- Total sales by category
- Profitability by category
- Performance evaluation of different product segments

This project can guide business decisions related to inventory planning, marketing focus, and strategic investments.

## 📁 Dataset Overview

Three CSV files are used:
1. `69BB0A36.csv` – Contains order information (Order ID, Customer details, Order Date, Location)
2. `2AF2B2F9.csv` – Contains order details (Order ID, Amount, Profit, Quantity, Category, Sub-Category)
3. `BB2194EF.csv` – Contains the month extracted from Order Dates for temporal analysis

The datasets are merged using the `Order ID` column.

## 🛠️ Tools & Libraries Used

- **Pandas** – For data manipulation and analysis
- **Matplotlib / Seaborn** *(if used)* – For visualizing trends and performance
- **Jupyter Notebook** – For interactive code development and presentation

## 🧮 Code Snippets & Logic

### 🔗 Merging Datasets
```python
import pandas as pd

order = pd.read_csv('69BB0A36.csv')
order_details = pd.read_csv('2AF2B2F9.csv')
target = pd.read_csv('BB2194EF.csv')

merge_df = pd.merge(order, order_details, on='Order ID')
```

### 💰 Total Sales by Category
```python
category_sales = merge_df.groupby("Category")["Amount"].sum().reset_index()
category_sales = category_sales.sort_values(by="Amount", ascending=False)
print(category_sales)
```

### 📈 Profit Margin and Avg Profit per Order
```python
merge_df['Profit Margin (%)'] = (merge_df['Profit'] / merge_df['Amount']) * 100

category_profit = merge_df.groupby('Category').agg({
    'Profit': 'sum',
    'Amount': 'sum',
    'Order ID': 'nunique'
}).reset_index()

category_profit['Avg Profit per Order'] = category_profit['Profit'] / category_profit['Order ID']
category_profit['Profit Margin (%)'] = (category_profit['Profit'] / category_profit['Amount']) * 100
```

## 🏆 Key Insights

- Categories with the highest sales volume
- Most profitable categories by margin and per-order averages
- Underperforming segments and potential reasons

## 📊 Visuals

Charts and bar plots are included in the notebook to:
- Compare sales and profit across categories
- Highlight trends and outliers in category performance

## 📌 How to Run

1. Clone this repository or download the files.
2. Install required libraries (if not already):
```bash
pip install pandas matplotlib seaborn
```
3. Launch Jupyter Notebook:
```bash
jupyter notebook Sales_Insights.ipynb
```
4. Execute the cells to see the full analysis.

---

## 🧠 Future Improvements

- Add monthly trend analysis
- Include customer segmentation
- Apply machine learning models for demand forecasting

  <h2>🖼️ Dashboard Previews</h2>

<table>
  <tr>
    <td><img src="assets/Dashboard1.png" width="400"/></td>
    <td><img src="assets/Furniture.png" width="400"/></td>
  </tr>
  <tr>
    <td><img src="assets/Clothing.png" width="400"/></td>
    <td><img src="assets/Electronics.png" width="400"/></td>
  </tr>
</table>


## 📬 Contact

For queries or collaborations, feel free to connect with the author.
