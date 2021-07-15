"""ResizableMessageBox
"""

__version__ = "1.0"
__author__ = "2-REC"


import logging
logger = logging.getLogger(__name__)


from Qt.QtCore import Qt as qt

from Qt.QtWidgets import (
    QMessageBox,
    QTextEdit,
    QDialogButtonBox,
    QSizePolicy
)


class ResizableMessageBox(QMessageBox):

    _max_width = 4096
    _max_height = 2048

    def __init__(self, *args, **kwargs):            
        super(ResizableMessageBox, self).__init__(*args, **kwargs)

        self.clearDetailBox()


    def setDetailedText(self, text):
        super(ResizableMessageBox, self).setDetailedText(text)

        if not text:
            self.clearDetailBox()
            return

        details_box = self.findChild(QTextEdit)
        if not details_box:
            logger.error("No 'QTextEdit' found in 'QDialogButtonBox'")
            return

        self.details_box = details_box

        dialog_button_box = self.findChild(QDialogButtonBox)
        if dialog_button_box:
            for button in dialog_button_box.buttons():
                if (
                    dialog_button_box.buttonRole(button)
                    == QDialogButtonBox.ButtonRole.ActionRole
                ):
                    button.released.connect(self.detailsToggle)
                    break
            else:
                logger.error("No 'ActionRole' button in 'QDialogButtonBox'")


    def resizeEvent(self, event):
        result = super(ResizableMessageBox, self).resizeEvent(event)

        if self.details_visible:
            self.setSizing()

        return result


    def clearDetailBox(self):
        self.details_box = None
        self.details_visible = False
        self.setSizeGripEnabled(False)


    def detailsToggle(self):
        self.details_visible = not self.details_visible
        self.setSizeGripEnabled(self.details_visible)

        if self.details_visible:
            self.setSizing()


    def setSizing(self):
        self.setWidgetSizing(self)
        self.setWidgetSizing(self.details_box)


    @classmethod
    def setWidgetSizing(cls, widget):
        widget.setMaximumHeight(cls._max_width)
        widget.setMaximumWidth(cls._max_height)
        widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
