from app import database, marshmallow

class RecipeType(database.Model):
    __tablename__ = 'recipe_type'
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(50))
    created_at = database.Column(database.DateTime, server_default=database.func.now())
    updated_at = database.Column(database.DateTime, onupdate=database.func.now())
    deleted_at = database.Column(database.DateTime, nullable=True)

class RecipeTypeSchema(marshmallow.SQLAlchemyAutoSchema):
    class Meta:
        model = RecipeType
        load_instance = True
        sqla_session = database.session
        fields = ('id', 'name')