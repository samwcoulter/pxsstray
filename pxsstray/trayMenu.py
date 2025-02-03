from importlib.resources import files
from PySide6 import QtGui, QtWidgets


class TrayMenu(QtWidgets.QSystemTrayIcon):
    def __init__(self, app):
        super().__init__()
        iconPath = str(files("pxsstray.images").joinpath("heart.png"))
        self.icon = QtGui.QIcon(iconPath)
        self.setIcon(self.icon)
        self.setVisible(True)

        self.menu = QtWidgets.QMenu()

        self.action = QtGui.QAction("Menu Action WXST")
        self.menu.addAction(self.action)

        self.quit = QtGui.QAction("Quit")
        self.quit.triggered.connect(app.quit)
        self.menu.addAction(self.quit)

        self.setContextMenu(self.menu)
