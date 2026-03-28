from utils.json_storage import save_all, load_cv


file_path = "../data/cvs.json"

def add_cv(cv_obj, email):
    """
    Adds a new CV to the storage after checking for duplicates
    """
    list_cv = load_cv(file_path)
    present = False

    for item in list_cv:
        if item is None or not isinstance(item, dict):
            continue
        if item['email'] == email:
            present = True
            raise ValueError(f"❌ Error: A CV for {cv_obj.nom} already exists."
                            f"\n🛠️ You can update the existing CV instead.")
        
    if not present:
        list_cv.append(cv_obj.to_dict())
        save_all(list_cv)

    return list_cv


def delete_cv(email):
    """
    Removes a CV from the storage using its email address.
    """

    list_cv = load_cv(file_path)

    new_list_cv = [value for value in list_cv if value['email'] != email]

    if len(list_cv) == len(new_list_cv):
        raise ValueError(f"❌ Error: No CV found with email: {email}.")
    
    save_all(new_list_cv)

    return f"✅ Successfully deleted CV from: {email}."

def check_email_exists(item, email):
    """
    Verifies if a specific email matches the current record.
    """
    email_found = False
    
    if item['email'] == email:
        email_found = True
        
    return email_found

def update_cv(new_cv_obj, email):
    """
    Updates an existing CV's information in the JSON file.
    """
    list_cv = load_cv(file_path)

    for k, item in enumerate(list_cv):
        if item is None or not isinstance(item, dict):
            continue
    
        if check_email_exists(item, email):
            list_cv[k] = new_cv_obj.to_dict() 
            break
        
    save_all(list_cv) 
    
    return list_cv

def get_skill_frequencies():
    """
    Calculates the frequency of each skill across all CVs.
    """
    list_cv = load_cv(file_path)
    skills = {}
    
    for item in list_cv:
        for skill in item['competence']:
            if skill not in skills:
                skills[skill] = 0
            skills[skill] += 1

    return skills

def top_skill():
    """
    Identifies the skills with the highest frequency.
    """
    top = float('-inf')
    skills = get_skill_frequencies()
    for skill, val in skills.items():
        if val > top:
            top = val
    top_skill = {item: skil for item, skil in skills.items() if skil == top}

    return top_skill

def filter_by_top_skills():
    """
    Returns a list of CVs that possess the most popular skills.
    """
    list_cv = load_cv(file_path)
    filter_by_top_skill = top_skill()
    new_list = []
    
    if not filter_by_top_skill:
        print(f"Top skills are empty.")
        
    for item in list_cv:
        found_cv = False
        for elt in item['competence']:
            if elt in filter_by_top_skill:
                found_cv = True
                
        if found_cv:
            new_list.append(item)
        
    return new_list

def input_email():
    return input(f"Enter email: ")