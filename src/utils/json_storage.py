import json
from models.cv import CV 

file_path = "../data/cvs.json"

def load_cv(file_path):
    """
    Loads CV data from a JSON file.
    """
    try:
        with open(file_path, "r", encoding='utf-8') as f:
            cv_list = json.load(f)
            return cv_list
    except FileNotFoundError:
        print(f"❌ Error: File {file_path} not found.")
        return []
    except json.JSONDecodeError:
        print(f'❌ Error: File {file_path} is empty or contains invalid JSON format.')
        return []
    
def save_all(list_cv):
    """
    Saves the list of CVs to the JSON file.
    """
    try:
        with open(file_path, "w", encoding='utf-8') as f:
            json.dump(list_cv, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"🛑 An unexpected error occurred while saving: {e}")



