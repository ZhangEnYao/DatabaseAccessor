from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from source.index import index_blueprint
from source.login import User, login_blueprint

application = Flask(__name__)
boostrap = Bootstrap(application)
login_manager = LoginManager()
login_manager.init_app(application)

application.secret_key = 'Data Analysis Team'
login_manager.login_view = 'login.login'
login_manager.login_message = ''

@login_manager.user_loader
def user_loader(user_id):
    user = User()
    user.id = user_id
    return user

application.register_blueprint(index_blueprint)
application.register_blueprint(login_blueprint)