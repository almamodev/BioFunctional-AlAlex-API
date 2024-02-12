import flask
import flask_smorest
import flask_cors
import view.kegg
import typing

app: flask.Flask = flask.Flask(__name__)
app.config['API_TITLE'] = ''
app.config['API_VERSION'] = ''
app.config['OPENAPI_VERSION'] = '3.1.0'

app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api: flask_smorest.Api = flask_smorest.Api(app)
api.register_blueprint(view.kegg.blueprint)

resources: typing.Dict[str, typing.Dict[str, str]] = {
    r'*': {
        'origins': '*'
    }
}
cors: flask_cors.CORS = flask_cors.CORS(app, resources=resources)

if __name__ == '__main__':
    app.run()