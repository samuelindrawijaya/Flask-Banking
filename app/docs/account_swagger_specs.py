get_all_accounts_admin_spec = {
    "tags": ["Accounts"],
    "security": [{"bearerAuth": []}],
    "responses": {
        "200": {
            "description": "A list of all accounts (Admin only)",
            "schema": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "integer", "description": "Account ID", "example": 1},
                        "user_id": {"type": "integer", "description": "User ID", "example": 1},
                        "account_type": {"type": "string", "description": "Account type", "example": "savings"},
                        "account_number": {"type": "string", "description": "Account number", "example": "1234567890"},
                        "balance": {"type": "number", "format": "float", "description": "Account balance", "example": 5000.75},
                        "created_at": {"type": "string", "format": "date-time", "description": "Account creation time", "example": "2024-10-24T12:34:56Z"},
                    },
                },
            },
        },
        "403": {"description": "Unauthorized access (only Admin can access)"},
    },
}

get_account_by_id_spec = {
    "tags": ["Accounts"],
    "security": [{"bearerAuth": []}],
    "parameters": [
        {
            "name": "account_id",
            "in": "path",
            "required": True,
            "type": "integer",
            "description": "ID of the account to retrieve",
        }
    ],
    "responses": {
        "200": {
            "description": "Account details",
            "schema": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer", "description": "Account ID", "example": 1},
                    "user_id": {"type": "integer", "description": "User ID", "example": 1},
                    "account_type": {"type": "string", "description": "Account type", "example": "savings"},
                    "account_number": {"type": "string", "description": "Account number", "example": "1234567890"},
                    "balance": {"type": "number", "format": "float", "description": "Account balance", "example": 5000.75},
                    "created_at": {"type": "string", "format": "date-time", "description": "Account creation time", "example": "2024-10-24T12:34:56Z"},
                },
            },
        },
        "404": {"description": "Account not found"},
    },
}

create_account_spec = {
    "tags": ["Accounts"],
    "security": [{"bearerAuth": []}],
    "parameters": [
        {
            "name": "account",
            "in": "body",
            "required": True,
            "schema": {
                "type": "object",
                "properties": {
                    "account_type": {"type": "string", "description": "Type of the account to create", "example": "savings"},
                },
                "required": ["account_type"],
            },
        }
    ],
    "responses": {
        "201": {
            "description": "Account created",
            "schema": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer", "description": "Account ID", "example": 1},
                    "account_type": {"type": "string", "description": "Account type", "example": "savings"},
                    "account_number": {"type": "string", "description": "Account number", "example": "1234567890"},
                    "balance": {"type": "number", "format": "float", "description": "Initial balance", "example": 0.0},
                    "created_at": {"type": "string", "format": "date-time", "description": "Account creation time", "example": "2024-10-24T12:34:56Z"},
                },
            },
        },
        "400": {"description": "Invalid account type or balance provided"},
    },
}

update_account_spec = {
    "tags": ["Accounts"],
    "security": [{"bearerAuth": []}],
    "parameters": [
        {
            "name": "account_id",
            "in": "path",
            "required": True,
            "type": "integer",
            "description": "ID of the account to update",
        },
        {
            "name": "account",
            "in": "body",
            "required": True,
            "schema": {
                "type": "object",
                "properties": {
                    "account_number": {
                        "type": "string",
                        "description": "Updated account number",
                        "example": "0987654321",
                    },
                },
            },
        }
    ],
    "responses": {
        "200": {
            "description": "Account updated successfully",
            "schema": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer", "description": "Account ID", "example": 1},
                    "account_type": {"type": "string", "description": "Account type", "example": "savings"},
                    "account_number": {"type": "string", "description": "Updated account number", "example": "0987654321"},
                    "balance": {"type": "number", "format": "float", "description": "Current balance", "example": 5500.50},
                },
            },
        },
        "400": {"description": "Invalid input for account update"},
        "404": {"description": "Account not found"},
    },
}


delete_account_spec = {
    "tags": ["Accounts"],
    "security": [{"bearerAuth": []}],
    "parameters": [
        {
            "name": "account_id",
            "in": "path",
            "required": True,
            "type": "integer",
            "description": "ID of the account to mark as deleted",
        }
    ],
    "responses": {
        "200": {
            "description": "Account marked as deleted successfully",
            "schema": {
                "type": "object",
                "properties": {
                    "message": {"type": "string", "example": "Account marked as deleted successfully"},
                    "account": {
                        "type": "object",
                        "properties": {
                            "id": {"type": "integer", "description": "Account ID", "example": 1},
                            "is_deleted": {"type": "boolean", "description": "Deletion status", "example": True},
                        },
                    },
                },
            },
        },
        "404": {"description": "Account not found"},
    },
}

get_all_accounts_spec = {
    "tags": ["Accounts"],
    "security": [{"bearerAuth": []}],
    "responses": {
        "200": {
            "description": "A list of accounts for the authenticated user",
            "schema": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "integer", "description": "Account ID", "example": 1},
                        "account_type": {"type": "string", "description": "Type of account", "example": "checking"},
                        "account_number": {"type": "string", "description": "Account number", "example": "1234567890"},
                        "balance": {"type": "number", "description": "Account balance", "example": 1000.50},
                        "created_at": {"type": "string", "format": "date-time", "description": "Account creation time"},
                        "is_deleted": {"type": "boolean", "description": "Account deletion status", "example": False},
                    },
                },
            },
        },
        "403": {"description": "Unauthorized access"},
    },
}

