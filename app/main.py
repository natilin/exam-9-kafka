from flask import Flask

from app.db.psql_database import init_db
from app.route.mail_route import email_blueprint

app = Flask(__name__)


if __name__ == "__main__":
    app.register_blueprint(email_blueprint, url_prefix="/api")
    init_db()
    app.run()