create_category_spec = {
    "tags": ["Transaction Categories"],
    "security": [{"bearerAuth": []}],
    "parameters": [
        {
            "name": "category",
            "in": "body",
            "required": True,
            "schema": {
                "type": "object",
                "properties": {
                    "name": {"type": "string", "description": "Name of the transaction category", "example": "Groceries"}
                },
                "required": ["name"]
            },
        }
    ],
    "responses": {
        "201": {
            "description": "Category created successfully",
            "schema": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer", "description": "Category ID", "example": 1},
                    "name": {"type": "string", "description": "Category name", "example": "Groceries"}
                },
            },
        },
        "400": {"description": "Invalid input"},
    },
}
get_all_categories_spec = {
    "tags": ["Transaction Categories"],
    "security": [{"bearerAuth": []}],
    "responses": {
        "200": {
            "description": "A list of all transaction categories",
            "schema": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "integer", "description": "Category ID", "example": 1},
                        "name": {"type": "string", "description": "Category name", "example": "Groceries"}
                    },
                },
            },
        },
    },
}
get_category_by_id_spec = {
    "tags": ["Transaction Categories"],
    "security": [{"bearerAuth": []}],
    "parameters": [
        {
            "name": "category_id",
            "in": "path",
            "required": True,
            "type": "integer",
            "description": "ID of the category to retrieve",
        }
    ],
    "responses": {
        "200": {
            "description": "Category details",
            "schema": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer", "description": "Category ID", "example": 1},
                    "name": {"type": "string", "description": "Category name", "example": "Groceries"}
                },
            },
        },
        "404": {"description": "Category not found"},
    },
}
update_category_spec = {
    "tags": ["Transaction Categories"],
    "security": [{"bearerAuth": []}],
    "parameters": [
        {
            "name": "category_id",
            "in": "path",
            "required": True,
            "type": "integer",
            "description": "ID of the category to update",
        },
        {
            "name": "category",
            "in": "body",
            "required": True,
            "schema": {
                "type": "object",
                "properties": {
                    "name": {"type": "string", "description": "Updated category name", "example": "Rent"}
                },
                "required": ["name"]
            },
        }
    ],
    "responses": {
        "200": {
            "description": "Category updated successfully",
            "schema": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer", "description": "Category ID", "example": 1},
                    "name": {"type": "string", "description": "Updated category name", "example": "Rent"}
                },
            },
        },
        "400": {"description": "Invalid input"},
        "404": {"description": "Category not found"},
    },
}
delete_category_spec = {
    "tags": ["Transaction Categories"],
    "security": [{"bearerAuth": []}],
    "parameters": [
        {
            "name": "category_id",
            "in": "path",
            "required": True,
            "type": "integer",
            "description": "ID of the category to delete",
        }
    ],
    "responses": {
        "200": {
            "description": "Category deleted successfully",
            "schema": {
                "type": "object",
                "properties": {
                    "message": {"type": "string", "example": "Category deleted successfully"}
                },
            },
        },
        "404": {"description": "Category not found"},
    },
}
