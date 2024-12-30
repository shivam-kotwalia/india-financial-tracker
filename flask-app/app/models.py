from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class YourModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f'<YourModel {self.name}>'