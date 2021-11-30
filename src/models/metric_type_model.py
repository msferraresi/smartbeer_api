from app import database, marshmallow

class MetricType(database.Model):
    __tablename__ = 'metric_type'
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(50))
    created_at = database.Column(database.DateTime, server_default=database.func.now())
    updated_at = database.Column(database.DateTime, onupdate=database.func.now())
    deleted_at = database.Column(database.DateTime, nullable=True)

class MetricTypeSchema(marshmallow.SQLAlchemyAutoSchema):
    class Meta:
        model = MetricType
        load_instance = True
        sqla_session = database.session
        fields = ('id', 'name')