from flask import Blueprint, jsonify, request, redirect, url_for, make_response
from flask_cors import CORS
from flask_login import login_user, logout_user, current_user, login_required
import requests
import json
from models.Account import Account
from utils.log import logger

consume_public_apis_routes = Blueprint('consume_public_apis_routes', __name__)

@consume_public_apis_routes.route('/', methods=['POST'])
@login_required
def index():
    if request.method == 'POST':
        if current_user.is_authenticated:
            try:
                response = requests.get('https://api.publicapis.org/entries')
            except Exception as e:
                logger.Error(e)
            return response.json(), 201
        else:
            response = '{"Erro": "Faça o login primeiro"}'
            return json.loads(response), 201


@consume_public_apis_routes.route('/login', methods=['GET','POST'])
def login():
    print(request.json)
    if request.method == 'POST':
        if request.json:
            username = request.json['username']
            password = request.json['password']
            print(username)
            user = Account.query.filter(
                            Account.username.like(username),
                            Account.password.like(password)
            ).first()
            if(user):
                logger.info("Logando usuário: " + user.username)
                login_user(user)
                #return redirect(url_for('consume_public_apis_routes.index'), code=307)
                response = '{"Sucesso": "Usuário logado"}'
                return json.loads(response), 201
            else:
                response = '{"Erro": "Usuário ou senha inválidos"}'
                return json.loads(response), 401

@consume_public_apis_routes.route('/logout', methods=['GET', 'POST'])
def logout():
    logger.info("Deslogando usuário")
    logout_user()
    response = '{"Sucesso": "Logout realizado com sucesso"}'
    return json.loads(response), 201

