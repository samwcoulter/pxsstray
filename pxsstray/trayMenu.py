from importlib.resources import files
from PySide6 import QtGui, QtWidgets


class TrayMenu(QtWidgets.QSystemTrayIcon):
    def __init__(self, app):
        super().__init__()
        iconPath = str(files("pxsstray.images").joinpath("heart.png"))
        icon = QtGui.QIcon(iconPath)

        self.setIcon(icon)
        self.setVisible(True)

        menu = QtWidgets.QMenu()

        action = QtGui.QAction("Menu Action WXST")
        menu.addAction(action)

        quit = QtGui.QAction("Quit")
        quit.triggered.connect(app.quit)
        menu.addAction(quit)

        self.setContextMenu(menu)
