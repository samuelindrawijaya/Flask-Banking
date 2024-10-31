login_spec = {
    "tags": ["Authentication"],
    "summary": "Log in a user and issue JWT tokens",
    "description": "Log in a user by validating email and password. Issues an access token and a refresh token. If 2FA is enabled, prompts for OTP verification.",
    "parameters": [
        {
            "name": "body",
            "in": "body",
            "required": True,
            "schema": {
                "type": "object",
                "properties": {
                    "email": {"type": "string", "example": "johndoe@example.com"},
                    "password": {"type": "string", "example": "password123"},
                },
                "required": ["email", "password"]
            }
        }
    ],
    "responses": {
        "200": {
            "description": "Login successful",
            "schema": {
                "type": "object",
                "properties": {
                    "message": {"type": "string", "example": "Logged in successfully"},
                    "access_token": {"type": "string"},
                    "refresh_token": {"type": "string"}
                }
            }
        },
        "400": {"description": "Email or password is missing"},
        "401": {"description": "Invalid email or password"}
    }
}

verify_2fa_spec = {
    "tags": ["Authentication"],
    "summary": "Verify 2FA OTP",
    "description": "Verify the One-Time Password (OTP) for a user with 2FA enabled.",
    "parameters": [
        {
            "name": "body",
            "in": "body",
            "required": True,
            "schema": {
                "type": "object",
                "properties": {
                    "otp_code": {"type": "string", "example": "123456"}
                },
                "required": ["otp_code"]
            }
        }
    ],
    "responses": {
        "200": {"description": "2FA verified successfully"},
        "400": {"description": "Invalid or missing 2FA code"}
    }
}

logout_spec = {
    "tags": ["Authentication"],
    "summary": "Logout the user and reset 2FA verification",
    "description": "Logs out the user and resets their 2FA verification status.",
    "responses": {
        "200": {"description": "Logged out successfully"}
    }
}

enable_2fa_spec = {
    "tags": ["Authentication"],
    "summary": "Enable 2FA for a user",
    "description": "Generates a new 2FA secret for the user and sends them a provisioning URI to set up an authenticator app.",
    "responses": {
        "200": {
            "description": "2FA enabled and setup email sent",
            "schema": {
                "type": "object",
                "properties": {
                    "message": {"type": "string", "example": "2FA enabled and setup email sent"}
                }
            }
        },
        "500": {"description": "Error sending email"}
    }
}

refresh_token_spec = {
    "tags": ["Authentication"],
    "summary": "Refresh the access token",
    "description": "Refreshes the JWT access token using the refresh token.",
    "security": [{"bearerAuth": []}],
    "responses": {
        "200": {
            "description": "Access token refreshed",
            "schema": {
                "type": "object",
                "properties": {
                    "access_token": {"type": "string"}
                }
            }
        }
    }
}
