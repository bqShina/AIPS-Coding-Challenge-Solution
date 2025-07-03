import unittest
from traffic_report import TrafficReportGenerator
from datetime import datetime
import tempfile
import os


class TestTrafficReportGenerator(unittest.TestCase):
    def setUp(self):
        # Create a temporary CSV file with sample data
        self.test_file = tempfile.NamedTemporaryFile(mode='w+', delete=False)
        self.test_file.write("timestamp,count\n")
        self.test_file.write("2021-12-01T05:00:00,5\n")
        self.test_file.write("2021-12-01T05:30:00,12\n")
        self.test_file.write("2021-12-01T06:00:00,14\n")
        self.test_file.write("2021-12-01T07:00:00,25\n")
        self.test_file.write("2021-12-01T07:30:00,46\n")
        self.test_file.write("2021-12-02T05:00:00,3\n")
        self.test_file.flush()
        self.report = TrafficReportGenerator(self.test_file.name)

    def tearDown(self):
        # Remove the temporary file
        os.unlink(self.test_file.name)

    def test_total_cars(self):
        self.assertEqual(self.report.total_cars(), 105)

    def test_daily_cars_count(self):
        daily = self.report.daily_cars_count()
        self.assertEqual(daily[datetime(2021, 12, 1).date()], 102)
        self.assertEqual(daily[datetime(2021, 12, 2).date()], 3)

    def test_top_3_half_hours_cars(self):
        top_3 = self.report.top_3_half_hours_cars()
        counts = [count for _, count in top_3]
        self.assertEqual(counts, [46, 25, 14])

    def test_least_cars_1_5_hour_period(self):
        result = self.report.least_cars_1_5_hour_period()
        self.assertIn("2021-12-01T05:00:00", result)
        self.assertTrue(result.endswith("31"))  # 5 + 12 + 14

    def test_load_data(self):
        self.assertEqual(len(self.report.records), 6)
        self.assertIsInstance(self.report.records[0][0], datetime)
        self.assertEqual(self.report.records[0][1], 5)

if __name__ == '__main__':
    unittest.main()
