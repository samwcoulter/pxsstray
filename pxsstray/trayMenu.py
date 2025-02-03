from importlib.resources import files
from PySide6 import QtCore, QtGui, QtWidgets
from pxsstray import xset


class TrayMenu(QtWidgets.QSystemTrayIcon):
    def __init__(self, app):
        super().__init__()
        iconPath = str(files("pxsstray.images").joinpath("heart.png"))
        self.icon = QtGui.QIcon(iconPath)
        self.setIcon(self.icon)
        self.setVisible(True)

        self.menu = QtWidgets.QMenu()

        self.toggleDPMS = QtGui.QAction("Enable DPMS")
        self.toggleDPMS.setCheckable(True)
        self.toggleDPMS.setChecked(True)
        self.toggleDPMS.toggled.connect(self.enableDPMS)
        self.menu.addAction(self.toggleDPMS)

        self.toggleS = QtGui.QAction("Enable S")
        self.toggleS.setCheckable(True)
        self.toggleS.setChecked(True)
        self.toggleS.toggled.connect(self.enableS)
        self.menu.addAction(self.toggleS)

        self.quit = QtGui.QAction("Quit")
        self.quit.triggered.connect(app.quit)
        self.menu.addAction(self.quit)

        self.setContextMenu(self.menu)

    @QtCore.Slot()
    def enableDPMS(self, enabled):
        xset.xset_dpms(enabled)

    @QtCore.Slot()
    def enableS(self, enabled):
        xset.xset_s(enabled)
