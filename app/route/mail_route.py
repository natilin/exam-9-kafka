from flask import Blueprint, request, jsonify

from app.repository.person_repository import get_context_by_email
from app.services.send_all_messages_producer import producer_send_message

email_blueprint = Blueprint('email', __name__)

@email_blueprint.route('/email', methods=['POST'])
def email_listing():
    mail = request.json
    producer_send_message(mail)
    return jsonify({}), 201


@email_blueprint.route('/context/<email>', methods=['GET'])
def get_context(email):
    data = get_context_by_email(email)
    return jsonify(data), 200