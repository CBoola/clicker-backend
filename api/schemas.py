CURRENT_STATE_SCHEMA = {
    "type": "object",
    "properties": {
        "cash": {
            "type": "integer",
            "default": 0
        }
    }
}


STRUCTURES_SCHEMA = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "system_id": {"type": "string"},
            "amount": {"type": "integer"}
        }
    },
    "default": []
}


UPGRADES_SCHEMA = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "system_id": {"type": "string"}
        }
    },
    "default": []
}


STATISTICS_SCHEMA = {
    "type": "object",
    "properties": {
        "number_of_clicks": {
            "type": "integer",
            "default": 0
        }
    }
}
