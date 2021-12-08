
from model import db, connect_to_db
from app import app
# import internal.routes
import external.routes

if __name__ == '__main__':
    
    connect_to_db(app)
    db.create_all()
    app.run()
        