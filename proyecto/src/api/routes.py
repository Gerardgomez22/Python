from flask import request, jsonify
from src.config.db import session
from src.models.game import Game

def init_api_routes(app):

    # --- GET: Obtener todos ---
    @app.route('/api/games', methods=['GET'])
    def get_games():
        games = session.query(Game).all()
        result = []
        for game in games:
            result.append({
                'id': game.id,
                'title': game.title,
                'genre': game.genre,
                'price': game.price
            })
        return jsonify(result)

    # --- POST: Crear uno nuevo ---
    @app.route('/api/games', methods=['POST'])
    def create_game():
        data = request.get_json()
        new_game = Game(
            title=data.get('title'),
            genre=data.get('genre'),
            price=data.get('price')
        )
        session.add(new_game)
        session.commit()
        return jsonify({'message': 'Juego creado', 'id': new_game.id}), 201

    # --- PUT: Actualizar ---
    @app.route('/api/games/<int:game_id>', methods=['PUT'])
    def update_game(game_id):
        data = request.get_json()
        game = session.query(Game).filter_by(id=game_id).first()
        
        if game:
            game.title = data.get('title', game.title)
            game.genre = data.get('genre', game.genre)
            game.price = data.get('price', game.price)
            session.commit()
            return jsonify({'message': 'Juego actualizado'}), 200
        return jsonify({'error': 'No encontrado'}), 404

    # --- DELETE: Borrar ---
    @app.route('/api/games/<int:game_id>', methods=['DELETE'])
    def delete_game(game_id):
        game = session.query(Game).filter_by(id=game_id).first()
        if game:
            session.delete(game)
            session.commit()
            return jsonify({'message': 'Juego eliminado'}), 200
        return jsonify({'error': 'No encontrado'}), 404