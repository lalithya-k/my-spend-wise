import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from flask import Flask
from flask_cors import CORS
from api.budgets import budgets_bp
from api.expenses import expenses_bp
from api.auth import auth_bp
from database.db import initialize_db

app = Flask(__name__)
CORS(app)

# Configuration for MongoDB
app.config['MONGO_URI'] = 'mongodb://localhost:27017/budget_app'  # Update with your MongoDB URI
initialize_db(app)

# Register Blueprints
app.register_blueprint(budgets_bp, url_prefix='/api/budgets')
app.register_blueprint(expenses_bp, url_prefix='/api/expenses')
app.register_blueprint(auth_bp, url_prefix='/api/auth')

if __name__ == "__main__":
    app.run(debug=True)
