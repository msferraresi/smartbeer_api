from app import database, marshmallow

class UserRole(database.Model):
    __tablename__ = 'user_role'
    id = database.Column(database.Integer, primary_key=True)
    user_public_id = database.Column(database.String(50), database.ForeignKey('user.public_id'))
    role_id = database.Column(database.Integer, database.ForeignKey('role.id'))
    created_at = database.Column(database.DateTime, server_default=database.func.now())
    updated_at = database.Column(database.DateTime, onupdate=database.func.now())
    deleted_at = database.Column(database.DateTime, nullable=True)

class UserRoleSchema(marshmallow.SQLAlchemyAutoSchema):
    class Meta:
        model = UserRole
        load_instance = True
        sqla_sesson = database.session
        fields = ('user_public_id', 'role_id')