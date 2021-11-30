from app import database, marshmallow

class Role(database.Model):
    __tablename__ = 'role'
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(50))
    created_at = database.Column(database.DateTime, server_default=database.func.now())
    updated_at = database.Column(database.DateTime, onupdate=database.func.now())
    deleted_at = database.Column(database.DateTime, nullable=True)

class RoleSchema(marshmallow.SQLAlchemyAutoSchema):
    class Meta:
        model = Role
        load_instance = True
        sqla_sesson = database.session
        fields = ('id', 'name')