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
    file:  marshmallow.fields.Raw = marshmallow.fields.Raw(metadata=__metadata, required=__required)
    
    @marshmallow.validates('file')
    def validates(self, file: werkzeug.datastructures.FileStorage) -> None:
        """
        Validates the file field for CSV format.
        
        :file: The FileStorage object representing the uploaded file.
        """
        filename: str = file.filename
        suffix: str = '.csv'
        if not filename.endswith(suffix):
            code: int = 415
            message: str = 'Content-Type allowed: text/csv'
            flask_smorest.abort(code, message=message)           