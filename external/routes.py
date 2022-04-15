from flask import render_template
from app import app
from flask_wtf import form
import time
import datetime
from model import Category, Course

@app.route("/", methods=['GET'])
def go_homepage():
    """dummy development page"""
    course_detail = Course.query.first()
    return render_template("homepage.html", course_detail=course_detail)

@app.route("/about", methods=['GET'])
def go_about():
    """dummy development page"""
    return render_template("aboutus.html")

@app.route("/base", methods=['GET'])
def go_base():
    """dummy development page"""
    return render_template("base.html")

@app.route("/how-learning-works", methods=['GET'])
def go_learning():
    """dummy development page"""
    return render_template("how.html")

@app.route("/courses", methods=['GET'])
def go_courses():
    """dummy development page"""
    cat_details = Category.query.order_by(Category.cat_no).all()
    
    return render_template("courses.html", cat_details=cat_details)

@app.route("/request-info", methods=['GET'])
def request_info():
    """dummy development page"""
    return render_template("request_info.html")

@app.route("/enroll", methods=['GET'])
def go_enroll():
    """dummy development page"""
    return render_template("enroll.html")

@app.route("/coming-soon", methods=['GET'])
def coming_soon():
    """dummy development page"""
    return render_template("coming_soon.html")

