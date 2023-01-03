import sys
from qtpy import QtWidgets


class TodoApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # create list widget
        self.list_widget = QtWidgets.QListWidget()

        # create input and add button
        self.input_field = QtWidgets.QLineEdit()
        self.add_button = QtWidgets.QPushButton('Add')
        self.done_button = QtWidgets.QPushButton('Done')
        self.edit_button = QtWidgets.QPushButton('Edit')
        self.delete_button = QtWidgets.QPushButton('Delete')

        # create layout
        self.layout = QtWidgets.QGridLayout()
        self.layout.addWidget(self.list_widget, 0, 0, 1, 4)
        self.layout.addWidget(self.input_field, 1, 0, 1, 4)
        self.layout.addWidget(self.add_button, 2, 0)
        self.layout.addWidget(self.done_button, 2, 1)
        self.layout.addWidget(self.delete_button, 2, 3)
        self.setLayout(self.layout)

        # create signals and slots
        self.add_button.clicked.connect(self.add_todo)
        self.done_button.clicked.connect(self.mark_done)
        self.delete_button.clicked.connect(self.delete_todo)

    def add_todo(self):
        # get text from input field
        text = self.input_field.text()
        # check if text is empty or a space
        if text.strip():
            # add text to list widget
            self.list_widget.addItem(text)
            # clear input field
            self.input_field.setText('')

    def mark_done(self):
        # get the selected item
        item = self.list_widget.currentItem()
        # strike-through the text
        font = item.font()
        font.setStrikeOut(True)
        item.setFont(font)

    def delete_todo(self):
        # get the selected item
        item = self.list_widget.currentItem()
        if item is not None:
            # get the index of the item
            index = self.list_widget.row(item)
            # remove the item from the list widget
            self.list_widget.takeItem(index)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    todo_app = TodoApp()
    todo_app.show()
    sys.exit(app.exec_())
