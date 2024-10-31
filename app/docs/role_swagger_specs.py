get_all_roles_spec = {
    "tags": ["Roles"],
    "security": [{"bearerAuth": []}],
    "responses": {
        "200": {
            "description": "A list of roles",
            "schema": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "integer", "description": "Role ID", "example": 1},
                        "name": {"type": "string", "description": "Role name", "example": "Admin"},
                    },
                },
            },
        },
    },
}

get_role_by_id_spec = {
    "tags": ["Roles"],
    "security": [{"bearerAuth": []}],
    "parameters": [
        {
            "name": "role_id",
            "in": "path",
            "required": True,
            "type": "integer",
            "description": "ID of the role to retrieve",
        }
    ],
    "responses": {
        "200": {
            "description": "Role details",
            "schema": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer", "description": "Role ID", "example": 1},
                    "name": {"type": "string", "description": "Role name", "example": "Admin"},
                },
            },
        },
        "404": {"description": "Role not found"},
    },
}

add_role_spec = {
    "tags": ["Roles"],
    "security": [{"bearerAuth": []}],
    "parameters": [
        {
            "name": "role",
            "in": "body",
            "required": True,
            "schema": {
                "type": "object",
                "properties": {
                    "name": {"type": "string", "description": "Name of the role", "example": "Editor"},
                },
            },
        }
    ],
    "responses": {
        "201": {
            "description": "Role created successfully",
            "schema": {
                "type": "object",
                "properties": {
                    "message": {"type": "string", "description": "Success message"},
                    "role": {
                        "type": "object",
                        "properties": {
                            "id": {"type": "integer", "description": "Role ID", "example": 1},
                            "name": {"type": "string", "description": "Role name", "example": "Editor"},
                        },
                    },
                },
            },
        },
        "400": {"description": "Role name is required"},
    },
}

update_role_spec = {
    "tags": ["Roles"],
    "security": [{"bearerAuth": []}],
    "parameters": [
        {
            "name": "role_id",
            "in": "path",
            "required": True,
            "type": "integer",
            "description": "ID of the role to update",
        },
        {
            "name": "role",
            "in": "body",
            "required": True,
            "schema": {
                "type": "object",
                "properties": {
                    "name": {"type": "string", "description": "Updated name of the role", "example": "Manager"},
                },
            },
        }
    ],
    "responses": {
        "200": {
            "description": "Role updated successfully",
            "schema": {
                "type": "object",
                "properties": {
                    "message": {"type": "string", "description": "Success message"},
                    "role": {
                        "type": "object",
                        "properties": {
                            "id": {"type": "integer", "description": "Role ID", "example": 1},
                            "name": {"type": "string", "description": "Updated role name", "example": "Manager"},
                        },
                    },
                },
            },
        },
        "400": {"description": "Role name is required"},
        "404": {"description": "Role not found"},
    },
}

delete_role_spec = {
    "tags": ["Roles"],
    "security": [{"bearerAuth": []}],
    "parameters": [
        {
            "name": "role_id",
            "in": "path",
            "required": True,
            "type": "integer",
            "description": "ID of the role to delete",
        }
    ],
    "responses": {
        "200": {"description": "Role deleted successfully"},
        "404": {"description": "Role not found"},
    },
}
