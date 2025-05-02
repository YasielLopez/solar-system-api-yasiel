from app import create_app, db
from app.models.Planet import Planet
from dotenv import load_dotenv

load_dotenv()

my_app = create_app()
with my_app.app_context():
    db.session.add(Planet('Mercury', 'The smallest and innermost planet in the Solar System', 4879)),
    db.session.add(Planet('Venus', 'Second planet from the Sun with thick atmosphere', 12104)),
    db.session.add(Planet('Earth', 'Our home planet and the only known planet with life', 12742)),
    db.session.add(Planet('Mars', 'The Red Planet, fourth from the Sun', 6779)),
    db.session.add(Planet('Jupiter', 'The largest planet in our Solar System', 139820)),
    db.session.add(Planet('Saturn', 'Known for its prominent ring system', 116460)),
    db.session.add(Planet('Uranus', 'The seventh planet from the Sun', 50724)),
    db.session.add(Planet('Neptune', 'The eighth and farthest planet from the Sun', 49244)),
    db.session.commit()
