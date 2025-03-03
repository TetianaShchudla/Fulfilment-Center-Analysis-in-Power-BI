# 📊 3PL Fulfillment Center Performance Dashboard

This repository contains a **Power BI dashboard** that tracks the performance of **8 fulfillment centers (FCs) in France** across key operational metrics. 

The data is **synthetically generated** using Python to simulate realistic fulfillment center operations over the year **2024**.

---

## 🚀 Project Overview

### Objective of the Project:
This project aims to create a dashboard to **track and evaluate the performance** of fulfillment centers. It visualizes key metrics like delivery rates, cycle times, accuracy and costs to help optimize efficiency and identify areas for improvement.

The **dashboard** visualizes the following five critical KPIs:

- 📦 **On-Time Delivery Rate (%)**: Percentage of orders delivered within the promised timeframe.
- ⏳ **Total Order Cycle Time (Days)**: Average time taken from order placement to delivery.
- ✅ **Order Picking Accuracy Rate (%)**: Percentage of items accurately picked for shipment.
- 📊 **Inventory Accuracy Rate (%)**: Ratio of physical inventory to recorded inventory.
- 💰 **Average Cost per Order ($)**: Average cost incurred to fulfill an order.

---

### What is a Fulfillment Center?

A **fulfillment center (FC)** is a warehouse where products are stored, orders are processed, and shipments are made. Fulfillment centers manage inventory, pick, pack, and ship orders to customers, ensuring timely delivery and efficient operations.

### What is 3PL (Third-Party Logistics)?

**3PL** refers to outsourcing logistics services to a third-party provider. This includes tasks like storage, order fulfillment, and shipping. Companies partner with 3PLs to streamline their supply chain and focus on core business activities while leaving logistics management to experts.

In the context of this project, **fulfillment centers** are a crucial part of the 3PL network. They help manage the storage and shipping of products, ensuring timely delivery and operational efficiency. By using 3PL services, businesses can scale operations and optimize their supply chain without managing the complexities of logistics themselves.

![image](https://github.com/user-attachments/assets/d84144e9-559f-4f16-b1e1-601b3c17c860)
---

## 📊 Data Generation Process

Data for the dashboard is generated using a **Python script** (`generate_data.py`), which simulates daily operations for **8 fulfillment centers** from **January 1, 2024, to December 31, 2024**.

### 🛠️ Key Data Generation Logic:

- **Fulfillment Center Groups**:
    - **High Volume**: FC 1, FC 5 (1M–1.2M orders/year)  
    - **Medium Volume**: FC 2, FC 8 (800K–970K orders/year)  
    - **Low Volume**: FC 3, FC 6 (500K–790K orders/year)  
    - **Small Volume**: FC 4, FC 7 (100K–400K orders/year)  

- **Special Conditions**:
    - **FC 3**: Lower on-time delivery in **September–November** (95–98.5%).  
    - **FC 3 & FC 6**: Reduced picking and inventory accuracy during **May–June** (97–98%).  
    - **Order Cycle Time**: Increases slightly if delivery performance drops (<99.48%).  

---

## 📊 Data Model (Power BI)

The dashboard follows a **star schema**:

1. **Fact Table**: `fulfillment_center_data.csv`  
   - Contains all operational KPIs with daily records per fulfillment center.  
2. **Dimension Tables**:
   - **Date**: Calendar table for time-based analysis.  
   - **Fulfillment Center**: Metadata for center categorization.  

---

## 📊 Dashboard Insights

1. **On-Time Delivery Challenges (FC 3)**:
   - On-time delivery for **FC 3** dropped **below 96%** from **September to November**.
   - Recovery in **December** with a rate of **99.71%**.
   - This decline **slightly increased** the **order cycle time** to **2.01–2.10 days** during these months.  

2. **Accuracy Issues (FC 3 & FC 6)**:
   - **Order picking accuracy** fell during **May and June** for **FC 3** and **FC 6** (97–98%).  
   - This resulted in a **lower inventory accuracy rate** during these months, highlighting potential operational bottlenecks.  

---

## 📊 How to Reproduce

1. **Generate Data**:  
Ensure you have **Python** and **Pandas** installed. Run the `generate_data.py` script to generate the data. Alternatively, you can import the Python script directly into Power BI using the **Get Data** option.

2. **Load the Dashboard in Power BI**:  
Open `3PL Fulfillment Dashboard.pbix` in Microsoft Power BI to load the dashboard.


## 📹 Demo Video

Watch the demo video below to see the 3PL Fulfillment Center Performance Dashboard in action:

https://github.com/user-attachments/assets/109cadc2-f8aa-4cf6-bde5-dbdada862726


## 📊 Future Improvements
- Incorporate forecasting for future delivery and accuracy trends.
- Add geospatial analysis to track performance across regions.
- Implement dynamic alerts for KPI deviations.
