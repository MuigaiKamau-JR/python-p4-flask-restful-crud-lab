from app import app
from models import db, Plant

with app.app_context():
    db.create_all()

    aloe = Plant(name="Aloe", image="./images/aloe.jpg", price=11.50, is_in_stock=True)
    cactus = Plant(name="Cactus", image="./images/cactus.jpg", price=8.00, is_in_stock=True)

    db.session.add(aloe)
    db.session.add(cactus)
    db.session.commit()
