from app import database, marshmallow

class RecipeConfiguration(database.Model):
    __tablename__ = 'recipe_configuration'
    id = database.Column(database.Integer, primary_key=True)
    recipe_public_id = database.Column(database.String(50), database.ForeignKey('recipe.public_id'))
    name = database.Column(database.String(50), nullable=False)
    amount = database.Column(database.Float, nullable=False)
    metric_type_id = database.Column(database.Integer, database.ForeignKey('metric_type.id'))
    created_at = database.Column(database.DateTime, server_default=database.func.now())
    updated_at = database.Column(database.DateTime, onupdate=database.func.now())
    deleted_at = database.Column(database.DateTime, nullable=True)

class RecipeConfigurationSchema(marshmallow.SQLAlchemyAutoSchema):
    class Meta:
        model = RecipeConfiguration
        load_instance = True
        sqla_session = database.session
        fields = ('id', 'recipe_public_id', 'name', 'amount', 'metric_type_id')