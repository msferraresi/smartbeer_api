from app import database, marshmallow

class Recipe(database.Model):
    __tablename__ = 'recipe'
    id = database.Column(database.Integer, primary_key=True)
    recipe_type_id = database.Column(database.Integer, database.ForeignKey('recipe_type.id'))
    user_public_id = database.Column(database.String(50), database.ForeignKey('user.public_id'))
    public_id = database.Column(database.String(50), unique=True)
    name = database.Column(database.String(50), default='New Recipe')
    cooking_count = database.Column(database.Integer, default=0)
    created_at = database.Column(database.DateTime, server_default=database.func.now())
    updated_at = database.Column(database.DateTime, onupdate=database.func.now())
    deleted_at = database.Column(database.DateTime, nullable=True)

class RecipeSchema(marshmallow.SQLAlchemyAutoSchema):
    class Meta:
        model = Recipe
        load_instance = True
        sqla_session = database.session
        fields = ('public_id', 'recipe_type_id', 'user_public_id', 'name', 'cooking_count')