from flask import jsonify, request
from app.services.role_services import RoleServices



class RoleController:
    @staticmethod
    def get_all_roles():
        roles = RoleServices.list_roles()
        return jsonify([role.to_dict() for role in roles]), 200

    @staticmethod
    def get_role_by_id(role_id):
        role = RoleServices.get_role_by_id(role_id)
        if role:
            return jsonify(role.to_dict()), 200
        return jsonify({'message': 'Role not found'}), 404

    @staticmethod
    def add_role():
        data = request.get_json()
        if not data or 'name' not in data:
            return jsonify({'message': 'Role name is required'}), 400

        role = RoleServices.create_role(data['name'])
        return jsonify({
            'message': f"Role '{data['name']}' created successfully.",
            'role': role.to_dict()
        }), 201

    @staticmethod
    def update_role(role_id):
        data = request.get_json()
        if not data or 'name' not in data:
            return jsonify({'message': 'Role name is required'}), 400

        role = RoleServices.update_role(role_id, data['name'])
        if role:
            return jsonify({
                'message': f"Role '{data['name']}' updated successfully.",
                'role': role.to_dict()
            }), 200
        return jsonify({'message': 'Role not found'}), 404

    @staticmethod
    def delete_role(role_id):
        deleted = RoleServices.delete_role(role_id)
        if deleted:
            return jsonify({'message': 'Role deleted successfully.'}), 200
        return jsonify({'message': 'Role not found'}), 404

