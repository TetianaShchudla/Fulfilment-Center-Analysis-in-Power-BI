import pandas as pd
import numpy as np
import os
from datetime import datetime, timedelta

# Define fulfillment centers
fulfillment_centers = [f"FC {i}" for i in range(1, 9)]

# Define date range for 2024
date_range = pd.date_range(start="2024-01-01", end="2024-12-31")

# Create directory to store CSV files
output_dir = "star_format_data"
os.makedirs(output_dir, exist_ok=True)

# Function to generate orders based on center size
def generate_orders(fc):
    if fc in ["FC 1", "FC 5"]:
        return np.random.randint(1000000, 1200000)
    elif fc in ["FC 2", "FC 8"]:
        return np.random.randint(800000, 970000)
    elif fc in ["FC 3", "FC 6"]:
        return np.random.randint(500000, 790000)
    else:
        return np.random.randint(100000, 400000)

# Generate data
all_data = []

for date in date_range:
    for fc in fulfillment_centers:
        total_orders = generate_orders(fc)
        
        # On-time delivery rate
        if fc == "FC 3" and date.month in [9, 10, 11]:
            on_time_delivered = int(total_orders * np.random.uniform(0.95, 0.985))
        else:
            on_time_delivered = int(total_orders * np.random.uniform(0.9948, 1.0))
        on_time_delivery_rate = round((on_time_delivered / total_orders) * 100, 2)
        
        # Total order cycle time (days)
        total_order_cycle_time = round(np.random.uniform(0.6, 2.9), 2)
        if on_time_delivery_rate < 99.48:
            total_order_cycle_time += np.random.uniform(0.2, 0.5)
        total_order_cycle_time = min(max(total_order_cycle_time, 0.6), 2.9)
        
        # Order picking accuracy rate
        if fc in ["FC 3", "FC 6"] and date.month in [5, 6]:
            picked_accurately = int(total_orders * np.random.uniform(0.97, 0.98))
        else:
            picked_accurately = int(total_orders * np.random.uniform(0.99, 1.0))
        order_picking_accuracy_rate = round((picked_accurately / total_orders) * 100, 2)
        
        # Inventory accuracy rate
        if fc in ["FC 3", "FC 6"] and date.month in [5, 6]:
            physical_units = int(total_orders * np.random.uniform(0.98, 0.985))
        else:
            physical_units = int(total_orders * np.random.uniform(0.99, 1.0))
        recorded_units = total_orders  # Assume recorded units are always the total_orders value
        inventory_accuracy_rate = round((physical_units / recorded_units) * 100, 2)
        
        # Average cost per order for fulfillment
        avg_cost_per_order = round(np.random.uniform(3, 5), 2)
        if total_order_cycle_time > 2.5:
            avg_cost_per_order += np.random.uniform(0.5, 1.5)
        avg_cost_per_order = min(max(avg_cost_per_order, 2), 9)
        
        # Append data
        all_data.append([
            date.strftime("%Y-%m-%d"), fc, total_orders, on_time_delivered, on_time_delivery_rate,
            total_order_cycle_time, picked_accurately, order_picking_accuracy_rate,
            physical_units, recorded_units, inventory_accuracy_rate, avg_cost_per_order
        ])

# Create DataFrame
columns = [
    "Date", "Fulfillment Center", "Total Orders", "On-Time Delivered", "On-Time Delivery Rate (%)",
    "Total Order Cycle Time (Days)", "Picked Accurately", "Order Picking Accuracy Rate (%)",
    "Physical Units", "Recorded Units", "Inventory Accuracy Rate (%)", "Average Cost per Order ($)"
]
data_df = pd.DataFrame(all_data, columns=columns)

# Save to CSV
csv_path = os.path.join(output_dir, "fulfillment_center_data.csv")
data_df.to_csv(csv_path, index=False)

print(f"CSV file saved: {csv_path}")
