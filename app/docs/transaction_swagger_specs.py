# transaction_swagger_specs.py

get_all_transactions_admin_spec = {
    "tags": ["Transactions"],
    "security": [{"bearerAuth": []}],
    "responses": {
        "200": {
            "description": "A list of all transactions (admin only)",
            "schema": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "integer", "example": 1},
                        "from_account_id": {"type": "integer", "example": 101},
                        "to_account_id": {"type": "integer", "example": 102},
                        "amount": {"type": "number", "format": "float", "example": 500.50},
                        "transaction_type": {"type": "string", "example": "transfer"},
                        "category_id": {"type": "integer", "description": "ID of the transaction category", "example": 1},
                        "bill_id": {"type": "integer", "description": "ID of the associated bill (if applicable)", "example": 2},
                        "created_at": {"type": "string", "format": "date-time", "example": "2023-10-01T12:30:00Z"},
                    },
                },
            },
        },
        "403": {"description": "Unauthorized access (admin only)"},
    },
}

get_all_transactions_spec = {
    "tags": ["Transactions"],
    "security": [{"bearerAuth": []}],
    "responses": {
        "200": {
            "description": "A list of transactions for the authenticated user",
            "schema": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "integer", "example": 1},
                        "from_account_id": {"type": "integer", "example": 101},
                        "to_account_id": {"type": "integer", "example": 102},
                        "amount": {"type": "number", "format": "float", "example": 500.50},
                        "transaction_type": {"type": "string", "example": "transfer"},
                        "category_id": {"type": "integer", "description": "ID of the transaction category", "example": 1},
                        "bill_id": {"type": "integer", "description": "ID of the associated bill (if applicable)", "example": 2},
                        "created_at": {"type": "string", "format": "date-time", "example": "2023-10-01T12:30:00Z"},
                    },
                },
            },
        },
        "403": {"description": "Unauthorized access"},
    },
}

get_transaction_by_id_spec = {
    "tags": ["Transactions"],
    "security": [{"bearerAuth": []}],
    "parameters": [
        {
            "name": "transaction_id",
            "in": "path",
            "required": True,
            "type": "integer",
            "description": "ID of the transaction to retrieve",
        }
    ],
    "responses": {
        "200": {
            "description": "Transaction details",
            "schema": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer", "example": 1},
                    "from_account_id": {"type": "integer", "example": 101},
                    "to_account_id": {"type": "integer", "example": 102},
                    "amount": {"type": "number", "format": "float", "example": 500.50},
                    "transaction_type": {"type": "string", "example": "transfer"},
                    "category_id": {"type": "integer", "description": "ID of the transaction category", "example": 1},
                    "bill_id": {"type": "integer", "description": "ID of the associated bill (if applicable)", "example": 2},
                    "created_at": {"type": "string", "format": "date-time", "example": "2023-10-01T12:30:00Z"},
                },
            },
        },
        "404": {"description": "Transaction not found"},
        "403": {"description": "Unauthorized access"},
    },
}

create_transaction_spec = {
    "tags": ["Transactions"],
    "security": [{"bearerAuth": []}],
    "parameters": [
        {
            "name": "transaction",
            "in": "body",
            "required": True,
            "schema": {
                "type": "object",
                "properties": {
                    "from_account_id": {"type": "integer", "description": "ID of the account sending funds", "example": 101},
                    "to_account_id": {"type": "integer", "description": "ID of the account receiving funds (only for transfers)", "example": 102},
                    "amount": {"type": "number", "format": "float", "description": "Amount of the transaction", "example": 500.50},
                    "transaction_type": {
                        "type": "string",
                        "enum": ["deposit", "withdrawal", "transfer"],
                        "description": "Type of transaction",
                        "example": "transfer"
                    },
                    "category_id": {"type": "integer", "description": "ID of the transaction category", "example": 1},
                    "bill_id": {"type": "integer", "description": "ID of the associated bill (if applicable)", "example": 2},
                    "description": {"type": "string", "description": "Optional description of the transaction", "example": "Monthly rent"},
                }
            }
        }
    ],
    "responses": {
        "201": {
            "description": "Transaction created successfully",
            "schema": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer", "description": "Transaction ID", "example": 1},
                    "from_account_id": {"type": "integer", "description": "ID of the account sending funds", "example": 101},
                    "to_account_id": {"type": "integer", "description": "ID of the account receiving funds", "example": 102},
                    "amount": {"type": "number", "format": "float", "description": "Transaction amount", "example": 500.50},
                    "transaction_type": {"type": "string", "description": "Type of transaction", "example": "transfer"},
                    "category_id": {"type": "integer", "description": "ID of the transaction category", "example": 1},
                    "bill_id": {"type": "integer", "description": "ID of the associated bill (if applicable)", "example": 2},
                    "created_at": {"type": "string", "format": "date-time", "example": "2023-10-01T12:30:00Z"},
                }
            }
        },
        "400": {"description": "Invalid input for transaction"},
        "403": {"description": "Unauthorized access"},
    }
}
