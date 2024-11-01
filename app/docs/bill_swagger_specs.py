create_bill_spec = {
    "tags": ["Bills"],
    "security": [{"bearerAuth": []}],
    "parameters": [
        {
            "name": "bill",
            "in": "body",
            "required": True,
            "schema": {
                "type": "object",
                "properties": {
                    "biller_name": {"type": "string", "description": "Name of the biller", "example": "Electric Company"},
                    "due_date": {"type": "string", "format": "date", "description": "Due date for the bill payment", "example": "2024-12-01"},
                    "amount": {"type": "number", "format": "float", "description": "Amount of the bill payment", "example": 150.50},
                    "account_id": {"type": "integer", "description": "ID of the account to deduct the payment from", "example": 1}
                },
                "required": ["biller_name", "due_date", "amount", "account_id"],
            },
        }
    ],
    "responses": {
        "201": {
            "description": "Bill created successfully",
            "schema": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer", "description": "Bill ID", "example": 1},
                    "biller_name": {"type": "string", "description": "Biller name", "example": "Electric Company"},
                    "due_date": {"type": "string", "format": "date", "description": "Due date", "example": "2024-12-01"},
                    "amount": {"type": "number", "format": "float", "description": "Amount due", "example": 150.50},
                    "account_id": {"type": "integer", "description": "Associated account ID", "example": 1}
                },
            },
        },
        "400": {"description": "Invalid input provided"},
    },
}
get_all_bills_spec = {
    "tags": ["Bills"],
    "security": [{"bearerAuth": []}],
    "responses": {
        "200": {
            "description": "List of all bills for the authenticated user",
            "schema": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "integer", "description": "Bill ID", "example": 1},
                        "biller_name": {"type": "string", "description": "Biller name", "example": "Electric Company"},
                        "due_date": {"type": "string", "format": "date", "description": "Due date", "example": "2024-12-01"},
                        "amount": {"type": "number", "format": "float", "description": "Amount due", "example": 150.50},
                        "account_id": {"type": "integer", "description": "Associated account ID", "example": 1}
                    },
                },
            },
        },
        "403": {"description": "Unauthorized access"},
    },
}
update_bill_spec = {
    "tags": ["Bills"],
    "security": [{"bearerAuth": []}],
    "parameters": [
        {
            "name": "bill_id",
            "in": "path",
            "required": True,
            "type": "integer",
            "description": "ID of the bill to update",
        },
        {
            "name": "bill",
            "in": "body",
            "required": True,
            "schema": {
                "type": "object",
                "properties": {
                    "biller_name": {"type": "string", "description": "Updated biller name", "example": "Electric Company"},
                    "due_date": {"type": "string", "format": "date", "description": "Updated due date", "example": "2024-12-10"},
                    "amount": {"type": "number", "format": "float", "description": "Updated amount", "example": 175.00},
                    "account_id": {"type": "integer", "description": "Updated account ID", "example": 1}
                },
            },
        }
    ],
    "responses": {
        "200": {
            "description": "Bill updated successfully",
            "schema": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer", "description": "Bill ID", "example": 1},
                    "biller_name": {"type": "string", "description": "Updated biller name", "example": "Electric Company"},
                    "due_date": {"type": "string", "format": "date", "description": "Updated due date", "example": "2024-12-10"},
                    "amount": {"type": "number", "format": "float", "description": "Updated amount due", "example": 175.00},
                    "account_id": {"type": "integer", "description": "Updated associated account ID", "example": 1}
                },
            },
        },
        "400": {"description": "Invalid input provided"},
        "404": {"description": "Bill not found"},
    },
}
delete_bill_spec = {
    "tags": ["Bills"],
    "security": [{"bearerAuth": []}],
    "parameters": [
        {
            "name": "bill_id",
            "in": "path",
            "required": True,
            "type": "integer",
            "description": "ID of the bill to delete",
        }
    ],
    "responses": {
        "200": {
            "description": "Bill deleted successfully",
            "schema": {
                "type": "object",
                "properties": {
                    "message": {"type": "string", "example": "Bill deleted successfully"},
                },
            },
        },
        "404": {"description": "Bill not found"},
    },
}
process_due_bills_spec = {
    "tags": ["Bills"],
    "security": [{"bearerAuth": []}],
    "responses": {
        "200": {
            "description": "Due bills processed successfully",
            "schema": {
                "type": "object",
                "properties": {
                    "message": {"type": "string", "example": "Due bills processed successfully"},
                },
            },
        },
        "403": {"description": "Unauthorized access"},
    },
}
