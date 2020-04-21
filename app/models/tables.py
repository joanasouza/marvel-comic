from app import db


class Character(db.Model):
    __tablename__ = "stories"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(180), nullable=False)

    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return "<%r>" self.name
    

class Story(db.Model):
    __tablename__ = "stories"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(String(90))
    attribution_text = db.Column(db.Text)
    character_id = db.Column(db.Integer, db.ForeignKey('characters.id'))

    character = db.relationship('Character', foreign_key=character_id)

    def __init__(self, title, description, attribution_text):
        self.title = title
        self.description = description
        self.attribution_text = attribution_text
    
    def __repr__(self):
        return "<%r>" self.title

    
