import flask_smorest
import flask.views
import schema.files
from pathway import Pathway
from parse import Parse
import flask
import typing
import werkzeug.datastructures
import os

blueprint: flask_smorest.Blueprint = flask_smorest.Blueprint('kegg', __name__)

@blueprint.route('/kegg')
class KeggView(flask.views.MethodView):
    @blueprint.arguments(schema.files.FilesSchema, location='files')
    @blueprint.response(200)
    def post(self, payload: typing.Dict[str, werkzeug.datastructures.FileStorage]) -> flask.Response:
        files: werkzeug.datastructures.FileStorage = payload['files']
        filename: str = files.filename
        files.save(filename)
        parse: Parse = Parse(filename)
        rowdicts: typing.List[typing.Dict[str, typing.Any]] = parse.reader()
        pathway: Pathway = Pathway()
        for collection in pathway.collection():
            for row in rowdicts:
                if row['relation'][2:] in collection['relation']:
                    row['interaction'] = collection['interaction']['name']
                    row['reaction'] = collection['reaction']['name']
        parse.writer(rowdicts)

        @blueprint.after_request
        def after_request(response: flask.Response) -> flask.Response:
            os.remove(filename)
            return response

        return flask.send_file(filename, as_attachment=True)

        
        

        
        

        
        






        




