# 🚗 Traffic Report Generator

**Author:** Shina Qin

A Python program that reads traffic counter data from a CSV file and generates useful reports.

---

## 📦 Features

- Total number of cars seen
- Daily breakdown of traffic
- Top 3 busiest half-hour periods
- Lowest-traffic 1.5 hour window (3 consecutive half-hours)

---

## 🛠 How to Run the Program

1. **Make sure you have Python 3 installed.**

2. **Prepare your CSV file** (e.g., `traffic_data.csv`) with the following format:

   ```csv
   timestamp,count
   2021-12-01T05:00:00,5
   2021-12-01T05:30:00,12
   ...
3. **Run the program:**
  
   ```
   python main.py traffic_data.csv
   ```
4. **🧪 Running Tests**
  Use Python’s unittest module:
   ```
   python -m unittest test_traffic_report.py
   ```
