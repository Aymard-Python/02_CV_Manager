## Structure des données d'un CV
import re
import time 

class CV():
    """
    Classe qui permet de générer le modèle d'un CV 
    """
    def __init__(self, nom, adresse, email, telephone, experience, competence, education, langue, loisir):
        self.nom = nom
        self.adresse = adresse
        self.email = email
        self.telephone = telephone
        self.experience = experience
        self.competence = competence
        self.education = education
        self.langue = langue
        self.loisir = loisir
        self.validate() # garanti qu'aucun objet "invalide" ne soit jamais créé
    
    def validate(self):
        """
        Méthode qui permet de valider la structure, le type et le contenu 
        """
        identity = [self.nom, self.email, self.telephone]
        if not all(isinstance(ident, str) for ident in identity):
            raise ValueError(f"Erreur: {self.nom} ou {self.email} ou {self.telephone} est invalide.")
        if not self.email.strip() or not self.nom.strip() or not self.telephone.strip():
            raise ValueError(f" Erreur: {self.nom} ou {self.email} ou {self.telephone} est vide.")

        listes = [self.competence, self.langue]
        if not all(isinstance(liste, list) for liste in listes):
            raise ValueError(f"Erreur: {self.competence} ou {self.langue} etc. est invalide.")
        for item in listes:
            if not item:
                raise ValueError(f"Erreur: {item} est vide.")
            else:
                for value in item:
                    if not isinstance(value, str):
                        raise ValueError(f"Erreur: {self.competence} ou {self.langue} contient une valeur {value} invalide.")
        
        if not isinstance(self.loisir, list):
            raise ValueError(f"Erreur: {self.loisir} est invalide.")
        if self.loisir:
            if not all(isinstance(value, str) for value in self.loisir):
                raise ValueError(f"Erreur: {self.loisir} contient une valeur invalide.")

         # Nettoyer les valeurs:
        self.nom = self.nom.strip()
        self.adresse = self._clean_dict(self.adresse)
        self.email = self.email.strip().lower()
        self.telephone = self.telephone.strip()
        self.competence = self._clean_liste(self.competence)
        self.langue = self._clean_liste(self.langue)
        self.loisir = self._clean_liste(self.loisir)
        self.experience = self._clean_listes_dict(self.experience)
        self.education = self._clean_listes_dict(self.education)
        
        self._validate_email()
        self._validate_phone()
        self._validate_address()
        self._validate_experience()
        self._validate_studie()
        self._validate_date()

    def _clean_liste(self, liste):
        """
        Méthode qui permet de nettoyer une liste 
        """
        return [val.strip() for val in liste]

    def _clean_listes_dict(self, list_dict):
        """
        Méthode qui permet de nettoyer une liste de dictionnaires 
        """
        for item in list_dict:
            for key, value in item.items():
                if isinstance(value, list):
                    item[key] = self._clean_liste(value)
                else:
                    item[key] = value.strip()
        return list_dict

    def _clean_dict(self, dict_ad):
        """
        Méthode qui permet de nettoyer un dictionnaire 
        """
        for key, value in dict_ad.items():
            if not isinstance(value, str):
                dict_ad[key] = self._clean_liste(value)
            else:
                dict_ad[key] = value.strip()
        return dict_ad
        
        # Valider l' email
    def _validate_email(self):
        """
        Méthode qui permet de valider une adresse email 
        """
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if not re.match(pattern, self.email):
            raise ValueError(f"Erreur: {self.email} est invalide!")
            
       # Valider le numéro de téléphone
    def _validate_phone(self):
        """
        Méthode qui permet de valider un numéro de téléphone
        """
        pattern = r"^\+?\d{1,4}?[-.\s]?\(?\d{1,3}?\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}$"
        if not re.match(pattern, self.telephone):
            raise ValueError(f"Erreur: {self.telephone} est invalide.")
            
    def _validate_address(self):
        """
        Méthode qui permet de valider une adresse 
        """
        if not isinstance(self.adresse, dict):
            raise ValueError(f"Erreur: {self.adresse} est invalide.")
        if not self.adresse:
            raise ValueError(f"Erreur: {self.adresse} est vide.")
        if 'rue' not in self.adresse or 'ville' not in self.adresse:
            raise ValueError("Erreur: clé rue ou clé ville manquante.")
        if not isinstance(self.adresse['rue'], str) or not isinstance(self.adresse['ville'], str):
            raise ValueError(f"Erreur: la clé rue ou la clé ville contient une valeur invalide.")

        # Cette boucle prend en compte d'autres valeurs optionnelles de l'adresse
        for _, value in self.adresse.items():
            if not isinstance(value, str):
                raise ValueError(f"Erreur: {self.adresse} contient une valeur {value} invalide.")
            if not value.strip():
                raise ValueError(f"Erreur: {value} est vide.")

    def _validate_date(self):
        """
        Méthode qui permet de valider le format des dates 
        """
        for item in self.experience:
            date_str_debut = item['date_debut']
            date_str_fin = item['date_fin']

            try:
                date_debut = time.strptime(date_str_debut, "%Y-%m")
                date_fin = time.strptime(date_str_fin, "%Y-%m")
            except ValueError:
                raise ValueError(
                    f"Erreur: mauvais formate date" 
                    f"debut: {date_str_debut}, fin: {date_str_fin} format attendu %Y-%m."
                )

            if date_debut > date_fin:
                raise ValueError(f"Erreur: {date_str_debut} ne doit pas être supérieur à {date_str_fin}")

        for item in self.education:
            year_str = item['annee']

            try:
                year = time.strptime(year_str, "%Y")
            except ValueError:
                raise ValueError(f"Erreur: mauvais format année {year_str} format attendu %Y")
                
    def _validate_experience(self):
        """
        Méthode qui permet de valider les champs de expérience 
        """
        if not isinstance(self.experience, list):
             raise ValueError(f"Erreur: {self.experience} est invalide.")
        if not self.experience:
            raise ValueError(f"Erreur: {self.experience} est vide.")
            
        experiences = ['poste', 'entreprise', 'date_debut', 'date_fin', 'points_cles']
        
        for exper in self.experience:
            if not isinstance(exper, dict):
                raise ValueError(f"Erreur: {exper} est invalide.")
            if not exper:
                raise ValueError(f"Erreur: Expérience vide.")
            
        # Vérifier si le nombre de clés attendues dans expériences est exacte.
        experience = set(experiences)
        for exper in self.experience:
            if set(exper.keys()) != experience:
                raise ValueError(f"Erreur: {self.experience} contient un nombre en trop de clés.")
            
            for key, value in exper.items():
                if key != 'points_cles':
                    if not isinstance(value, str):
                        raise ValueError(f"Erreur: {key} contient une valeur {value} invalide.")
                    if not value.strip():
                        raise ValueError(f"Erreur: {key} est vide.")
                else:
                    if not isinstance(value, list):
                        raise ValueError(f"Erreur: {key} doit être une liste.")
                    if not value:
                        raise ValueError(f"Erreur: la clé points_cles est vide.")
                    if not all(isinstance(point, str) for point in value):
                        raise ValueError(f"Erreur: {key} contient des ou une valeur invalide.")
                             
    def _validate_studie(self):
        """
        Méthode qui permet de valider les champs de la formation 
        """
        if not isinstance(self.education, list):
             raise ValueError(f"Erreur: {self.education} est invalide.")
        if not self.education:
            raise ValueError(f"Erreur: {self.education} est vide.")
            
        studies = ['diplome', 'institution', 'annee']
        for stud in self.education:
            if not isinstance(stud, dict):
                raise ValueError(f"Erreur: {stud} est invalide.")
            if not stud:
                raise ValueError(f"Erreur: {stud} est vide.")
            if not isinstance(stud['diplome'], str) or not isinstance(stud['institution'], str) or not isinstance(stud['annee'], str):
                raise ValueError("Erreur: la clé diplome, institution ou annee est invalide.")
            if not stud['diplome'].strip() or not stud['institution'].strip() or not stud['annee'].strip():
                raise ValueError("Erreur: la clé diplome ou institution ou annee est vide.")
                
        # Vérifier si le nombre de clés attendues dans formation est exacte.
        studies = set(studies)
        for stud in self.education:
            if set(stud.keys()) != studies:
                raise ValueError(f"Erreur: {self.education} contient un nombre en trop de clés.")
            
    def to_dict(self):
        """
        Méthode qui permet de créer un CV en format Json. 
        """
        return {
                'nom': self.nom,
                'adresse': self.adresse,
                'email': self.email,
                'telephone': self.telephone,
                'experience': self.experience,
                'competence': self.competence,
                'education': self.education,
                'langue': self.langue,
                'loisir': self.loisir
            }