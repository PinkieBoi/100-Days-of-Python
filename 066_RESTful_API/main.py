from random import choice

import werkzeug.exceptions
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Boolean
from flask import Flask, jsonify, render_template, request
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


app = Flask(__name__)
app.secret_key = "495v8vty4q5t8n8734ct5b8cbc387tbc13trr4"
Bootstrap5(app)


# CREATE DB
class Base(DeclarativeBase):
    pass


# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)
    
    def to_dict(self):
        dictionary = {}
        # Loop through each column in the data record
        for column in self.__table__.columns:
            # Create a new dictionary entry;
            # where the key is the name of the column
            # and the value is the value of the column
            dictionary[column.name] = getattr(self, column.name)
        return dictionary


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random", methods=['GET'])
def get_random():
    with app.app_context():
        rand_cafe = choice(db.session.execute(db.select(Cafe)).scalars().all())
    return jsonify(cafes=[rand_cafe.to_dict()])


@app.route("/all")
def get_all():
    with app.app_context():
        all_cafes = db.session.execute(db.select(Cafe)).scalars().all()
    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])


@app.route("/search")
def cafe_search():
    cafes_found = db.session.execute(db.select(Cafe).where(
        Cafe.location == request.args.get('location').title())).scalars().all()
    if len(cafes_found) > 0:
        return jsonify(cafes=[cafe.to_dict() for cafe in cafes_found])
    else:
        return jsonify({"error": {"Not Found": "Sorry, we do not have a cafe at that location."}})


# HTTP POST - Create Record
@app.route("/add", methods=['POST'])
def add_cafe():
    with app.app_context():
        new_cafe = Cafe(
            name=request.form['name'],
            map_url=request.form['map_url'],
            img_url=request.form['img_url'],
            location=request.form['location'],
            seats=request.form['seats'],
            has_wifi=int(request.form['has_wifi']),
            has_toilet=int(request.form['has_toilet']),
            has_sockets=int(request.form['has_sockets']),
            can_take_calls=int(request.form['can_take_calls']),
            coffee_price=request.form['coffee_price'],
        )
        db.session.add(new_cafe)
        db.session.commit()
        return jsonify(response={"success": "Cafe added successfully."})


# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=['PATCH'])
def update_price(cafe_id):
    with app.app_context():
        try:
            cafe = db.get_or_404(Cafe, cafe_id)
            cafe.coffee_price = request.args.get('new_price')
            db.session.commit()
            return jsonify(response={"success": "Coffee price updates successfully."})
        except werkzeug.exceptions.NotFound:
            return jsonify(error={"Not Found": f"Cafe ID {cafe_id} not found"}), 404


# HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=['DELETE'])
def report_closed(cafe_id):
    submitted_api_key = request.args.get('api-key')
    api_key = "TopSecretAPIKeyTotallyDontShare"
    if submitted_api_key == api_key:
        try:
            cafe = db.get_or_404(Cafe, cafe_id)
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"Cafe Deleted": "Cafe record successfully deleted."})
        except werkzeug.exceptions.NotFound:
            return jsonify(error={"Not Found": f"Cafe ID {cafe_id} not found"}), 404
    else:
        return jsonify(error={"Not Authorized": "API Key not recognised"}), 403


if __name__ == '__main__':
    app.run(debug=True)
