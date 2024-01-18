from app import db

class TodoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(255))

    def __init__(self, task):
        self.task = task
