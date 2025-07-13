# from crypt import methods

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from requests import Response
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random
app = Flask(__name__)

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
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/random", methods=["GET"])
def get_random_cafe():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    random_cafe = random.choice(all_cafes)
    return jsonify(cafe=random_cafe.to_dict())

@app.route("/all", methods=["GET"])
def all_records():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    cafe_data = [cafe.to_dict() for cafe in all_cafes]
    return  jsonify(cafes=cafe_data)

@app.route("/search", methods=["GET"])
def search_by_location():
    location = request.args.get("location")
    result = db.session.execute(db.select(Cafe).where(Cafe.location == location))
    all_cafes = result.scalars().all()
    if all_cafes:
        return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}), 404
# HTTP GET - Read Record

@app.route("/add", methods=["POST"])
def add_cafe():
    print(request.form.get("wifi") == "true")
    print(type(request.form.get("wifi")))
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=request.form.get("sockets") == "true",
        has_toilet=request.form.get("toilet") == "true",
        has_wifi=request.form.get("wifi") == "true",
        can_take_calls=request.form.get("calls") == "true",
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)

    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})

# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def patch_new_price(cafe_id):
    new_price = request.args.get("new_price")
    print(f"New price: {new_price}")
    print(f"Cafe ID: {cafe_id}")

    cafe = db.session.get(Cafe, cafe_id)  # or db.session.get(Cafe, cafe_id) if using SQLAlchemy 2.0+

    if cafe is None:
        print("Cafe not found.")
        return jsonify(error={"Not Found": "Sorry, a cafe with that id was not found in the database."}), 404

    print(f"Found cafe: {cafe.name}")
    cafe.coffee_price = new_price
    db.session.commit()
    return jsonify(response={"success": "Successfully updated the price."}), 200

# HTTP DELETE - Delete Record

@app.route("/delete-cafe/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get("API_KEY")
    if api_key != "MY_SECRET_KEY":
        return jsonify(error={"message": "Please use a valid API key"}), 403

    cafe = db.session.get(Cafe, cafe_id)
    if cafe is None:
        return jsonify(error={"message": "Cafe not found"}), 404

    db.session.delete(cafe)
    db.session.commit()
    return jsonify(response={"message": "Cafe deleted successfully"}), 200


if __name__ == '__main__':
    app.run(debug=True)
