import flask_smorest
import flask.views
import schema.file
import service.pathway
import service.parser
import flask
import typing
import werkzeug.datastructures
import os
import requests

blueprint: flask_smorest.Blueprint = flask_smorest.Blueprint('kegg', __name__)

@blueprint.route('/kegg')
class KeggView(flask.views.MethodView):
    @blueprint.arguments(schema.file.FileSchema, location='files')
    @blueprint.response(200)
    def post(self, payload: typing.Dict[str, werkzeug.datastructures.FileStorage]) -> flask.Response:
        """
        Handles POST requests to the KEGG endpoint.

        :payload: The payload containing the uploaded file.
        :return: A response containing the processed file.
        """
        try:
            file: werkzeug.datastructures.FileStorage = payload['file']
            filename: str = file.filename
            file.save(filename)
            parser: service.parser.Parser = service.parser.Parser(filename)
            pathway: service.pathway.Pathway = service.pathway.Pathway()
            rowdicts: typing.List[typing.Dict[str, typing.Any]] = parser.reader()
            collection: typing.List[typing.Dict[str, str]] = pathway.collection()
            for map in collection:
                for row in rowdicts:
                    if row['ONTOLOGY'][2:] in map['relation']:
                        row['interaction'] = map['interaction']['name']
                        row['reaction'] = map['reaction']['name']
            parser.writer(rowdicts)
            response: flask.Response = flask.send_file(filename, as_attachment=True)
            return response
        except KeyError:
            code: int = 404
            message: str = "Column name allowed: 'ONTOLOGY'"
            flask_smorest.abort(code, message=message)
        except requests.RequestException as exception:
            code: int = exception.response.status_code
            flask_smorest.abort(code)
        

        
        






        




