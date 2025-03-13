from app import create_app, db
from models import User

flask_app = create_app()

with flask_app.app_context():
    # Вставляем данные
    person1 = User(uid=27, username='Mike', password='12345', role='Lead', description='IT')
    person2 = User(uid=28, username='Bob', password='12345', role='Lead', description='IT')

    db.session.add(person1)
    db.session.add(person2)
    db.session.commit()

    # SELECT
    people = User.query.all()
    for p in people:
        print(f"{p.username} - {p.uid} - {p.role}")
