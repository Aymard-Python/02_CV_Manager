from utils.json_storage import save_cv, load_cv
from models.cv import CV 


def main():

    try:
        cv_obj = CV(
            'BEKALE Armelle Josiane', 
            {
                "rue": 'Yassa', 
                "ville": 'Douala'
                }, 
            "bekalearmel@yahoo.com", 
            '691-14-53-14', 
            [
                {
                    'poste': 'RH', 
                    'entreprise': 'Orbite Plus', 
                    'date_debut': "2021-10", 
                    'date_fin': '2026-01', 
                    'points_cles': [
                                    "Gestion des relations humaines", 
                                    "Gestion calendrier du personnel",
                                    "Management des évènements"
                                ]
                            }
                ], 
            [
                "Gestion des planning de meeting",
                "Gestion des relations sociales"
                ], 
            [
                {
                    'diplome': "Master en RH", 
                    'institution': "ENAM", 
                    'annee': '2016'
                    }
                ], 
            [
                "FR",
                "EN"
                ], 
            [
               
                ]
)
    except Exception as e:
        print(f"Erreur: {e}")
    save_cv(cv_obj)

    print("CV sauvegardé avec succès !")


if __name__ == "__main__":
    main()