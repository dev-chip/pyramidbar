#
# Functions for reading and writing tab data
#
import csv
import os

TABS_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "tabs.csv"))


def load_tabs():
    """ returns an array of all tabs """
    with open(TABS_PATH, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        return [row for row in csv_reader]


def save_tabs(tabs):
    """ saves tabs to a file

        params
        -----------------
        tabs - 2d array of all tabs, e.g.: [["Kie", 10.00],
                                            ["Ben", 14.21]]

        returns
        -----------------
        0 - success
        1 - failed to save
    """
    for row in tabs:
        if len(row) != 2:
            return 1
    try:
        with open(TABS_PATH, mode='w', newline='') as csv_file:
            employee_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for tab in tabs:
                employee_writer.writerow(tab)
        return 0
    except Exception as e:
        return 1


if __name__ == "__main__":
    #print(save_tabs([["Kie", 10.00], ["Ben", 14.21]]))
    print(load_tabs())