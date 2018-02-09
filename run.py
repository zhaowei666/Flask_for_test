from application import app
from flask_cors import CORS

CORS(app)
app.config.from_pyfile('../config/config.py')
app.run(host=app.config['HOST'],
        port=app.config['PORT'],
        debug=app.config['DEBUG'])

