import marshmallow

class FilesSchema(marshmallow.Schema):
    files = marshmallow.fields.Raw(metadata={'type': 'string', 'format': 'binary'}, required=True)
    
    @marshmallow.validates('files')
    def validates(self, files):
        if not files.filename.endswith('.csv'):
            raise marshmallow.ValidationError()                