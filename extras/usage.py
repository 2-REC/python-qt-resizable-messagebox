"""usage.py

    Example usage of the Resizable MessageBox widget.
"""

import sys

from Qt.QtWidgets import (
    QApplication
)

import dialogs


def run(*args):
    if not QApplication.instance():
        app = QApplication(*args)
    else:
        app = QApplication.instance()

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


    dialogs.success(
        None,
        "Success message",
        details=long_text
    )

    dialogs.warning(
        None,
        "Warning message",
        details=long_text
    )

    dialogs.alert(
        None,
        "Alert message",
        details=long_text
    )

    dialogs.question(
        None,
        "Question?",
        details=long_text
    )

    dialogs.questionWarning(
        None,
        "Question as warning?",
        details=long_text
    )

    return 0

if __name__ == "__main__":
    return_code = run(sys.argv)
    sys.exit(return_code)
