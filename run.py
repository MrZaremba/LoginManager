#Runs the app, before this can run make sure the db is setup.  otherwise db.create_all() will not work.

from ICT import app
from ICT import db

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)