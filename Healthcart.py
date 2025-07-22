# -*- coding: utf-8 -*-
"""
Created on Tue Jul 22 15:26:04 2025

@author: Kirti
"""

# HealthKart Influencer Campaign Dashboard

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# --------------- Dummy Data Creation ------------------
@st.cache_data
def load_data():
    np.random.seed(42)
    influencer_df = pd.DataFrame({
        'ID': range(1, 11),
        'Name': [f'Influencer {i}' for i in range(1, 11)],
        'Category': np.random.choice(['Fitness', 'Lifestyle', 'Nutrition'], 10),
        'Gender': np.random.choice(['Male', 'Female'], 10),
        'Followers': np.random.randint(10000, 500000, 10),
        'Platform': np.random.choice(['Instagram', 'YouTube'], 10)
    })

    posts_df = pd.DataFrame({
        'Influencer_ID': np.random.choice(influencer_df['ID'], 30),
        'Platform': np.random.choice(['Instagram', 'YouTube'], 30),
        'Date': pd.date_range(start='2024-01-01', periods=30),
        'Reach': np.random.randint(5000, 100000, 30),
        'Likes': np.random.randint(100, 5000, 30),
        'Comments': np.random.randint(10, 500, 30)
    })

    tracking_df = pd.DataFrame({
        'Source': 'Campaign',
        'Campaign': 'Summer Fit 2024',
        'Influencer_ID': np.random.choice(influencer_df['ID'], 50),
        'User_ID': np.arange(1, 51),
        'Product': np.random.choice(['Protein', 'Vitamin', 'Energy Drink'], 50),
        'Date': pd.date_range(start='2024-01-01', periods=50),
        'Orders': np.random.randint(1, 5, 50),
        'Revenue': np.random.randint(500, 5000, 50)
    })

    payouts_df = pd.DataFrame({
        'Influencer_ID': influencer_df['ID'],
        'Basis': np.random.choice(['post', 'order'], 10),
        'Rate': np.random.randint(1000, 5000, 10),
        'Orders': np.random.randint(10, 100, 10)
    })
    payouts_df['Total_Payout'] = payouts_df['Rate'] * payouts_df['Orders']

    return influencer_df, posts_df, tracking_df, payouts_df

influencer_df, posts_df, tracking_df, payouts_df = load_data()

# --------------- Streamlit Dashboard ------------------
st.title('HealthKart Influencer Campaign Dashboard')

st.header('Campaign Performance Summary')
total_revenue = tracking_df['Revenue'].sum()
total_orders = tracking_df['Orders'].sum()
total_payout = payouts_df['Total_Payout'].sum()
roas = total_revenue / total_payout if total_payout else 0

col1, col2, col3, col4 = st.columns(4)
col1.metric('Total Revenue (₹)', f'{total_revenue:,.0f}')
col2.metric('Total Orders', total_orders)
col3.metric('Total Payout (₹)', f'{total_payout:,.0f}')
col4.metric('ROAS', f'{roas:.2f}x')

st.header('Top Influencers by Revenue Generation')
merged = tracking_df.merge(influencer_df, left_on='Influencer_ID', right_on='ID')
top_influencers = merged.groupby('Name')['Revenue'].sum().sort_values(ascending=False).reset_index()
st.bar_chart(top_influencers.set_index('Name'))

st.header('Payout vs Revenue Scatter Plot')
influencer_revenue = merged.groupby('Influencer_ID')['Revenue'].sum().reset_index()
payout_revenue_df = payouts_df.merge(influencer_revenue, on='Influencer_ID')

fig = px.scatter(payout_revenue_df, x='Total_Payout', y='Revenue', 
                 hover_name=payout_revenue_df['Influencer_ID'],
                 title='Payout vs Revenue Comparison')

st.plotly_chart(fig)

st.header('Downloadable Insights')
@st.cache_data
def convert_df(df):
    return df.to_csv(index=False).encode('utf-8')

csv = convert_df(top_influencers)
st.download_button("Download Top Influencers CSV", data=csv, file_name='top_influencers.csv', mime='text/csv')

st.success("Dashboard Loaded Successfully 🎉")
