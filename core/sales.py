#
# Functions for reading and writing tab data
#
import csv
import os
import time

SALES_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "sales.csv"))


def append_sale(item, price, customer):
    date_str = time.strftime("%Y-%m-%d")
    time_str = time.strftime("%H:%M:%S")
    try:
        with open(SALES_PATH, mode='a', newline='') as csv_file:
            employee_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            employee_writer.writerow([item, price, customer, date_str, time_str])
        return 0
    except Exception as e:
        return 1


if __name__ == "__main__":
    #print(save_tabs([["Kie", 10.00], ["Ben", 14.21]]))
    print(append_sale("the best stuff", 14.22, "alan"))