from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Load configuration from config.py
    app.config.from_object('config')

    # Initialize extensions here (e.g., database, login manager)

    # Import and register blueprints
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app