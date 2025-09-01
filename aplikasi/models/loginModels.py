from aplikasi import db, login_manager
from flask_login import UserMixin

class Users(db.Model, UserMixin):
    __table_args__ = {'schema': 'portfolio_tracker'}
    id = db.Column(db.String(255), primary_key = True)
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))
    name = db.Column(db.String(200))

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))    