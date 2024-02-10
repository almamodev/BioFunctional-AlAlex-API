import flask
import flask_smorest
import flask_cors
from view import kegg

app: flask.Flask = flask.Flask(__name__)
app.config['API_TITLE'] = ''
app.config['API_VERSION'] = ''
app.config['OPENAPI_VERSION'] = '3.1.0'

api: flask_smorest.Api = flask_smorest.Api(app)
api.register_blueprint(kegg.blueprint)

cors: flask_cors.CORS = flask_cors.CORS(app, resources={r'*': {'origins': '*'}})

if __name__ == '__main__':
    app.run(debug=True)