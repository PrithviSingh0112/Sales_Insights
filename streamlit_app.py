import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Title
st.title("📊 Sales Insights Dashboard")

# Upload CSV
uploaded_file = st.file_uploader("Upload Sales Data CSV", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Data Preview:", df.head())

    # Total sales
    st.metric("Total Revenue", f"${df['Amount'].sum():,.2f}")
    
    # Category-wise revenue
    category_rev = df.groupby("Category")["Amount"].sum().sort_values(ascending=False)
    st.subheader("Revenue by Category")
    st.bar_chart(category_rev)

    # Profit margin
    df['Profit Margin'] = (df['Profit'] / df['Amount']) * 100
    st.subheader("Profit Margin Distribution")
    fig, ax = plt.subplots()
    sns.histplot(df['Profit Margin'], kde=True, ax=ax)
    st.pyplot(fig)

    # Custom filters
    selected_category = st.selectbox("Select Category", df['Category'].unique())
    filtered = df[df['Category'] == selected_category]
    st.write(f"Summary for {selected_category}", filtered.describe())
