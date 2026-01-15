from flask import Flask, jsonify
from flask_migrate import Migrate
from models import db, Earthquake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)

@app.route('/')
def index():
    return '<h1>Flask SQLAlchemy Lab</h1>'

# Task #3: Get earthquake by id
@app.route('/earthquakes/<int:id>')
def get_earthquake_by_id(id):
    earthquake = Earthquake.query.filter_by(id=id).first()
    
    if earthquake:
        return jsonify(earthquake.to_dict()), 200
    else:
        return jsonify({"message": f"Earthquake {id} not found."}), 404

# Task #4: Get earthquakes by minimum magnitude
@app.route('/earthquakes/magnitude/<float:magnitude>')
def get_earthquakes_by_magnitude(magnitude):
    earthquakes = Earthquake.query.filter(Earthquake.magnitude >= magnitude).all()
    
    quakes_list = [quake.to_dict() for quake in earthquakes]
    
    return jsonify({
        "count": len(quakes_list),
        "quakes": quakes_list
    }), 200

if __name__ == '__main__':
    app.run(port=5555, debug=True)