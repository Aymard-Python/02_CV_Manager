## Structure des données d'un CV
import re
import time 
import uuid

class CV():
    """
    Classe qui permet de générer le modèle d'un CV 
    """
    def __init__(self, nom, adresse, email, telephone, experience, competence, education, langue, loisir):
        self.id = str(uuid.uuid4())
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

        # Valider les données
        profil = ["nom", "email", "telephone"]
        for key in profil:
            if not isinstance(key, str):
                raise ValueError(f"Erreur: champ {key} invalide")
                
        value = [self.nom, self.email, self.telephone]
        for val in value:
            if not isinstance(val, str):
                raise ValueError(f"La valeur de nom ou email ou telephone est invalide.")
            if not val.strip():
                raise ValueError(f"La clé nom ou email ou telephone est vide.")

        listes = [self.competence, self.langue]
        if not all(isinstance(liste, list) for liste in listes):
            raise ValueError(f"Erreur: {self.competence} ou {self.langue} etc. est invalide.")
        for item in listes:
            if not item:
                raise ValueError("Liste vide interdite.")
            for value in item:
                if not isinstance(value, str) or not value.strip():
                    raise ValueError(f"Erreur: champ et invalide (valeur: {value})")
        
        if not isinstance(self.loisir, list):
            raise ValueError(f"Erreur: {self.loisir} est invalide.")
        if self.loisir:
            for value in self.loisir:
                if not isinstance(value, str) or not value.strip():
                    raise ValueError("Loisir invalide.")
                
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
        cleaned = []
        
        for item in list_dict:
            new_item = {}
            
            for key, value in item.items():
                if isinstance(value, list):
                    new_item[key] = self._clean_liste(value)
                else:
                    if not isinstance(value, str):
                        raise ValueError(f"Erreur: la date: {value} doit être une chaine de caractère.")
                    else:
                        new_item[key] = value.strip()
                        
            cleaned.append(new_item)
        
        return cleaned

    def _clean_dict(self, dict_ad):
        """
        Méthode qui permet de nettoyer un dictionnaire 
        """
        cleaned = {}
        
        for key, value in dict_ad.items():
            if not isinstance(value, str):
                raise ValueError(f"Erreur: champ '{key}' invalide (valeur: {value})")
            else:
                cleaned[key] = value.strip()
        return cleaned
        
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
        if not self.adresse['rue'] or not self.adresse['ville']:
            raise ValueError(f"Erreur: clé ville ou clé rue n'a pas de valeur.")
            
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
            
            if 'date_debut' not in item or 'date_fin' not in item:
                raise ValueError("Dates manquantes dans expérience.")
                
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
            
        experiences = {'poste', 'entreprise', 'date_debut', 'date_fin', 'points_cles'}
        
        for exper in self.experience:
            if not isinstance(exper, dict):
                raise ValueError(f"Erreur: {exper} est invalide.")
            if not exper:
                raise ValueError(f"Erreur: Expérience vide.")
                
            for key, value in exper.items():
                # Vérifier si le nombre de clés attendues dans expériences est exacte.
                self._validate_keys(exper, experiences, key)
                
                if key == 'points_cles':    
                    if not isinstance(value, list):
                        raise ValueError(f"Erreur: {key} doit être une liste.")
                    for val in value:
                        if not isinstance(val, str) or not val.strip():
                            raise ValueError("Point clé invalide.")
                else:
                    if not isinstance(value, str) or not value.strip():
                        raise ValueError(f"Erreur: champ '{key}' invalide (valeur: {value})")
                        
                             
    def _validate_studie(self):
        """
        Méthode qui permet de valider les champs de la formation 
        """
        if not isinstance(self.education, list):
             raise ValueError(f"Erreur: {self.education} est invalide.")
        if not self.education:
            raise ValueError(f"Erreur: {self.education} est vide.")
            
        studies = {'diplome', 'institution', 'annee'}
        for stud in self.education:
            if not isinstance(stud, dict):
                raise ValueError(f"Erreur: {stud} est invalide.")
            if not stud:
                raise ValueError(f"Erreur: {stud} est vide.")
            for key, value in stud.items():
                # Vérifier si le nombre de clés attendues dans formation est exacte.
                self._validate_keys(stud, studies, key)
                if not isinstance(value, str):
                    raise ValueError(f"Erreur: champ '{key}' invalide (valeur: {value})")
                if not value.strip():
                    raise ValueError(f"Erreur: {key} est vide.")
                    
               
                
    def _validate_keys(self, data, expected_key, name):
        if set(data.keys()) != expected_key:
            raise ValueError(f"{name} invalide: {data}")
            
    def to_dict(self):
        """
        Méthode qui permet de créer un CV en format Json. 
        """
        return {
                'id': self.id,
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