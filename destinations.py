"""Belfast City Airport (BHD) destinations — May 2026."""

DESTINATIONS = {
    "BHD": {
        "name": "Belfast City",
        "routes": {
            # UK & Ireland
            "ABZ": "Aberdeen",
            "BHX": "Birmingham",
            "BRS": "Bristol",
            "CWL": "Cardiff",
            "EDI": "Edinburgh",
            "EMA": "East Midlands",
            "EXT": "Exeter",
            "GLA": "Glasgow",
            "INV": "Inverness",
            "IOM": "Isle of Man",
            "LBA": "Leeds Bradford",
            "LCY": "London City",
            "LGW": "London Gatwick",
            "LHR": "London Heathrow",
            "LPL": "Liverpool",
            "LTN": "London Luton",
            "MAN": "Manchester",
            "SEN": "London Southend",
            "SOU": "Southampton",
            # Benelux
            "AMS": "Amsterdam",
            # Balearic Islands, Spain
            "PMI": "Palma de Mallorca",
            # Italy
            "BLQ": "Bologna",
            "VRN": "Verona",
        },
    },
}


def get_destinations(airport: str) -> dict:
    entry = DESTINATIONS.get(airport, {})
    return entry.get("routes", {})


def get_airport_name(airport: str) -> str:
    entry = DESTINATIONS.get(airport, {})
    return entry.get("name", airport)
