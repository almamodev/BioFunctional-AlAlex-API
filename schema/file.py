import marshmallow
import typing
import werkzeug.datastructures
import flask_smorest

class FileSchema(marshmallow.Schema):
    __metadata: typing.Dict[str, str] = {
        'type': 'string',
        'format': 'binary'
    }
    __required=True

    file = marshmallow.fields.Raw(metadata=__metadata, required=__required)
    
    @marshmallow.validates('file')
    def validates(self, file: werkzeug.datastructures.FileStorage) -> None:
        filename: str = file.filename

        if not filename.endswith('.csv'):
            code: int = 415
            flask_smorest.abort(code)           