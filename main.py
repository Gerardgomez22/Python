from flask import Flask
from src.api.routes import init_api_routes
from src.config import db
from src.models.game import Game 

app = Flask(__name__)

db.Base.metadata.create_all(db.engine)

init_api_routes(app)

if __name__ == '__main__':
    app.run(debug=True)