
from datetime import timedelta


# MAINTENANCE TRANSACTION RULE HERE !

TRANSACTION_RULES = {
    "checking": {
        "daily_limit": 100000,
        "monthly_limit": 500000,
        "allowed_transactions": ["deposit", "withdrawal", "transfer", "bill payment"],
        "hold_period": timedelta(days=0),  # No hold period for checking accounts
        "budget_tracking": True  # Enable budget tracking for categories
    },
    "savings": {
        "daily_limit": 50000,
        "monthly_limit": 2000000,
        "allowed_transactions": ["deposit", "withdrawal"],
        "hold_period": timedelta(days=3),  # 3-day hold period for deposits
        "budget_tracking": False  # Budget tracking not required for savings accounts
    },
    "business": {
        "daily_limit": 200000,
        "monthly_limit": 1000000,
        "allowed_transactions": ["deposit", "withdrawal", "transfer", "bill payment"],
        "hold_period": timedelta(days=1),  # 1-day hold period for deposits
        "budget_tracking": True  # Enable budget tracking for categories
    }
}

def get_transaction_rules(account_type):
    return TRANSACTION_RULES.get(account_type)