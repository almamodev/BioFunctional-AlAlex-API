import marshmallow
import typing
import werkzeug.datastructures

class FilesSchema(marshmallow.Schema):
    __metadata: typing.Dict[str, str] = {
        'type': 'string',
        'format': 'binary'
    }
    __required = True

    files: marshmallow.fields.Raw = marshmallow.fields.Raw(metadata=__metadata, required=__required)

    @marshmallow.validates('files')
    def validates(self, files: werkzeug.datastructures.FileStorage) -> None:
        filename: str = files.filename

        if not filename.endswith('.csv'):
            raise marshmallow.ValidationError()                