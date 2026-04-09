from gestion_hopital.patient import Patient

class GestionPatients:
    def __init__(self):
        self.patients = []

    def ajouter_patient(self, nom, age):
        patient = Patient(nom, age)
        self.patients.append(patient)

    def lister_patients(self):
        return self.patients

    def rechercher_patient(self, nom):
        return [p for p in self.patients if p.nom == nom]