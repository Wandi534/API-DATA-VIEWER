# API-DATA-VIEWER

A small desktop/web app built with [Flet](https://flet.dev/). Enter the URL of a JSON API and the app displays the `name` value from each item in its response.

## Requirements

- Python 3.10 or later
- An internet connection to install packages and access the JSON endpoint

## Setup

From the project directory:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install "flet[all]>=1.1.3" requests
```

If PowerShell prevents activating the virtual environment, you can skip activation and use `.venv\Scripts\python.exe` in place of `python` in the commands below.

## Run

From the project directory:

```powershell
python .\src\main.py
```

To run it in a browser instead:

```powershell
flet run --web .\src\main.py
```

## Expected API response

The app expects the URL to return a JSON array of objects, each containing a `name` field. For example:

```json
[
  { "name": "Ada" },
  { "name": "Grace" }
]
```

Paste the API URL into the input field and select **Scrape**. The app makes a GET request and displays the names, one per line.

## Current limitations

- It reads JSON API responses; it does not extract data from ordinary HTML pages.
- Each response item must have a `name` field.
- Authentication, pagination, and request-error handling are not implemented yet.

## Project structure

```text
src/
  main.py     # Flet UI and request logic
tests/
  test_main.py
```
