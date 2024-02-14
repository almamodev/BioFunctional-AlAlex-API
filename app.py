import flask
import flask_smorest
import flask_cors
import view.kegg
import typing
import dotenv
import os

dotenv.load_dotenv()

app: flask.Flask = flask.Flask(__name__)
api_title: str = os.getenv('API_TITLE')
api_version: str = os.getenv('API_VERSION')
openapi_version: str = os.getenv('OPENAPI_VERSION')
app.config['API_TITLE'] = api_title
app.config['API_VERSION'] = api_version
app.config['OPENAPI_VERSION'] = openapi_version
api: flask_smorest.Api = flask_smorest.Api(app)
kegg: flask_smorest.Blueprint = view.kegg.blueprint
api.register_blueprint(kegg)
resources: typing.Dict[str, typing.Dict[str, str]] = {
    r'*': {
        'origins': '*'
    }
}
cors: flask_cors.CORS = flask_cors.CORS(app, resources=resources)
if __name__ == '__main__':
    port: int = os.getenv('PORT')
    app.run(port=port)