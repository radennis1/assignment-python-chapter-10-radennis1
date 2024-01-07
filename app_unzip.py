from zipfile import ZipFile
from pathlib import Path

# Ryan Dennis

# Create a path to worldbank_zipfiles
source_path = Path(".\worldbank_zipfiles")

# Create list of zip files
path_of_zipfiles = [p for p in source_path.rglob("*.zip")]

# Define target directory
target_directory = "worldbank_data"

# For loop to unnzip files to worldbank_data directory
for file in path_of_zipfiles:
    with ZipFile(file) as zip:
        zip.extractall(target_directory)
