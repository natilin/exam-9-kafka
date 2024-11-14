from flask import Blueprint, request, jsonify

email_blueprint = Blueprint('email', __name__)

@email_blueprint.route('/email', methods=['POST'])
def email_listing():
    mail = request.json
    print(mail)
    return jsonify({}), 201