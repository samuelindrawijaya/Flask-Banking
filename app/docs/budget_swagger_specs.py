get_all_budgets_spec = {
    "tags": ["Budgets"],
    "security": [{"bearerAuth": []}],
    "responses": {
        "200": {
            "description": "A list of all budgets for the authenticated user",
            "schema": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "integer", "description": "Budget ID", "example": 1},
                        "user_id": {"type": "integer", "description": "User ID", "example": 1},
                        "name": {"type": "string", "description": "Name of the budget category", "example": "Groceries"},
                        "amount": {"type": "number", "format": "float", "description": "Budgeted amount", "example": 500.0},
                        "total_spent": {"type": "number", "format": "float", "description": "Amount spent so far", "example": 150.0},
                        "start_date": {"type": "string", "format": "date", "description": "Start date of the budget period", "example": "2024-11-01"},
                        "end_date": {"type": "string", "format": "date", "description": "End date of the budget period", "example": "2024-12-01"},
                    },
                },
            },
        },
        "403": {"description": "Unauthorized access"},
    },
}
create_budget_spec = {
    "tags": ["Budgets"],
    "security": [{"bearerAuth": []}],
    "parameters": [
        {
            "name": "budget",
            "in": "body",
            "required": True,
            "schema": {
                "type": "object",
                "properties": {
                    "name": {"type": "string", "description": "Name of the budget category", "example": "Groceries"},
                    "amount": {"type": "number", "format": "float", "description": "Total budget amount", "example": 500.0},
                    "start_date": {"type": "string", "format": "date", "description": "Start date of the budget period", "example": "2024-11-01"},
                    "end_date": {"type": "string", "format": "date", "description": "End date of the budget period", "example": "2024-12-01"},
                    "category_id": {"type": "integer", "description": "ID of the transaction category", "example": 2},
                },
                "required": ["name", "amount", "start_date", "end_date", "category_id"],
            },
        }
    ],
    "responses": {
        "201": {
            "description": "Budget created successfully",
            "schema": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer", "description": "Budget ID", "example": 1},
                    "name": {"type": "string", "description": "Budget category name", "example": "Groceries"},
                    "amount": {"type": "number", "format": "float", "description": "Total budgeted amount", "example": 500.0},
                    "total_spent": {"type": "number", "format": "float", "description": "Amount spent so far", "example": 0.0},
                    "start_date": {"type": "string", "format": "date", "description": "Start date of the budget", "example": "2024-11-01"},
                    "end_date": {"type": "string", "format": "date", "description": "End date of the budget", "example": "2024-12-01"},
                },
            },
        },
        "400": {"description": "Invalid input for creating a budget"},
    },
}
update_budget_spec = {
    "tags": ["Budgets"],
    "security": [{"bearerAuth": []}],
    "parameters": [
        {
            "name": "budget_id",
            "in": "path",
            "required": True,
            "type": "integer",
            "description": "ID of the budget to update",
        },
        {
            "name": "budget",
            "in": "body",
            "required": True,
            "schema": {
                "type": "object",
                "properties": {
                    "name": {"type": "string", "description": "Updated name of the budget category", "example": "Groceries"},
                    "amount": {"type": "number", "format": "float", "description": "Updated total budget amount", "example": 600.0},
                    "start_date": {"type": "string", "format": "date", "description": "Updated start date of the budget", "example": "2024-11-01"},
                    "end_date": {"type": "string", "format": "date", "description": "Updated end date of the budget", "example": "2024-12-31"},
                    "category_id": {"type": "integer", "description": "Updated transaction category ID", "example": 2},
                },
            },
        }
    ],
    "responses": {
        "200": {
            "description": "Budget updated successfully",
            "schema": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer", "description": "Budget ID", "example": 1},
                    "name": {"type": "string", "description": "Budget category name", "example": "Groceries"},
                    "amount": {"type": "number", "format": "float", "description": "Updated total budget amount", "example": 600.0},
                    "total_spent": {"type": "number", "format": "float", "description": "Amount spent so far", "example": 150.0},
                    "start_date": {"type": "string", "format": "date", "description": "Updated start date of the budget", "example": "2024-11-01"},
                    "end_date": {"type": "string", "format": "date", "description": "Updated end date of the budget", "example": "2024-12-31"},
                },
            },
        },
        "400": {"description": "Invalid input for updating the budget"},
        "404": {"description": "Budget not found"},
    },
}
delete_budget_spec = {
    "tags": ["Budgets"],
    "security": [{"bearerAuth": []}],
    "parameters": [
        {
            "name": "budget_id",
            "in": "path",
            "required": True,
            "type": "integer",
            "description": "ID of the budget to delete",
        }
    ],
    "responses": {
        "200": {
            "description": "Budget deleted successfully",
            "schema": {
                "type": "object",
                "properties": {
                    "message": {"type": "string", "example": "Budget deleted successfully"},
                },
            },
        },
        "404": {"description": "Budget not found"},
    },
}
