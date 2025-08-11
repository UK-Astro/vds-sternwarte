from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///D:/work/vds-sternwarte/instance/DBLDVdS01.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    image_file = db.Column(db.String(255), nullable=False)

def encrypt_passwords():
    with app.app_context():
        musers = User.query.all()
        for Muser in musers:
            if not Muser.password.startswith('$2b$'):  # Überprüfen, ob das Passwort bereits gehasht ist
                hashed_password = bcrypt.generate_password_hash(Muser.password).decode('utf-8')
                Muser.password = hashed_password
                # Muser.image_file = 'default.jpg'
        db.session.commit()
    print("Passwörter wurden erfolgreich verschlüsselt.")

if __name__ == '__main__':
    encrypt_passwords()
