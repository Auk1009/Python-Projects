import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                           QHBoxLayout, QPushButton, QLabel, QLineEdit, 
                           QTableWidget, QTableWidgetItem, QMessageBox, 
                           QDialog, QRadioButton, QButtonGroup, QHeaderView)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPalette, QColor
from Bank_account import BankAccount

class StyleConfig:
    MAIN_BG = "#000000"  # Black background
    HEADER_BG = "#1a1a1a"  # Slightly lighter black for header
    HEADER_TEXT = "#ffffff"  # White text
    BUTTON_BG = "#333333"  # Dark gray buttons
    BUTTON_HOVER = "#4d4d4d"  # Lighter gray on hover
    SUCCESS_BUTTON = "#006400"  # Dark green for success actions
    TABLE_HEADER_BG = "#1a1a1a"  # Slightly lighter black for table header
    TABLE_HEADER_TEXT = "#ffffff"  # White text
    TEXT_COLOR = "#ffffff"  # White text for general use
    BORDER_COLOR = "#333333"  # Dark gray borders

class TransactionDialog(QDialog):
    def __init__(self, title, parent=None):
        super().__init__(parent)
        self.setWindowTitle(title)
        self.setMinimumWidth(400)
        self.setup_ui()
        # Set dialog style
        self.setStyleSheet(f"""
            QDialog {{
                background-color: {StyleConfig.MAIN_BG};
                color: {StyleConfig.TEXT_COLOR};
            }}
            QLabel {{
                color: {StyleConfig.TEXT_COLOR};
            }}
            QLineEdit {{
                background-color: {StyleConfig.BUTTON_BG};
                color: {StyleConfig.TEXT_COLOR};
                padding: 5px;
                border: 1px solid {StyleConfig.BORDER_COLOR};
                border-radius: 3px;
            }}
            QPushButton {{
                background-color: {StyleConfig.SUCCESS_BUTTON};
                color: {StyleConfig.TEXT_COLOR};
                padding: 10px;
                border: none;
                border-radius: 5px;
            }}
            QPushButton:hover {{
                background-color: #008000;
            }}
        """)

    def setup_ui(self):
        layout = QVBoxLayout()
        
        # Account Number
        self.acc_label = QLabel("Account Number:")
        self.acc_input = QLineEdit()
        layout.addWidget(self.acc_label)
        layout.addWidget(self.acc_input)
        
        # Amount (if needed)
        if "Balance" not in self.windowTitle():
            self.amount_label = QLabel("Amount:")
            self.amount_input = QLineEdit()
            layout.addWidget(self.amount_label)
            layout.addWidget(self.amount_input)
        
        # Submit Button
        self.submit_btn = QPushButton("Submit")
        self.submit_btn.setStyleSheet(f"background-color: {StyleConfig.SUCCESS_BUTTON}; color: white;")
        layout.addWidget(self.submit_btn)
        
        self.setLayout(layout)

class CreateAccountDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Create New Account")
        self.setMinimumWidth(400)
        self.setup_ui()
        # Set dialog style
        self.setStyleSheet(f"""
            QDialog {{
                background-color: {StyleConfig.MAIN_BG};
                color: {StyleConfig.TEXT_COLOR};
            }}
            QLabel {{
                color: {StyleConfig.TEXT_COLOR};
            }}
            QLineEdit {{
                background-color: {StyleConfig.BUTTON_BG};
                color: {StyleConfig.TEXT_COLOR};
                padding: 5px;
                border: 1px solid {StyleConfig.BORDER_COLOR};
                border-radius: 3px;
            }}
            QRadioButton {{
                color: {StyleConfig.TEXT_COLOR};
            }}
            QPushButton {{
                background-color: {StyleConfig.SUCCESS_BUTTON};
                color: {StyleConfig.TEXT_COLOR};
                padding: 10px;
                border: none;
                border-radius: 5px;
            }}
            QPushButton:hover {{
                background-color: #008000;
            }}
        """)

    def setup_ui(self):
        layout = QVBoxLayout()
        
        # Account Holder
        holder_label = QLabel("Account Holder:")
        self.holder_input = QLineEdit()
        layout.addWidget(holder_label)
        layout.addWidget(self.holder_input)
        
        # Account Type
        type_label = QLabel("Account Type:")
        layout.addWidget(type_label)
        
        type_layout = QHBoxLayout()
        self.type_group = QButtonGroup()
        
        savings_radio = QRadioButton("Savings")
        checking_radio = QRadioButton("Checking")
        savings_radio.setChecked(True)
        
        self.type_group.addButton(savings_radio)
        self.type_group.addButton(checking_radio)
        
        type_layout.addWidget(savings_radio)
        type_layout.addWidget(checking_radio)
        layout.addLayout(type_layout)
        
        # Create Button
        self.create_btn = QPushButton("Create Account")
        self.create_btn.setStyleSheet(f"background-color: {StyleConfig.SUCCESS_BUTTON}; color: white;")
        layout.addWidget(self.create_btn)
        
        self.setLayout(layout)

class BankAccountGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.bank = BankAccount()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Bank Account Management System")
        self.setMinimumSize(800, 600)
        
        # Create central widget and main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # Create header
        self.create_header(layout)
        
        # Create buttons
        self.create_buttons(layout)
        
        # Create account table
        self.create_account_table(layout)
        
        # Set window style
        self.setStyleSheet(f"background-color: {StyleConfig.MAIN_BG};")

    def create_header(self, layout):
        header = QLabel("Bank Account Management System")
        header.setAlignment(Qt.AlignCenter)
        header.setStyleSheet(f"""
            background-color: {StyleConfig.HEADER_BG};
            color: {StyleConfig.HEADER_TEXT};
            padding: 20px;
            font-size: 24px;
            font-weight: bold;
            border-bottom: 1px solid {StyleConfig.BORDER_COLOR};
        """)
        layout.addWidget(header)

    def create_buttons(self, layout):
        button_layout = QHBoxLayout()
        
        buttons = [
            ("Create Account", self.show_create_account),
            ("Deposit", self.show_deposit),
            ("Withdraw", self.show_withdraw),
            ("Check Balance", self.show_balance),
            ("Account Details", self.show_account_details)
        ]
        
        for text, slot in buttons:
            btn = QPushButton(text)
            btn.setStyleSheet(f"""
                QPushButton {{
                    background-color: {StyleConfig.BUTTON_BG};
                    color: {StyleConfig.TEXT_COLOR};
                    padding: 10px;
                    border: 1px solid {StyleConfig.BORDER_COLOR};
                    border-radius: 5px;
                }}
                QPushButton:hover {{
                    background-color: {StyleConfig.BUTTON_HOVER};
                }}
            """)
            btn.clicked.connect(slot)
            button_layout.addWidget(btn)
        
        layout.addLayout(button_layout)

    def create_account_table(self, layout):
        # Table Title
        table_title = QLabel("Existing Accounts")
        table_title.setAlignment(Qt.AlignCenter)
        table_title.setStyleSheet(f"""
            font-size: 18px;
            font-weight: bold;
            margin: 10px;
            color: {StyleConfig.TEXT_COLOR};
        """)
        layout.addWidget(table_title)
        
        # Create Table
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Account No.", "Account Holder", "Type", "Balance"])
        
        # Style the table
        self.table.setStyleSheet(f"""
            QTableWidget {{
                background-color: {StyleConfig.MAIN_BG};
                color: {StyleConfig.TEXT_COLOR};
                gridline-color: {StyleConfig.BORDER_COLOR};
                border: none;
            }}
            QHeaderView::section {{
                background-color: {StyleConfig.TABLE_HEADER_BG};
                color: {StyleConfig.TEXT_COLOR};
                padding: 8px;
                border: 1px solid {StyleConfig.BORDER_COLOR};
                font-weight: bold;
            }}
            QTableWidget::item {{
                padding: 5px;
                border-bottom: 1px solid {StyleConfig.BORDER_COLOR};
            }}
            QTableWidget::item:selected {{
                background-color: {StyleConfig.BUTTON_HOVER};
            }}
        """)
        
        # Set column widths
        header = self.table.horizontalHeader()
        for i in range(4):
            header.setSectionResizeMode(i, QHeaderView.Stretch)
        
        layout.addWidget(self.table)
        self.refresh_account_list()

    def refresh_account_list(self):
        self.table.setRowCount(0)
        for acc_num, details in self.bank.accounts.items():
            row = self.table.rowCount()
            self.table.insertRow(row)
            self.table.setItem(row, 0, QTableWidgetItem(acc_num))
            self.table.setItem(row, 1, QTableWidgetItem(details['holder']))
            self.table.setItem(row, 2, QTableWidgetItem(details['type']))
            self.table.setItem(row, 3, QTableWidgetItem(f"${details['balance']:.2f}"))

    def show_create_account(self):
        dialog = CreateAccountDialog(self)
        dialog.create_btn.clicked.connect(lambda: self.create_account(dialog))
        dialog.exec_()

    def create_account(self, dialog):
        holder = dialog.holder_input.text().strip()
        if holder:
            acc_type = "Savings" if dialog.type_group.buttons()[0].isChecked() else "Checking"
            acc_num = self.bank.create_account(holder, acc_type)
            QMessageBox.information(self, "Success", f"Account created successfully!\nAccount Number: {acc_num}")
            self.refresh_account_list()
            dialog.accept()
        else:
            QMessageBox.warning(self, "Error", "Please enter account holder name")

    def show_deposit(self):
        self.show_transaction_dialog("Deposit Money", self.bank.deposit)

    def show_withdraw(self):
        self.show_transaction_dialog("Withdraw Money", self.bank.withdraw)

    def show_transaction_dialog(self, title, transaction_func):
        dialog = TransactionDialog(title, self)
        dialog.submit_btn.clicked.connect(lambda: self.process_transaction(dialog, transaction_func))
        dialog.exec_()

    def process_transaction(self, dialog, transaction_func):
        try:
            acc_num = dialog.acc_input.text().strip()
            amount = float(dialog.amount_input.text())
            result = transaction_func(acc_num, amount)
            
            if "not found" in result.lower():
                QMessageBox.warning(self, "Error", result)
            else:
                QMessageBox.information(self, "Success", result)
                self.refresh_account_list()
                dialog.accept()
        except ValueError:
            QMessageBox.warning(self, "Error", "Please enter a valid amount")

    def show_balance(self):
        dialog = TransactionDialog("Check Balance", self)
        dialog.submit_btn.clicked.connect(lambda: self.check_balance(dialog))
        dialog.exec_()

    def check_balance(self, dialog):
        acc_num = dialog.acc_input.text().strip()
        balance = self.bank.get_balance(acc_num)
        if isinstance(balance, float):
            QMessageBox.information(self, "Balance", f"Current balance: ${balance:.2f}")
            dialog.accept()
        else:
            QMessageBox.warning(self, "Error", balance)

    def show_account_details(self):
        dialog = TransactionDialog("Account Details", self)
        dialog.submit_btn.clicked.connect(lambda: self.display_account_details(dialog))
        dialog.exec_()

    def display_account_details(self, dialog):
        acc_num = dialog.acc_input.text().strip()
        details = self.bank.display_account(acc_num)
        if "not found" in details.lower():
            QMessageBox.warning(self, "Error", details)
        else:
            QMessageBox.information(self, "Account Details", details)
            dialog.accept()

def main():
    print("Starting application...")
    app = QApplication(sys.argv)
    print("QApplication created")
    
    # Set application-wide style
    app.setStyle("Fusion")
    print("Style set to Fusion")
    
    # Set dark theme palette
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(StyleConfig.MAIN_BG))
    palette.setColor(QPalette.WindowText, QColor(StyleConfig.TEXT_COLOR))
    palette.setColor(QPalette.Base, QColor(StyleConfig.MAIN_BG))
    palette.setColor(QPalette.AlternateBase, QColor(StyleConfig.BUTTON_BG))
    palette.setColor(QPalette.ToolTipBase, QColor(StyleConfig.TEXT_COLOR))
    palette.setColor(QPalette.ToolTipText, QColor(StyleConfig.TEXT_COLOR))
    palette.setColor(QPalette.Text, QColor(StyleConfig.TEXT_COLOR))
    palette.setColor(QPalette.Button, QColor(StyleConfig.BUTTON_BG))
    palette.setColor(QPalette.ButtonText, QColor(StyleConfig.TEXT_COLOR))
    palette.setColor(QPalette.Highlight, QColor(StyleConfig.BUTTON_HOVER))
    palette.setColor(QPalette.HighlightedText, QColor(StyleConfig.TEXT_COLOR))
    app.setPalette(palette)
    
    # Create and show the main window
    window = BankAccountGUI()
    print("Main window created")
    window.show()
    print("Show command issued")
    
    print("Entering main event loop...")
    sys.exit(app.exec_())

if __name__ == "__main__":
    print("Script started")
    main() 