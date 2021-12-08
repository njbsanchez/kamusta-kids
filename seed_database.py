"""Script to seed database."""

import json
from datetime import datetime
import sqlalchemy.exc as sq

import model as m
import server


def get_categories():
    """Load dummy users from dataset into database."""

    # Load dummy user data from JSON file
    with open("data/cat_catalog.json") as f:
        categories = json.loads(f.read())

    for cat_count, details in categories[0].items():
        cat_no, cat_name, pre_req = (
            int(details["cat_no"]),
            details["cat_name"],
            details["pre_req"]
        )
        # print(contact_name, company_name, entity_type, email, phone, notes)
        db_category = m.Category(
            cat_no, cat_name, pre_req)
        m.db.session.add(db_category)

        try:
            m.db.session.commit()
        except sq.IntegrityError:
            m.db.session.rollback()
            print("category already exists")

def get_courses():
    """Load dummy users from dataset into database."""

    # Load dummy course data from JSON file
    with open("data/course_catalog.json") as f:
        courses = json.loads(f.read())

    # Create dummy users
    for course_count, details in courses[0].items():
        course_no, course_name, description, registration_link, category, image_url = (
            int(details["course_no"]),
            details["course_name"],
            details["description"],
            details["registration_link"],
            int(details["category"]),
            details["image_url"]
        )

        db_course = m.Course(
            course_no, course_name, category, registration_link, description, image_url)
        
        m.db.session.add(db_course)
    
        try:
            m.db.session.commit()
        except sq.IntegrityError:
            m.db.session.rollback()
            print("course already exists")

if __name__ == "__main__":

    m.connect_to_db(server.app)

    print(
        "************************ CHECK IF DB CREATED ********************"
    )

    get_categories()

    print(
        "************************ CATEGORIES ADDED TO DB ********************"
    )

    get_courses()

    print(
        "************************ COURSES ADDED TO DB ********************"
    )

    m.db.session.commit()

