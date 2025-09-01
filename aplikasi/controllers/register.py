from aplikasi import app, bcrypt
from flask_login import current_user

@app.route('/register', methods=['POST', 'GET'])
def register():
    return True

        