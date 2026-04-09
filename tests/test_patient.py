from gestion_hopital.patient import Patient

def test_patient_creation():
    p = Patient("Alice", 25)
    assert p.nom == "Alice"
    assert p.age == 25