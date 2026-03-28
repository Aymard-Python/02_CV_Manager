## Structure des données d'un CV
import re
import time 
import uuid

class CV():
    """
    Represents the data structure and validation for a CV. 
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
        self.validate() # call method public validate does not create invalid object CV.
    
    def validate(self):
        """
        Main method to validate and clean all CV data.
        """
        # Cleaning all datas
        self.nom = self.nom.strip()
        self.adresse = self._clean_dict(self.adresse)
        self.email = self.email.strip().lower()
        self.telephone = self.telephone.strip()
        self.competence = self._clean_liste(self.competence)
        self.langue = self._clean_liste(self.langue)
        self.loisir = self._clean_liste(self.loisir)
        self.experience = self._clean_listes_dict(self.experience)
        self.education = self._clean_listes_dict(self.education)

        profil = ["nom", "email", "telephone"]
        for key in profil:
            if not isinstance(key, str):
                raise ValueError(f"❌ Error: Invalid {key}")
                
        value = [self.nom, self.email, self.telephone]
        for val in value:
            if not isinstance(val, str):
                raise ValueError(f"🔘 Invalid name or email or phone.")
            if not val.strip():
                raise ValueError(f"🔘 Name, email, and phone fields are required and cannot be empty.")

        listes = [self.competence, self.langue]
        if not all(isinstance(liste, list) for liste in listes):
            raise ValueError(f"❌ Erreur: Invalid {self.competence} or {self.langue} etc.")
        for item in listes:
            if not item:
                raise ValueError("List is empty.")
            for value in item:
                if not isinstance(value, str) or not value.strip():
                    raise ValueError(f"❌ Error: Invalid (value: {value})")
        
        if not isinstance(self.loisir, list):
            raise ValueError(f"❌ Error: Invalid {self.loisir}.")
        if self.loisir:
            for value in self.loisir:
                if not isinstance(value, str) or not value.strip():
                    return value
                
        # Calling all private methods
        self._validate_email()
        self._validate_phone()
        self._validate_address()
        self._validate_experience()
        self._validate_studie()
        self._validate_date()

    def _clean_liste(self, liste):
        """
        Trims whitespace from each element in a list.
        """
        return [val.strip() for val in liste]

    def _clean_listes_dict(self, list_dict):
        """
        Method cleaning list dictionary
        """
        cleaned = []
        
        for item in list_dict:
            new_item = {}
            if not isinstance(list_dict, dict):
                return list_dict
            
            for key, value in item.items():
                if isinstance(value, list):
                    new_item[key] = self._clean_liste(value)
                else:
                    if not isinstance(value, str):
                        raise ValueError(f"❌ Error: date: {value} must be string.")
                    else:
                        new_item[key] = value.strip()
                        
            cleaned.append(new_item)
        
        return cleaned

    def _clean_dict(self, dict_ad):
        """
        Method cleaning the dictionary
        """
        cleaned = {}

        if not isinstance(dict_ad, dict):
            return dict_ad
        
        for key, value in dict_ad.items():
            if not isinstance(value, str):
                raise ValueError(f"❌ Error: Invalid champ '{key}' or (value: {value})")
            else:
                cleaned[key] = value.strip()
        return cleaned
        
    def _validate_email(self):
        """
        Validates the email format using regex. 
        """
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if not re.match(pattern, self.email):
            raise ValueError(f"❌ Error: Invalid {self.email} !")
            
    def _validate_phone(self):
        """
        Method validates format phone number 
        """
        pattern = r"^\+?\d{1,4}?[-.\s]?\(?\d{1,3}?\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}$"
        if not re.match(pattern, self.telephone):
            raise ValueError(f"❌ Error: Invalid {self.telephone}.")
            
    def _validate_address(self):
        """
        Method validates the champ adress  
        """
        if not isinstance(self.adresse, dict):
            raise ValueError(f"❌ Error: Invalid adress.")
        if not self.adresse:
            raise ValueError(f"❌ Error: Adress is empty.")
        if 'rue' not in self.adresse or 'ville' not in self.adresse:
            raise ValueError("❌ Error: Address must contain both 'rue' (street) and 'ville' (city).")
        if not isinstance(self.adresse['rue'], str) or not isinstance(self.adresse['ville'], str):
            raise ValueError(f"❌ Error: Key city or key street contains invalid value.")
        if not self.adresse['rue'] or not self.adresse['ville']:
            raise ValueError(f"❌ Error: key city or key street is empty.")
            
        for _, value in self.adresse.items():
            if not isinstance(value, str):
                raise ValueError(f"❌ Error: {self.adresse} contains Invalid {value}.")
            if not value.strip():
                raise ValueError(f"❌ Error: {value} is empty.")

    def _validate_date(self):
        """
        Ensures dates are in YYYY-MM format and logically ordered.
        """
        for item in self.experience:
            
            if 'date_debut' not in item or 'date_fin' not in item:
                raise ValueError("🔘 Dates does not exits.")
                
            date_str_debut = item['date_debut']
            date_str_fin = item['date_fin']

            try:
                date_debut = time.strptime(date_str_debut, "%Y-%m")
                date_fin = time.strptime(date_str_fin, "%Y-%m")
            except ValueError:
                raise ValueError(
                    f"❌ Error: Invalid date format." 
                    f"Start : {date_str_debut}, End: {date_str_fin} expected format: %Y-%m."
                )

            if date_debut > date_fin:
                raise ValueError(f"❌ Error: Start date : {date_str_debut} cannot be after end date: {date_str_fin}")

        for item in self.education:
            year_str = item['annee']

            try:
                year = time.strptime(year_str, "%Y")
            except ValueError:
                raise ValueError(f"❌ Error: Format year is bad {year_str} expected format: %Y")
                
    def _validate_experience(self):
        """
        Method validates the champ experience from the CVs in Json file
        """
        if not isinstance(self.experience, list):
             raise ValueError(f"❌ Error: Invalid {self.experience}.")
        if not self.experience:
            raise ValueError(f"❌ Error: {self.experience} is empty.")
            
        experiences = {'poste', 'entreprise', 'date_debut', 'date_fin', 'points_cles'}
        
        for exper in self.experience:
            if not isinstance(exper, dict):
                raise ValueError(f"❌ Error: Invalid {exper}.")
            if not exper:
                raise ValueError(f"❌ Error: Experience is empty.")
                
            for key, value in exper.items():
                self._validate_keys(exper, experiences, key)
                
                if key == 'points_cles':    
                    if not isinstance(value, list):
                        raise ValueError(f"❌ Error: {key} must be a list.")
                    for val in value:
                        if not isinstance(val, str) or not val.strip():
                            raise ValueError("❌ Error Invalid Point clé.")
                else:
                    if not isinstance(value, str) or not value.strip():
                        raise ValueError(f"❌ Error: Invalid champ '{key}' or  (value: {value})")
                        
                             
    def _validate_studie(self):
        """
        Method valiadtes type, data to specifies key 
        """
        if not isinstance(self.education, list):
             raise ValueError(f"❌ Error: Invalid {self.education}.")
        if not self.education:
            raise ValueError(f"❌ Error: {self.education} is empty.")
            
        studies = {'diplome', 'institution', 'annee'}
        for stud in self.education:
            if not isinstance(stud, dict):
                raise ValueError(f"❌ Error: Invalid {stud}.")
            if not stud:
                raise ValueError(f"❌ Error: {stud} is emplty.")
            for key, value in stud.items():
                self._validate_keys(stud, studies, key)
                if not isinstance(value, str):
                    raise ValueError(f"❌ Error: Invalid '{key}' or (value: {value})")
                if not value.strip():
                    raise ValueError(f"❌ Error: {key} is empty.")
                    
               
                
    def _validate_keys(self, data, expected_key, name):
        """
        Checks if the dictionary keys match the expected schema.
        """
        if set(data.keys()) != expected_key:
            raise ValueError(f"🔘 Invalid schema for {name}. Data: {data}")
            
    def to_dict(self):
        """
        Converts the CV object into a dictionary for JSON storage.
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