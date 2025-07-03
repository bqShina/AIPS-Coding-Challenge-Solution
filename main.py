"""
Traffic Report Generator

Author: Shina Qin

How to run the program:
-----------------------
1. Make sure you have Python 3 installed.
2. Prepare your CSV data file (e.g., 'traffic_data.csv') with the format:
    timestamp,count
    2021-12-01T05:00:00,5
    2021-12-01T05:30:00,12
    ...

3. Run the program:
    python main.py traffic_data.csv

How to run the tests:
---------------------
Run the tests using unittest:
    python -m unittest test_traffic_report.py
"""

from traffic_report import TrafficReportGenerator

reportGenerator = TrafficReportGenerator('traffic_data.csv')
reportGenerator.generate_report()

