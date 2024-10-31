get_all_users_admin_spec = {
    "tags": ["Users"],
    "security": [{"bearerAuth": []}],
    "responses": {
        "200": {
            "description": "A list of users",
            "schema": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "integer", "description": "User ID", "example": 1},
                        "username": {"type": "string", "description": "Username", "example": "johndoe"},
                        "email": {"type": "string", "description": "Email", "example": "johndoe@example.com"},
                        "roles": {
                            "type": "array",
                            "description": "List of roles assigned to the user",
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
            },
        },
        "403": {
            "description": "Unauthorized access (only Admin can access)"
        }
    }
}

add_user_spec = {
    "tags": ["Users"],
    "security": [{"bearerAuth": []}],
    "parameters": [
        {
            "name": "user",
            "in": "body",
            "required": True,
            "schema": {
                "type": "object",
                "properties": {
                    "username": {"type": "string"},
                    "email": {"type": "string"},
                    "password": {"type": "string"},
                    "roles": {
                        "type": "array",
                        "items": {"type": "string"}
                    },
                }
            }
        }
    ],
    "responses": {
        "201": {
            "description": "User created",
            "schema": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer", "description": "User ID", "example": 1},
                    "username": {"type": "string", "description": "User username", "example": "johndoe"},
                    "email": {"type": "string", "description": "User email", "example": "johndoe@example.com"},
                    "roles": {
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
        },
        "400": {"description": "Missing required fields"},
        "409": {"description": "User already exists"},
    }
}

get_user_profile_spec = {
    "tags": ["Users"],
    "security": [{"bearerAuth": []}],
    "responses": {
        "200": {
            "description": "User profile details",
            "schema": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer", "description": "User ID", "example": 1},
                    "username": {"type": "string", "description": "Username", "example": "johndoe"},
                    "email": {"type": "string", "description": "Email", "example": "johndoe@example.com"},
                    "roles": {
                        "type": "array",
                        "description": "List of roles assigned to the user",
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
        },
        "404": {"description": "User not found"},
    }
}

update_user_profile_spec = {
    "tags": ["Users"],
    "security": [{"bearerAuth": []}],
    "parameters": [
        {
            "name": "user",
            "in": "body",
            "required": True,
            "schema": {
                "type": "object",
                "properties": {
                    "username": {"type": "string", "description": "New username", "example": "johndoe_updated"},
                    "email": {"type": "string", "description": "New email", "example": "johndoe_updated@example.com"},
                    "password": {"type": "string", "description": "New password", "example": "newpassword123"},
                    "roles": {
                        "type": "array",
                        "items": {"type": "string"}
                    },
                }
            }
        }
    ],
    "responses": {
        "200": {
            "description": "User profile updated successfully",
            "schema": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer", "description": "User ID", "example": 1},
                    "username": {"type": "string", "description": "Updated username", "example": "johndoe_updated"},
                    "email": {"type": "string", "description": "Updated email", "example": "johndoe_updated@example.com"},
                    "roles": {
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
        },
        "400": {"description": "Invalid input or email validation error"},
        "404": {"description": "User not found"},
    }
}
