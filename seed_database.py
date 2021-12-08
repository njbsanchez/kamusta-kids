"""Script to seed database."""

import json
from datetime import datetime
import sqlalchemy.exc as sq

import internal.model as m
import server


def get_categories():
    """Load dummy users from dataset into database."""

    # Load dummy user data from JSON file
    with open("data/cat_catalog.json") as f:
        dummy_entities = json.loads(f.read())
    # print (dummy_entities)
    # Create dummy users, store them in list so we can use them
    dummies_in_db = []
    for entity, details in dummy_entities[0].items():
        contact_name, company_name, entity_role, entity_type, email, phone, notes = (
            details["contact_name"],
            details["company_name"],
            details["entity_role"],
            details["entity_type"],
            details["email"],
            details["phone"],
            details["notes"]
        )
        # print(contact_name, company_name, entity_type, email, phone, notes)
        db_entity = m.Entity(
            contact_name, entity_role, company_name, entity_type, email, phone, notes
        )
        m.db.session.add(db_entity)

        try:
            m.db.session.commit()
        except sq.IntegrityError:
            m.db.session.rollback()
            print("entity already exists")

def get_courses():
    """Load dummy users from dataset into database."""

    # Load dummy class data from JSON file
    with open("data/class_catalog.json") as f:
        classes = json.loads(f.read())

    # Create dummy users
    for class_count, details in classes[0].items():
        level_no, level_name, description, registration_link, category, image_url = (
            details["level_no"],
            details["level_name"],
            details["description"],
            details["registration_link"],
            details["category"],
            details["image_url"]
        )

        db_class = m.Course(
            level_no, level_name, category, registration_link, description, image_url)
        
        m.db.session.add(db_class)
    
        try:
            m.db.session.commit()
        except sq.IntegrityError:
            m.db.session.rollback()
            print("class already exists")

if __name__ == "__main__":

    m.connect_to_db(server.app)

    print(
        "************************ CHECK IF DB CREATED ********************"
    )

    get_entities()

    print(
        "************************ DUMMY ENTITIES ADDED TO DB ********************"
    )

    get_staff()

    print(
        "************************ DUMMY STAFF ADDED TO DB ********************"
    )

    get_products()

    print(
        "************************ DUMMY PRODUCTS ADDED TO DB ********************"
    )

    get_intake()

    print(
        "************************ DUMMY INTAKES ADDED TO DB ********************"
    )

    m.db.session.commit()

