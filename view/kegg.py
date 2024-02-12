import flask_smorest
import flask.views
import schema.file
import service.pathway
import service.parser
import flask
import typing
import werkzeug.datastructures
import os
import marshmallow

blueprint: flask_smorest.Blueprint = flask_smorest.Blueprint('kegg', __name__)

@blueprint.route('/kegg')
class KeggView(flask.views.MethodView):
    @blueprint.arguments(schema.file.FileSchema, location='files')
    @blueprint.response(200)
    def post(self, payload: typing.Dict[str, werkzeug.datastructures.FileStorage]) -> flask.Response:
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
                    if row['relation'][2:] in map['relation']:
                        row['interaction'] = map['interaction']['name']
                        row['reaction'] = map['reaction']['name']

            parser.writer(rowdicts)

            response: flask.Response = flask.send_file(filename, as_attachment=True)

            os.remove(filename)
            
            return response
        except KeyError:
            flask.abort(404)
        except marshmallow.ValidationError:
            flask.abort(415)

        
        

        
        

        
        






        




