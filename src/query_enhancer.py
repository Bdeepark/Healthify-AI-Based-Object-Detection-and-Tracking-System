def enhance_query(query):
    query = query.lower()

    if "drink" in query or "drinking" in query:
        return query + " A001"
    if "sit" in query:
        return query + " A008"
    if "stand" in query:
        return query + " A009"
    if "stagger" in query:
        return query + " A042"
    if "fall" in query:
        return query + " A043"
    if "cough" in query or "sneeze" in query:
        return query + " A041"
    if "chest" in query:
        return query + " A045"
    if "back" in query:
        return query + " A046"
    if "yawn" in query:
        return query + " A103"

    if "walk towards" in query or "approach" in query:
        return query + " A059"
    if "walk away" in query:
        return query + " A060"
    if "help" in query or "assist" in query or "support" in query:
        return query + " A119"
    if "give" in query:
        return query + " A056"
    if "read" in query:
        return query + " A011"
    if "write" in query:
        return query + " A012"
    if "cream" in query:
        return query + " A085"

    return query