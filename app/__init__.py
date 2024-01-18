import os

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from config import DevelopmentConfig, ProductionConfig, TestingConfig


app = Flask(__name__)

# Set the default configuration (development)
app.config.from_object(DevelopmentConfig)

# Override the configuration based on the FLASK_ENV environment variable
if os.environ.get('FLASK_ENV') == 'production':
    app.config.from_object(ProductionConfig)
elif os.environ.get('FLASK_ENV') == 'testing':
    app.config.from_object(TestingConfig)

db = SQLAlchemy(app)

api = Api(app)

from app.resources.todo_resource import TodoList, Todo

api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<todo_id>')
