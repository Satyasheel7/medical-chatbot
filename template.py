import os
from pathlib import Path
import logging 

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: [%(message)s]')

list_of_files = [
    "src/_init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "app.py",
    "research/trials.ipynb"
]

# Automatically creates the files needed
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)  # Split into folder and file 

    # Creating a folder if it does not exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)  # Fixed typo here
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    # Creating the file if it does not exist or is empty
    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")
