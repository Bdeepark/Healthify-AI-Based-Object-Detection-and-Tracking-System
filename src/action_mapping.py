ACTION_MAP = {

    #Patient Actions
    "A001": {"name": "drink water", "category": "Patient"},
    "A002": {"name": "eat meal", "category": "Patient"},
    "A003": {"name": "brush teeth", "category": "Patient"},
    "A008": {"name": "sit down", "category": "Patient"},
    "A009": {"name": "stand up", "category": "Patient"},
    "A018": {"name": "put on glasses", "category": "Patient"},
    "A019": {"name": "take off glasses", "category": "Patient"},
    "A041": {"name": "sneeze cough", "category": "Patient"},
    "A042": {"name": "staggering", "category": "Patient"},
    "A043": {"name": "falling down", "category": "Patient"},
    "A044": {"name": "headache", "category": "Patient"},
    "A045": {"name": "chest pain", "category": "Patient"},
    "A046": {"name": "back pain", "category": "Patient"},
    "A047": {"name": "neck pain", "category": "Patient"},
    "A048": {"name": "nausea vomiting", "category": "Patient"},
    "A049": {"name": "fan self", "category": "Patient"},
    "A080": {"name": "squat down", "category": "Patient"},
    "A103": {"name": "yawn", "category": "Patient"},
    "A108": {"name": "knock over", "category": "Patient"},

    #Caregiver Actions
    "A011": {"name": "reading", "category": "Caregiver"},
    "A012": {"name": "writing", "category": "Caregiver"},
    "A053": {"name": "pat on back", "category": "Caregiver"},
    "A054": {"name": "point finger", "category": "Caregiver"},
    "A056": {"name": "giving object", "category": "Caregiver"},
    "A059": {"name": "walking towards", "category": "Caregiver"},
    "A060": {"name": "walking apart", "category": "Caregiver"},
    "A085": {"name": "apply cream on face", "category": "Caregiver"},
    "A086": {"name": "apply cream on hand", "category": "Caregiver"},
    "A089": {"name": "put object into bag", "category": "Caregiver"},
    "A090": {"name": "take object out of bag", "category": "Caregiver"},
    "A091": {"name": "open box", "category": "Caregiver"},
    "A114": {"name": "carry object", "category": "Caregiver"},
    "A116": {"name": "follow", "category": "Caregiver"},
    "A119": {"name": "support somebody", "category": "Caregiver"},

    # shared Actions
    "A005": {"name": "drop", "category": "Shared"},
    "A006": {"name": "pick up", "category": "Shared"},
    "A028": {"name": "phone call", "category": "Shared"},
    "A055": {"name": "hugging", "category": "Shared"},
    "A058": {"name": "shaking hands", "category": "Shared"},
    "A092": {"name": "move heavy objects", "category": "Shared"},
    "A109": {"name": "grab stuff", "category": "Shared"},

    # Anomaly Actions
    "A050": {"name": "punch slap", "category": "Anomaly"},
    "A106": {"name": "hit with object", "category": "Anomaly"},

    # Out of Scope (Optional Handling)
    "A027": {"name": "jump up", "category": "Out_of_Scope"},
    "A107": {"name": "wield knife", "category": "Out_of_Scope"}
}