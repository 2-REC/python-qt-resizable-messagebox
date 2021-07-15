"""dialogs.py

Example usage of 'ResizableMessageBox' class.
"""

from Qt.QtWidgets import QMessageBox

from resizable_messagebox import ResizableMessageBox


def _messagebox(parent, icon, message, title, details=None):
    message_box = ResizableMessageBox(
        icon,
        title,
        message,
        parent=parent
    )
    message_box.setDefaultButton(QMessageBox.Ok)

    if details:
        message_box.setDetailedText(details)

    message_box.exec_()


def success(parent, message, title=u"Success", details=None):
    """Information single button dialog."""
    _messagebox(parent, QMessageBox.Information, message, title, details)


def warning(parent, message, title=u"WARNING", details=None):
    """Warning single button dialog."""
    _messagebox(parent, QMessageBox.Warning, message, title, details)


def alert(parent, message, title=u"ERROR", details=None):
    """Error single button dialog."""
    _messagebox(parent, QMessageBox.Critical, message, title, details)



def question(parent, message, title=u"Question", details=None, warning=False):
    """Yes/No question dialog."""
    message_box = ResizableMessageBox(
        QMessageBox.Warning if warning else QMessageBox.Question,
        title,
        message
    )
    message_box.addButton(QMessageBox.Yes)
    message_box.addButton(QMessageBox.No)
    message_box.setDefaultButton(QMessageBox.No)

    if details:
        message_box.setDetailedText(details)

    result = message_box.exec_()
    return result == QMessageBox.Yes


def questionWarning(parent, message, title=u"WARNING", details=None):
    """Yes/No question dialog, with warning."""
    return question(parent, message, title, details, warning=True)
