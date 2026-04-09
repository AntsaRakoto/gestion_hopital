from gestion_hopital.service import GestionPatients

def test_ajout_patient():
    service = GestionPatients()
    service.ajouter_patient("Alice", 25)

    assert len(service.patients) == 1

def test_recherche_patient():
    service = GestionPatients()
    service.ajouter_patient("Alice", 25)

    result = service.rechercher_patient("Alice")
    assert len(result) == 1