#
# Functions for reading and writing tab data
#
import csv
import os
import time

TOPUP_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "topup.csv"))


def append_topup(customer, amount):
    date_str = time.strftime("%Y-%m-%d")
    time_str = time.strftime("%H:%M:%S")
    try:
        with open(TOPUP_PATH, mode='a', newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow([customer, amount, date_str, time_str])
        return 0
    except Exception as e:
        return 1


if __name__ == "__main__":
    #print(save_tabs([["Kie", 10.00], ["Ben", 14.21]]))
    print(append_topup("test", 0.01))