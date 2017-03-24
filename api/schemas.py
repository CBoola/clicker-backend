CURRENT_STATE_SCHEMA = {
    "type": "objects",
    "properties": {
        "cash": {"type": "number"}
    }
}


STRUCTURES_SCHEMA = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "system_id": {"type": "string"},
            "amount": {"type": "number"}
        }
    }
}


UPGRADES_SCHEMA = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "system_id": {"type": "string"}
        }
    }
}


STATISTICS_SCHEMA = {
    "type": "objects",
    "properties": {
        "number_of_clicks": {"type": "number"}
    }
}
