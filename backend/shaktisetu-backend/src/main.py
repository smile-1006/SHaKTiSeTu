import os
import sys
# DON'T CHANGE THIS !!!
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from flask import Flask, send_from_directory, jsonify
from src.models.user import db
from src.routes.user import user_bp
from src.routes.auth import auth_bp
from src.routes.marketplace import marketplace_bp
from src.routes.storefront import storefront_bp
from src.routes.learning import learning_bp
from src.routes.government import government_bp
from src.routes.mentorship import mentorship_bp

app = Flask(__name__, static_folder=os.path.join(os.path.dirname(__file__), 'static'))
app.config['SECRET_KEY'] = 'asdf#FGSgvasgf$5$WGT'

# Register all blueprints
app.register_blueprint(user_bp, url_prefix='/api/users')
app.register_blueprint(auth_bp, url_prefix='/api/auth')
app.register_blueprint(marketplace_bp, url_prefix='/api/marketplace')
app.register_blueprint(storefront_bp, url_prefix='/api/storefronts')
app.register_blueprint(learning_bp, url_prefix='/api/learning')
app.register_blueprint(government_bp, url_prefix='/api/government')
app.register_blueprint(mentorship_bp, url_prefix='/api/mentorship')

# Enable database
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{os.getenv('DB_USERNAME', 'root')}:{os.getenv('DB_PASSWORD', 'password')}@{os.getenv('DB_HOST', 'localhost')}:{os.getenv('DB_PORT', '3306')}/{os.getenv('DB_NAME', 'mydb')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
with app.app_context():
    db.create_all()

# API status endpoint
@app.route('/api/status', methods=['GET'])
def api_status():
    return jsonify({
        'status': 'online',
        'name': 'ShaktiSetu API',
        'version': '1.0.0'
    })

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    static_folder_path = app.static_folder
    if static_folder_path is None:
            return "Static folder not configured", 404

    if path != "" and os.path.exists(os.path.join(static_folder_path, path)):
        return send_from_directory(static_folder_path, path)
    else:
        index_path = os.path.join(static_folder_path, 'index.html')
        if os.path.exists(index_path):
            return send_from_directory(static_folder_path, 'index.html')
        else:
            return "index.html not found", 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
