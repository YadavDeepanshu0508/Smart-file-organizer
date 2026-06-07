import os
import shutil

CATEGORIES = {
    ".pdf": "Documents",
    ".docx": "Documents",
    ".jpg": "Images",
    ".png": "Images",
    ".mp4": "Videos",
    ".zip": "Archives",
    ".py": "Code",
    ".java": "Code",
    ".c": "Code"
}

def organize_files(files):

    for file in files:

        ext = os.path.splitext(file)[1].lower()

        if ext in CATEGORIES:

            folder = CATEGORIES[ext]

            os.makedirs(folder, exist_ok=True)

            try:
                shutil.copy(file, folder)
            except:
                pass