CURRENT_STATE_SCHEMA = {
    "type": "object",
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
    "type": "object",
    "properties": {
        "number_of_clicks": {"type": "number"}
    }
}
