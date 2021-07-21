# Usage examples

## Basic usage

Simple example showing how to create and use a Resizable Message Box.

Required files:
* resizable_messagebox.py
* Qt.py

Make sure the files are in the same directory and that the path is in the Python search paths (defined in "PYTHONPATH" or at least in 'sys.path').


Code snippet:
```python
from resizable_messagebox import ResizableMessageBox
from Qt.QtWidgets import QMessageBox


# Create the Message Box
message_box = ResizableMessageBox(
    QMessageBox.Information,
    "Title",
    "Short message"
)

# Set the long message (details)
message_box.setDetailedText("This can be long text...")

message_box.exec_()
```


## Usage in a Python application.

Example showing how to use the Resizable Message Box in a Python application.
It shows how to use different Message Box types.

The example uses additional files from the 'extras' directory.

Required files:
* resizable_messagebox.py
* dialogs.py
* usage.py
* Qt.py

Make sure the files are in the same directory and that the path is in the Python search paths (defined in "PYTHONPATH" or at least in 'sys.path').


If running the code from a terminal, simply execute the Python script:
```
python -m usage
```
or:
```
python usage.py
```

If running the code in a Python interpreter, import the file and execute the 'run' function:
```python
import usage
usage.run()
```


## Usage in Maya.

Example showing how to use a Resizable Message Box in a Maya session.
It shows how to use different Message Box types.

The example uses additional files from the 'extras' directory.

Required files:
* resizable_messagebox.py
* dialogs.py
* usage_maya.py
* Qt.py

Make sure the files are in the same directory and that the path is in the Python search paths (defined in "PYTHONPATH" or at least in 'sys.path').

Simply import the example file:
```python
import usage_maya
```
