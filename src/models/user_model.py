from app import database, marshmallow

class User(database.Model):
    __tablename__ = 'user'
    id = database.Column(database.Integer, primary_key=True)
    public_id = database.Column(database.String(50), unique=True)
    name = database.Column(database.String(50))
    password = database.Column(database.String(250))
    mail = database.Column(database.String(100), unique=True)
    created_at = database.Column(database.DateTime, server_default=database.func.now())
    updated_at = database.Column(database.DateTime, onupdate=database.func.now())
    deleted_at = database.Column(database.DateTime, nullable=True)

class UserSchema(marshmallow.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        sqla_session = database.session
        #fields = ('public_id', 'client_id', 'name', 'password', 'mail', 'admin', 'created_at')