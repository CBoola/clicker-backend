CURRENT_STATE_SCHEMA = {
    "type": "object",
    "properties": {
        "cash": {
            "type": "integer",
            "default": 0,
            "minimum": 0
        }
    }
}


STRUCTURES_SCHEMA = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "system_id": {"type": "string"},
            "amount": {"type": "integer", "minimum": 0}
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


ACHIEVEMENT_SCHEMA = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "system_id": {"type": "string"},
            "time": {"type": "date-time"}
        }
    },
    "default": []
}


STATISTICS_SCHEMA = {
    "type": "object",
    "properties": {
        "number_of_clicks": {
            "type": "integer",
            "default": 0,
            "minimum": 0
        },

        "collected_cash": {
            "type": "integer",
            "default": 0,
            "minimum": 0
        },

        "spent_cash": {
            "type": "integer",
            "default": 0,
            "minimum": 0
        },

        "cash_from_clicks": {
            "type": "integer",
            "default": 0,
            "minimum": 0
        }
    }
}
