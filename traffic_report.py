import csv
from datetime import datetime
from collections import defaultdict


class TrafficReportGenerator:
    def __init__(self, file_path):
        self.records = self.load_data(file_path)

    def load_data(self, file_path):
        result = []
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            header = next(reader)   # skip the header
            for line in reader:
                timestamp = line[0]
                datetime_obj = datetime.fromisoformat(timestamp)
                count = int(line[1])
                result.append((datetime_obj, count))
        return result

    def total_cars(self):
        return sum(count for _, count in self.records)

    def daily_cars_count(self):
        result = defaultdict(int)
        for datetime_obj, count in self.records:
            day = datetime_obj.date()
            result[day] += count
        return result

    def top_3_half_hours_cars(self):
        return sorted(self.records, key=lambda x: x[1], reverse=True)[:3]

    def least_cars_1_5_hour_period(self):
        cars_1_5_hour_period = []
        for i in range(0, len(self.records) - 2):
            t1, c1 = self.records[i]
            t2, c2 = self.records[i + 1]
            t3, c3 = self.records[i + 2]

            # Check if there are 3 contiguous half hour records
            if (t2 - t1).seconds == 1800 and (t3 - t2).seconds == 1800:
                cars_1_5_hour_period.append((t1, c1 + c2 + c3))
        result = sorted(cars_1_5_hour_period, key=lambda x: x[1])[0]
        return f"{result[0].isoformat()} {result[1]}"

    def generate_report(self):
        print(f"The number of cars seen in total: {self.total_cars()}")
        print("\nCars seen per day (date in yyyy-mm-dd format):")
        for date, count in self.daily_cars_count().items():
            print(f"{date} {count}")
        print("\nThe top 3 half hours with most cars:")
        for datetime_obj, count in self.top_3_half_hours_cars():
            print(f"{datetime_obj.isoformat()} {count}")
        print(f"\n1.5 hour period with least cars: \n{self.least_cars_1_5_hour_period()}")
