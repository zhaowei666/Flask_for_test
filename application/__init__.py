from flask import Flask
from flask_cors import CORS
import os


app = Flask(__name__)
CORS(app)
config_file_address = os.getcwd() + '/config/config.py'
app.config.from_pyfile(config_file_address)

# PostgreSQL configuration
sqlalchemy_settings_key = 'SQLALCHEMY_DATABASE_SETTINGS'
sqlalchemy_settings = app.config.get(sqlalchemy_settings_key)
app.config.update({
    'SQLALCHEMY_DATABASE_URI':
        '{protocol}://{user_name}:{password}@{host}:{port}/{db_name}'.format(
            protocol=sqlalchemy_settings.get('PROTOCOL'),
            user_name=sqlalchemy_settings.get('USER_NAME'),
            password=sqlalchemy_settings.get('PASSWORD'),
            host=sqlalchemy_settings.get('HOST'),
            port=sqlalchemy_settings.get('PORT'),
            db_name=sqlalchemy_settings.get('DB_NAME')
        )
})

from application import views