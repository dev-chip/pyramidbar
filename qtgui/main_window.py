# -------------------------------------------------------------------------------
# Name:        main_window.py
# Purpose:     Main window example.
#
# Author:      James Cook
#
# Created:     30/09/2020
# Copyright:   (c) James Cook 2020
# -------------------------------------------------------------------------------

from qtgui.gen import MainWindowGenerated
from qtgui.window import Window
from qtgui.logger import init_console_logger

from PyQt5.QtWidgets import QTableWidgetItem
import time
import os

from qtgui.show_dialog import (show_message_dialog,
                               show_confirm_dialog,
                               show_line_edit_dialog,
                               NumpadDialog)

from core.drinks import (rum,
                         whiskey,
                         vodka,
                         gin,
                         amaretto,
                         cocktails,
                         all_drinks,
                         bottles)
from core.tabs import (load_tabs,
                       save_tabs)
from core.sales import append_sale, SALES_PATH
from core.topup import append_topup, TOPUP_PATH

logger = init_console_logger(name="gui")


class MainWindow(Window):

    def __init__(self):

        logger.debug("Setting up UI")
        super(Window, self).__init__()
        self.ui = MainWindowGenerated.Ui_MainWindow()
        self.ui.setupUi(self)

        logger.verbose("Initialising GUI logger")
        self.init_GUI_logger(logger)
        self.ui.textEdit.setVisible(False)
        self.ui.menuLog_Level.setEnabled(False)

        logger.verbose("Initialising signals")
        self.init_signals()

        logger.verbose("Setting up menu table widget...")
        self.menu_buttons = [self.ui.pushButton_all,
                             self.ui.pushButton_rum,
                             self.ui.pushButton_whiskey,
                             self.ui.pushButton_vodka,
                             self.ui.pushButton_gin,
                             self.ui.pushButton_amaretto,
                             self.ui.pushButton_cocktails,
                             self.ui.pushButton_bottles]
        self.ui.tableWidget_menu.setColumnWidth(0, 270)
        self.ui.tableWidget_menu.setColumnWidth(1, 80)
        self.menu_all()

        logger.verbose("Setting up till table widget...")
        self.ui.tableWidget_till.setColumnWidth(0, 230)
        self.ui.tableWidget_till.setColumnWidth(1, 80)

        logger.verbose("Setting up tab table widget...")
        self.load_tabs()
        self.ui.tableWidget_tabs.setColumnWidth(0, 190)
        self.ui.tableWidget_tabs.setColumnWidth(1, 80)

        self.last_sale = time.time()

        logger.info("GUI initialised")

    def init_signals(self):
        """
            Initialises widget signals
        """
        self.ui.actionToggle_developer_log.triggered.connect(self.toggle_developer_log)
        self.ui.action_manually_set_tab.triggered.connect(self.manually_set_tab)
        self.ui.action_update_tabs_from_file.triggered.connect(self.load_tabs)

        self.ui.actionAdd_patron.triggered.connect(self.add_tab)
        self.ui.actionRemove_patron.triggered.connect(self.remove_tab)

        self.ui.action_open_top_up_log.triggered.connect(self.open_topup_log_file)
        self.ui.action_open_sales_log.triggered.connect(self.open_sales_log_file)


        self.ui.pushButton_all.clicked.connect(self.menu_all)
        self.ui.pushButton_rum.clicked.connect(self.menu_rum)
        self.ui.pushButton_whiskey.clicked.connect(self.menu_whiskey)
        self.ui.pushButton_vodka.clicked.connect(self.menu_vodka)
        self.ui.pushButton_gin.clicked.connect(self.menu_gin)
        self.ui.pushButton_amaretto.clicked.connect(self.menu_amaretto)
        self.ui.pushButton_cocktails.clicked.connect(self.menu_cocktails)
        self.ui.pushButton_bottles.clicked.connect(self.menu_bottles)

        self.ui.tableWidget_menu.cellClicked.connect(self.add_selected_item_to_till)
        self.ui.tableWidget_till.cellClicked.connect(self.till_item_selected)
        self.ui.tableWidget_tabs.cellClicked.connect(self.tab_item_selected)

        self.ui.pushButton_clear.clicked.connect(self.clear_till)
        self.ui.pushButton_remove_item.clicked.connect(self.remove_item)
        self.ui.pushButton_manual_item.clicked.connect(self.manual_item)

        self.ui.pushButton_charge.clicked.connect(self.charge)
        self.ui.pushButton_top_up.clicked.connect(self.top_up)

    def menu_all(self):
        logger.debug("showing menu 'all'")
        self.enable_all_menu_buttons()
        self.ui.pushButton_all.setEnabled(False)
        self.set_menu_items(all_drinks)

    def menu_rum(self):
        logger.debug("showing menu 'rum'")
        self.enable_all_menu_buttons()
        self.ui.pushButton_rum.setEnabled(False)
        self.set_menu_items(rum)

    def menu_whiskey(self):
        logger.debug("showing menu 'whiskey'")
        self.enable_all_menu_buttons()
        self.ui.pushButton_whiskey.setEnabled(False)
        self.set_menu_items(whiskey)

    def menu_vodka(self):
        logger.debug("showing menu 'vodka'")
        self.enable_all_menu_buttons()
        self.ui.pushButton_vodka.setEnabled(False)
        self.set_menu_items(vodka)

    def menu_gin(self):
        logger.debug("showing menu 'gin'")
        self.enable_all_menu_buttons()
        self.ui.pushButton_gin.setEnabled(False)
        self.set_menu_items(gin)

    def menu_amaretto(self):
        logger.debug("showing menu 'amaretto'")
        self.enable_all_menu_buttons()
        self.ui.pushButton_amaretto.setEnabled(False)
        self.set_menu_items(amaretto)

    def menu_cocktails(self):
        logger.debug("showing menu 'cocktails'")
        self.enable_all_menu_buttons()
        self.ui.pushButton_cocktails.setEnabled(False)
        self.set_menu_items(cocktails)

    def menu_bottles(self):
        logger.debug("showing menu 'bottles'")
        self.enable_all_menu_buttons()
        self.ui.pushButton_bottles.setEnabled(False)
        self.set_menu_items(bottles)

    def toggle_developer_log(self):
        self.ui.textEdit.setVisible(not self.ui.textEdit.isVisible())
        self.ui.menuLog_Level.setEnabled(self.ui.textEdit.isVisible())
        logger.debug("toggled developer log to {}".format(self.ui.textEdit.isVisible()))

    def set_menu_items(self, items):
        self.ui.tableWidget_menu.setRowCount(len(items))
        for r, row in enumerate(items):
            self.ui.tableWidget_menu.setItem(r, 0, QTableWidgetItem(str(row[0])))
            self.ui.tableWidget_menu.setItem(r, 1, QTableWidgetItem("%.2f" % float(row[1])))

    def enable_all_menu_buttons(self):
        for b in self.menu_buttons:
            b.setEnabled(True)

    def add_selected_item_to_till(self, row, column):
        """ adds an item selected in the menu widget to the till """
        logger.debug("menu item at ({},{}) selected".format(row, column))
        self.ui.tableWidget_menu.clearFocus()
        self.ui.pushButton_clear.setEnabled(True)

        item = self.ui.tableWidget_menu.item(row, 0).text()
        price = self.ui.tableWidget_menu.item(row, 1).text()

        till_row = self.ui.tableWidget_till.rowCount()
        self.ui.tableWidget_till.setRowCount(till_row+1)
        self.ui.tableWidget_till.setItem(till_row, 0, QTableWidgetItem(str(item)))
        self.ui.tableWidget_till.setItem(till_row, 1, QTableWidgetItem("%.2f" % float(str(price))))
        self.update_total()
        if len(self.ui.tableWidget_tabs.selectedItems()) > 0:
            self.ui.pushButton_charge.setEnabled(True)

    def charge(self):
        """ charges the drinks on the till widget to the customer who is currently selected """
        total = float(self.ui.label_total_value.text())
        tab_row = self.ui.tableWidget_tabs.selectedItems()[0].row()
        tab_balance = float(self.ui.tableWidget_tabs.item(tab_row, 1).text())
        patron_name = str(self.ui.tableWidget_tabs.item(tab_row, 0).text())
        new_balance = tab_balance - total
        if new_balance < 0:
            if not show_confirm_dialog("{}'s balance is currently £{} and will be £{} after this sale. Continue?".format(
                    patron_name, "%.2f" % tab_balance, "%.2f" % new_balance)):
                return
        self.ui.tableWidget_tabs.setItem(tab_row, 1, QTableWidgetItem("%.2f" % new_balance))
        self.append_sales_to_log()
        txt = ""
        for r in range(self.ui.tableWidget_till.rowCount()):
            txt += "\n    " + str(self.ui.tableWidget_till.item(r, 0).text()) + " £" + "%.2f" % float(self.ui.tableWidget_till.item(r, 1).text())
        self.append_to_history("{} spent £{}".format(patron_name, "%.2f" % total) + txt)
        self.clear_till()
        self.save_tabs()


    def top_up(self):
        """ adds credit to a customer's tab """
        tab_row = self.ui.tableWidget_tabs.selectedItems()[0].row()
        tab_balance = float(self.ui.tableWidget_tabs.item(tab_row, 1).text())
        patron_name = str(self.ui.tableWidget_tabs.item(tab_row, 0).text())

        dialog = NumpadDialog()
        dialog.exec_()
        topup_amount = float(dialog.ui.lineEdit.text())
        if not dialog.confirmed or topup_amount == 0:
            return
        new_balance = topup_amount + tab_balance
        self.ui.tableWidget_tabs.setItem(tab_row, 1, QTableWidgetItem("%.2f" % new_balance))
        self.append_to_history("{} topped-up £{}".format(patron_name, "%.2f" % topup_amount))
        append_topup(patron_name, topup_amount)
        self.save_tabs()

    def clear_till(self):
        """ clears all items in the till table widget """
        self.ui.tableWidget_till.setRowCount(0)
        self.update_total()
        self.ui.pushButton_remove_item.setEnabled(False)
        self.ui.pushButton_clear.setEnabled(False)
        self.ui.pushButton_charge.setEnabled(False)

    def remove_item(self):
        """ removes the item selected from the till widget """
        row = self.ui.tableWidget_till.selectedItems()[0].row()
        logger.debug("removing till item in row {}".format(row))
        self.ui.tableWidget_till.removeRow(row)
        self.ui.tableWidget_till.clearFocus()
        self.update_total()
        if self.ui.tableWidget_till.rowCount() == 0:
            self.ui.pushButton_remove_item.setEnabled(False)
            self.ui.pushButton_charge.setEnabled(False)

    def manual_item(self):
        """ opens the numpad dialog and adds a till item of a manual value as 'manual' """
        logger.debug("adding manual item amount...")
        dialog = NumpadDialog()
        dialog.exec_()
        value = float(dialog.ui.lineEdit.text())
        if not dialog.confirmed or value == 0:
            return

        self.ui.pushButton_clear.setEnabled(True)

        item = "Manual"
        price = float(value)

        till_row = self.ui.tableWidget_till.rowCount()
        self.ui.tableWidget_till.setRowCount(till_row + 1)
        self.ui.tableWidget_till.setItem(till_row, 0, QTableWidgetItem(str(item)))
        self.ui.tableWidget_till.setItem(till_row, 1, QTableWidgetItem("%.2f" % float(str(price))))
        self.update_total()
        if len(self.ui.tableWidget_tabs.selectedItems()) > 0:
            self.ui.pushButton_charge.setEnabled(True)
        logger.debug("manual item with price {} added".format("%.2f" % float(str(price))))

    def update_total(self):
        """ updates the sum of all items on the till table widget """
        logger.debug("Updating total...")
        r = 0
        till_row_count = self.ui.tableWidget_till.rowCount()
        total = float(0.0)
        while r < till_row_count:
            total += float(str(self.ui.tableWidget_till.item(r, 1).text()))
            r += 1
        logger.debug("Total calculated: {}".format(total))
        self.ui.label_total_value.setText("%.2f" % float(total))

    def add_tab(self):
        """ adds a new customer to the tabs widget """
        result, name = show_line_edit_dialog("Enter patron's name.")
        if result and name != "":
            tab_row = self.ui.tableWidget_tabs.rowCount()
            self.ui.tableWidget_tabs.setRowCount(tab_row + 1)
            self.ui.tableWidget_tabs.setItem(tab_row, 0, QTableWidgetItem(str(name)))
            self.ui.tableWidget_tabs.setItem(tab_row, 1, QTableWidgetItem("%.2f" % 0.0))
        self.save_tabs()

    def remove_tab(self):
        """ deletes a customer from the tabs widget """
        if len(self.ui.tableWidget_tabs.selectedItems()) == 0:
            show_message_dialog("You must first select a patron.")
            return
        tab_row = self.ui.tableWidget_tabs.selectedItems()[0].row()
        patron = str(self.ui.tableWidget_tabs.item(tab_row, 0).text())
        balance = float(self.ui.tableWidget_tabs.item(tab_row, 1).text())
        if show_confirm_dialog("Confirm deleting {}'s tab with balance £{}.".format(patron, "%.2f" % balance)):
            self.ui.tableWidget_tabs.removeRow(tab_row)
        self.save_tabs()

    def load_tabs(self):
        """ loads the names and balances of all patrons """
        tabs = load_tabs()
        self.ui.tableWidget_tabs.setRowCount(len(tabs))
        for r, data in enumerate(tabs):
            self.ui.tableWidget_tabs.setItem(r, 0, QTableWidgetItem(str(data[0])))
            self.ui.tableWidget_tabs.setItem(r, 1, QTableWidgetItem("%.2f" % float(data[1])))

    def save_tabs(self):
        """ saves the names and balances of all patrons """
        logger.debug("saving tabs...")
        data = []
        for r in range(self.ui.tableWidget_tabs.rowCount()):
            data.append([self.ui.tableWidget_tabs.item(r, 0).text(),
                         self.ui.tableWidget_tabs.item(r, 1).text()])
        logger.debug("tabs to be saved: {}".format(data))
        save_tabs(data)
        logger.debug("saved tabs")

    def append_sales_to_log(self):
        """ appends a drink to the log file """
        logger.debug("appending sale to sale log...")
        patron = str(self.ui.tableWidget_tabs.item(self.ui.tableWidget_tabs.selectedItems()[0].row(), 0).text())
        for r in range(self.ui.tableWidget_till.rowCount()):
            append_sale(str(self.ui.tableWidget_till.item(r, 0).text()),
                        str(self.ui.tableWidget_till.item(r, 1).text()),
                        patron)
        logger.debug("sale saved")

    def manually_set_tab(self):
        if len(self.ui.tableWidget_tabs.selectedItems()) == 0:
            show_message_dialog("You must first select a patron.")
            return
        tab_row = self.ui.tableWidget_tabs.selectedItems()[0].row()
        patron = str(self.ui.tableWidget_tabs.item(tab_row, 0).text())
        old_tab = float(self.ui.tableWidget_tabs.item(tab_row, 1).text())

        dialog = NumpadDialog()
        dialog.exec_()
        new_tab = float(dialog.ui.lineEdit.text())
        if dialog.confirmed and new_tab != 0:
            if show_confirm_dialog("Confirm {}'s tab to be set from £{} to £{}.".format(patron, ("%.2f" % old_tab), ("%.2f" % new_tab))):
                self.ui.tableWidget_tabs.setItem(tab_row, 1, QTableWidgetItem("%.2f" % new_tab))
        self.save_tabs()

    def till_item_selected(self, row, column):
        logger.debug("till item at ({},{}) selected".format(row, column))
        self.ui.pushButton_remove_item.setEnabled(True)

    def tab_item_selected(self, row, column):
        logger.debug("tab item at ({},{}) selected".format(row, column))
        self.ui.pushButton_top_up.setEnabled(True)
        if float(self.ui.label_total_value.text()) != 0:
            self.ui.pushButton_charge.setEnabled(True)

    def append_to_history(self, text):
        if self.last_sale < (time.time() - (10 * 60)):  # blank line after 10 minutes of no-sale
            self.ui.textEdit_history.append("")
        self.last_sale = time.time()
        self.ui.textEdit_history.append("[{}] {}".format(time.strftime("%H:%M:%S"), text))

    def open_topup_log_file(self):
        os.system("start " + TOPUP_PATH)

    def open_sales_log_file(self):
        os.system("start " + SALES_PATH)


if __name__ == "__main__":
    print ("No module test implemented.")