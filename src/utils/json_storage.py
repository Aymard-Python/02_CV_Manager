import json
from models.cv import CV

cv_obj = CV(
    'NDONGO Aymard Regamey', 
    {
        "rue": 'Mendong', 
        "ville": 'Yaoundé'
        }, 
    "aymard@gmail.com", 
    '691-37-38-64', 
    [
        {
            'poste': 'Web', 
            'entreprise': 'PMUC', 
            'date_debut': "2022-10", 
            'date_fin': '2026-01', 
            'points_cles': [
                            "Python", 
                            "Js"
                        ]
                    }
        ], 
    [
        "Python",
        "JavaScript"
        ], 
    [
        {
            'diplome': "Master", 
            'institution': "SUp'PTIC", 
            'annee': '2017'
             }
        ], 
    [
        "FR",
        "EN"
        ], 
    [
        "Sport"
        ]
)

data = "../data/cvs.json"

def load_cv(data):
    try:
        with open(data, "r", encoding='utf-8') as f:
            cv_list = json.load(f)
            return cv_list
    except FileNotFoundError:
        print(f"Erreur: le fichier {data} n'existe pas.")
        return []
    except json.JSONDecodeError:
        print(f'Erreur: le fichier {data} est vide ou mal formaté.')
        return []
    
def save_cv(cv_obj):
    cv = load_cv(data)
    cv.append(cv_obj.to_dict())

    with open(data, "w", encoding='utf-8') as f:
        json.dump(cv, f, indent=4, ensure_ascii=False)


