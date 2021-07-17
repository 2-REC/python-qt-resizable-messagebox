"""usage_maya.py

    Example usage of the Resizable MessageBox widget.
"""

from Qt.QtWidgets import (
    QApplication
)

import dialogs


def getMayaWindow():
    top_level_widgets = QApplication.topLevelWidgets()
    return next(
        widget for widget in top_level_widgets
            if widget.objectName() == "MayaWindow"
    )


def run():

    long_text = (
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do "
        "eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut "
        "enim ad minim veniam, quis nostrud exercitation ullamco laboris"
        " nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor"
        " in reprehenderit in voluptate velit esse cillum dolore eu "
        "fugiat nulla pariatur. Excepteur sint occaecat cupidatat non "
        "proident, sunt in culpa qui officia deserunt mollit anim id est"
        " laborum. Lorem ipsum dolor sit amet, consectetur adipiscing "
        "elit, sed do eiusmod tempor incididunt ut labore et dolore magna"
        " aliqua. Ut enim ad minim veniam, quis nostrud exercitation "
        "ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis "
        "aute irure dolor in reprehenderit in voluptate velit esse cillum"
        " dolore eu fugiat nulla pariatur. Excepteur sint occaecat "
        "cupidatat non proident, sunt in culpa qui officia deserunt "
        "mollit anim id est laborum."
    )

    parent = getMayaWindow()

    dialogs.success(
        parent,
        "Success message",
        details=long_text
    )

    dialogs.warning(
        parent,
        "Warning message",
        details=long_text
    )

    dialogs.alert(
        parent,
        "Alert message",
        details=long_text
    )

    dialogs.question(
        parent,
        "Question?",
        details=long_text
    )

    dialogs.questionWarning(
        parent,
        "Question as warning?",
        details=long_text
    )


run()