from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/database_name'
db = SQLAlchemy(app)

# Define model classes for each schema

class Schema1(db.Model):
    __table_args__ = {'schema': 'schema1'}
    id = db.Column(db.Integer, primary_key=True)
    # Add other columns as needed

class Schema2(db.Model):
    __table_args__ = {'schema': 'schema2'}
    id = db.Column(db.Integer, primary_key=True)
    # Add other columns as needed

class Schema3(db.Model):
    __table_args__ = {'schema': 'schema3'}
    id = db.Column(db.Integer, primary_key=True)
    # Add other columns as needed

class Schema4(db.Model):
    __table_args__ = {'schema': 'schema4'}
    id = db.Column(db.Integer, primary_key=True)
    # Add other columns as needed

class Schema5(db.Model):
    __table_args__ = {'schema': 'schema5'}
    id = db.Column(db.Integer, primary_key=True)
    # Add other columns as needed

@app.route('/query/<schema>', methods=['GET'])
def query_schema(schema):
    if schema not in ['schema1', 'schema2', 'schema3', 'schema4', 'schema5']:
        return jsonify({'error': 'Invalid schema'}), 400
    
    # Select the appropriate model class based on the schema provided
    model_class = globals()[schema.capitalize()]
    
    # Query the database using SQLAlchemy
    results = model_class.query.all()
    
    # Return the results directly as JSON without serialization
    return jsonify([result.id for result in results])

if __name__ == '__main__':
    app.run(debug=True)
