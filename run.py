"""Contains application entry point."""

from app import app
from app.db.init_db import db

if __name__ == '__main__':
    # Set the FLASK_ENV environment variable to 'production' or 'testing' if needed
    # Example: export FLASK_ENV=production
    app.run(debug=True)
