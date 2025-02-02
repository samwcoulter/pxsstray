# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause
from __future__ import annotations
import sys
from importlib.resources import files
from PySide6 import QtGui, QtWidgets as QW

from . import xset


def query():
    text = xset.xset_q()
    return text


def run():
    app = QW.QApplication()

    if not QW.QSystemTrayIcon.isSystemTrayAvailable():
        QW.QMessageBox.critical(
            None, "Systray", "I couldn't detect any system tray on this system."
        )
        sys.exit(1)

    QW.QApplication.setQuitOnLastWindowClosed(False)

    iconPath = str(files("pxsstray.images").joinpath("heart.png"))
    icon = QtGui.QIcon(iconPath)

    tray = QW.QSystemTrayIcon()
    tray.setIcon(icon)
    tray.setVisible(True)

    menu = QW.QMenu()

    label = menu.addSection(xset.xset_q())

    action = QtGui.QAction("Menu Action WXST")
    menu.addAction(action)

    quit = QtGui.QAction("Quit")
    quit.triggered.connect(app.quit)
    menu.addAction(quit)

    tray.setContextMenu(menu)

    sys.exit(app.exec())
