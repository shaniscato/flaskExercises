from flask import Flask
from flask_mail import Mail

from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

upload_folder = 'uploads/profile_pics'
allowed_extensions = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


app = Flask(__name__)
app.config.from_object(Config)
app.config['UPLOAD_FOLDER'] = upload_folder
db = SQLAlchemy(app)
migrate = Migrate(app, db)
mail = Mail(app)

login = LoginManager(app)
login.login_view = 'login'




from app import routes, models
