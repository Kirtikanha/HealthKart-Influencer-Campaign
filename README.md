# HealthKart Influencer Campaign Dashboard 📊

## 📌 Overview

This is an open-source interactive dashboard to monitor the performance of influencer marketing campaigns for HealthKart. The dashboard helps visualize key metrics such as ROAS, revenue, orders, payouts, and influencer-wise performance insights.

## ✅ Features

* Simulated influencer campaign data (customizable)
* Campaign performance metrics (Revenue, Orders, Payout, ROAS)
* Top influencers by revenue
* Payout vs Revenue scatter plot
* CSV export of top influencers
* Interactive and easy-to-use interface via Streamlit

## 🗂️ Folder Structure

```
healthkart_influencer_dashboard/
│
├── Healthcart.py                  # Streamlit dashboard code
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

## 📁 Data Description

Data is simulated using Python libraries:

* `influencers`: ID, Name, Category, Gender, Followers, Platform
* `posts`: Influencer\_ID, Platform, Date, Reach, Likes, Comments
* `tracking_data`: Source, Campaign, Influencer\_ID, User\_ID, Product, Date, Orders, Revenue
* `payouts`: Influencer\_ID, Basis, Rate, Orders, Total\_Payout

> **Note:** Data is completely simulated for demonstrating dashboard features and does not reflect actual business figures.

## 🚀 How to Run

1. Clone the repository or download the code.
2. Install the required Python libraries:

```bash
pip install -r requirements.txt
```

3. Run the Streamlit dashboard:

```bash
streamlit run app.py
```

## 🛠️ Requirements

* Python 3.7+
* Libraries:

  * streamlit
  * pandas
  * numpy
  * plotly

## 🎁 Deliverables

* ✅ Streamlit interactive dashboard (`app.py`)
* ✅ Insights summary downloadable in CSV format
* ✅ Clean code with comments
* ✅ README with setup and feature description

## 📌 Notes

* This project uses **dummy data** to simulate influencer campaigns.
* Suitable for **HealthKart Intern Assignment** to showcase data analysis and product sense.

## 🏆 Author

**Prepared by:** \[Your Name]

---

For any queries, please feel free to contact me.

