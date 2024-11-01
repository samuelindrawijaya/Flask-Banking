from flask import Blueprint
from app.controller.TransactionCategoryController import TransactionCategoryController
from app.controller.bill_controller import BillController
from app.controller.budget_controller import BudgetController
from app.controller.role_controller import RoleController
from app.controller.user_controller import UserController
from app.controller.account_controller import AccountController
from app.controller.transaction_controller import TransactionController
from app.controller.auth_controller import AuthController  # Import the AuthController
from app.middleware.auth_middleware import admin_required, token_required, two_fa_required  # Include 2FA middleware

user_bp = Blueprint('users', __name__)
account_bp = Blueprint('accounts', __name__)
transaction_bp = Blueprint('transactions', __name__)
auth_bp = Blueprint('auth', __name__)  # Add auth routes
role_bp = Blueprint('roles', __name__)
bill_bp = Blueprint('bills', __name__)
budget_bp = Blueprint('budgets', __name__)
transaction_category_bp = Blueprint('transaction_categories', __name__)

budget_bp.add_url_rule('/', view_func=token_required(two_fa_required(BudgetController.get_all_budgets)), methods=['GET'])
budget_bp.add_url_rule('/', view_func=token_required(two_fa_required(BudgetController.create_budget)), methods=['POST'])
budget_bp.add_url_rule('/<int:budget_id>', view_func=token_required(two_fa_required(BudgetController.update_budget)), methods=['PUT'])

transaction_category_bp.add_url_rule('/', view_func=token_required(two_fa_required(TransactionCategoryController.get_all_categories)), methods=['GET'])
transaction_category_bp.add_url_rule('/<int:category_id>', view_func=token_required(two_fa_required(TransactionCategoryController.get_category_by_id)), methods=['GET'])
transaction_category_bp.add_url_rule('/', view_func=token_required(two_fa_required(TransactionCategoryController.create_category)), methods=['POST'])
transaction_category_bp.add_url_rule('/<int:category_id>', view_func=token_required(two_fa_required(TransactionCategoryController.update_category)), methods=['PUT'])
transaction_category_bp.add_url_rule('/<int:category_id>', view_func=token_required(two_fa_required(TransactionCategoryController.delete_category)), methods=['DELETE'])

bill_bp.add_url_rule('/', view_func=token_required(two_fa_required(BillController.get_all_bills)), methods=['GET'])
bill_bp.add_url_rule('/', view_func=token_required(two_fa_required(BillController.create_bill)), methods=['POST'])
bill_bp.add_url_rule('/<int:bill_id>', view_func=token_required(two_fa_required(BillController.update_bill)), methods=['PUT'])
bill_bp.add_url_rule('/<int:bill_id>', view_func=token_required(two_fa_required(BillController.delete_bill)), methods=['DELETE'])
bill_bp.add_url_rule('/process-due', view_func=token_required(two_fa_required(BillController.process_due_bills)), methods=['POST'])

# Authentication Routes
auth_bp.add_url_rule('/login', view_func=AuthController.login, methods=['POST'])
auth_bp.add_url_rule('/logout', view_func=token_required(AuthController.logout), methods=['POST'])  # Requires token
auth_bp.add_url_rule('/enable-2fa', view_func=token_required(AuthController.enable_2fa), methods=['POST'])
auth_bp.add_url_rule('/verify-2fa', view_func=token_required(AuthController.verify_2fa), methods=['POST'])
auth_bp.add_url_rule('/refresh', view_func=AuthController.refresh_token, methods=['POST'])  # Refresh JWT token

# User Routes
user_bp.add_url_rule('/', view_func=UserController.add_user, methods=['POST'])
user_bp.add_url_rule('/me', view_func=token_required(UserController.get_user_profile), methods=['GET'])
user_bp.add_url_rule('/me', view_func=token_required(UserController.update_user_profile), methods=['PUT'])

# Account Routes (with 2FA check for extra security)
account_bp.add_url_rule('/', view_func=token_required(two_fa_required(AccountController.get_all_accounts)), methods=['GET'])
account_bp.add_url_rule('/<int:account_id>', view_func=token_required(two_fa_required(AccountController.get_account_by_id)), methods=['GET'])
account_bp.add_url_rule('/', view_func=token_required(two_fa_required(AccountController.create_account)), methods=['POST'])
account_bp.add_url_rule('/<int:account_id>', view_func=token_required(two_fa_required(AccountController.update_account)), methods=['PUT'])
account_bp.add_url_rule('/<int:account_id>', view_func=token_required(two_fa_required(AccountController.delete_account)), methods=['DELETE'])

# Transaction Routes (with 2FA check for extra security)
transaction_bp.add_url_rule('/', view_func=token_required(two_fa_required(TransactionController.get_all_transactions)), methods=['GET'])
transaction_bp.add_url_rule('/<int:transaction_id>', view_func=token_required(two_fa_required(TransactionController.get_transaction_by_id)), methods=['GET'])
transaction_bp.add_url_rule('/', view_func=token_required(two_fa_required(TransactionController.create_transaction)), methods=['POST'])



role_bp.add_url_rule('/', view_func=token_required(two_fa_required(RoleController.get_all_roles)), methods=['GET'])
role_bp.add_url_rule('/<int:role_id>', view_func=token_required(two_fa_required(RoleController.get_role_by_id)), methods=['GET'])
role_bp.add_url_rule('/', view_func=token_required(two_fa_required(RoleController.add_role)), methods=['POST'])
role_bp.add_url_rule('/<int:role_id>', view_func=token_required(two_fa_required(RoleController.update_role)), methods=['PUT'])
role_bp.add_url_rule('/<int:role_id>', view_func=token_required(two_fa_required(RoleController.delete_role)), methods=['DELETE'])

# # Admin-only User Management Routes
user_bp.add_url_rule('/admin/users', view_func=token_required(admin_required(UserController.get_all_users_admin)), methods=['GET'])

# # # Admin-only Account Management
account_bp.add_url_rule('/admin/accounts', view_func=token_required(admin_required(AccountController.get_all_accounts_admin)), methods=['GET'])

# # # Admin-only Transaction Management
transaction_bp.add_url_rule('/admin/transactions', view_func=token_required(admin_required(TransactionController.get_all_transactions_admin)), methods=['GET'])
