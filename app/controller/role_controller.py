from flasgger import swag_from
from flask import request
from app.services.role_services import RoleServices
from app.utils.response import Response
from app.docs.role_swagger_specs import (
    get_all_roles_spec,
    get_role_by_id_spec,
    add_role_spec,
    update_role_spec,
    delete_role_spec
)

class RoleController:
    
    @staticmethod
    @swag_from(get_all_roles_spec)
    def get_all_roles():
        roles = RoleServices.list_roles()
        return Response.success([role.to_dict() for role in roles], 200)

    @staticmethod
    @swag_from(get_role_by_id_spec)
    def get_role_by_id(role_id):
        role = RoleServices.get_role_by_id(role_id)
        if role:
            return Response.success(role.to_dict(), 200)
        return Response.error('Role not found', 404)

    @staticmethod
    @swag_from(add_role_spec)
    def add_role():
        data = request.get_json()
        if not data or 'name' not in data:
            return Response.error('Role name is required', 400)

        role = RoleServices.create_role(data['name'])
        return Response.success({
            'message': f"Role '{data['name']}' created successfully.",
            'role': role.to_dict()
        }, 201)

    @staticmethod
    @swag_from(update_role_spec)
    def update_role(role_id):
        data = request.get_json()
        if not data or 'name' not in data:
            return Response.error('Role name is required', 400)

        role = RoleServices.update_role(role_id, data['name'])
        if role:
            return Response.success({
                'message': f"Role '{data['name']}' updated successfully.",
                'role': role.to_dict()
            }, 200)
        return Response.error('Role not found', 404)

    @staticmethod
    @swag_from(delete_role_spec)
    def delete_role(role_id):
        deleted = RoleServices.delete_role(role_id)
        if deleted:
            return Response.success({'message': 'Role deleted successfully.'}, 200)
        return Response.error('Role not found', 404)
