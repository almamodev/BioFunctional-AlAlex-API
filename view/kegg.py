import flask_smorest
import asyncio
import flask.views
import schema.files
import typing
import werkzeug.datastructures
from pathway import Pathway
from parse import Parse

blueprint: flask_smorest.Blueprint = flask_smorest.Blueprint('kegg', __name__)

@blueprint.route('/kegg')
class KEGGView(flask.views.MethodView):
    @blueprint.arguments(schema.files.FilesSchema, location='files')
    @blueprint.response(200)
    async def post(self, payload: typing.Dict[str, werkzeug.datastructures.FileStorage]) -> None:
        files: werkzeug.datastructures.FileStorage = payload['files']

        parse: Parse = Parse(files)
        rowdicts: typing.List[typing.Dict[str, typing.Any]] = parse.reader()

        pathway: Pathway = Pathway()
        






        




