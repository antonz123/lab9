from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask('Города')
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///project.db"
db = SQLAlchemy(app)



class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String)
    visit_date = db.Column(db.Integer)
    liked = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<City {self.id} / {self.visit_date}> {self.city}'


@app.route('/')
def main():
    cities = City.query.all()
    return render_template('index.html', cities_list=cities)


@app.route('/city', methods=['POST'])
def add_city():
    data = request.json
    city = City(**data)
    db.session.add(city)
    db.session.commit()
    return 'OK'


@app.route('/update/<int:id>', methods=['PATCH'])
def update_satus(id):
    city = City.query.get(id)
    city.liked = request.json['liked']
    db.session.commit()
    return 'OK'


@app.route("/clear", methods=['DELETE'])
def clear_list():
    City.query.delete()
    db.session.commit()
    return 'OK'


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
