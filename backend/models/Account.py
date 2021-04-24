from app import login_manager, db
from flask_login import UserMixin


''' 
Extende UserMixin, os atributos e métodos necessários para passar um objeto User 
como parametro para a função login_user de flask_login (routes/routes.py -> line 28)
são implementados pela classe UserMixin: is_authenticated; is_active; is_anonymous; get_id().
'''
class Account(db.Model, UserMixin):
    __tablename__ = 'account'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

#standalone callback function
@login_manager.user_loader
def get_user(user_id):
    return Account.query.filter_by(id=user_id).first()