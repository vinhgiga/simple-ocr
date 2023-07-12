# The project at university: Image processing

## About this project

The Simple OCR is a desktop application that uses the PyQt5, OpenCV, and pytesseract libraries. Its main functions include:

- Image preprocessing options to improve text recognition results.
- Displaying and saving the recognized text to the Clipboard or a file.

## Demo

![Demo](/demo/demo.gif)

## Installation

### Requirements

- Windows 10 or higher
- Python 3.9

### Installation on Windows

Clone this repository:

```powershell
$ git clone https://github.com/vinhgiga/simple-ocr.git
```

Change working directory to `simple-ocr`:

```powershell
$ cd simple-ocr
```

(Optional) Create and activate a Python virtual environment:

```powershell
$ python -m venv .venv
$ .venv\Scripts\activate
```

Install Python modules:

```powershell
$ pip install -r requirements.txt
```

Run app:

```powershell
$ python main.py
```
