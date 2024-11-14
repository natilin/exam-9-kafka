from flask import Blueprint, request, jsonify

from app.services.send_all_messages_producer import producer_send_message

email_blueprint = Blueprint('email', __name__)

@email_blueprint.route('/email', methods=['POST'])
def email_listing():
    mail = request.json
    producer_send_message(mail)
    return jsonify({}), 201