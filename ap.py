from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:qwerty@localhost/creditcard'
db = SQLAlchemy(app)

class Schema1(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Add other columns as needed

@app.route('/query', methods=['GET'])
def query_schema1():
    # Query the database using SQLAlchemy
    results = Schema1.query.all()
    
    # Return the results directly as JSON without serialization
    return jsonify([result.id for result in results])

if __name__ == '__main__':
    app.run(debug=True)
