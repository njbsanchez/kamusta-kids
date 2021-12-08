from flask import render_template
from app import app
from flask_wtf import form
import time
import datetime
from model import Category, Course

@app.route("/")
def go_homepage():
    """dummy development page"""
    return render_template("homepage.html")

@app.route("/about")
def go_about():
    """dummy development page"""
    return render_template("aboutus.html")

@app.route("/how-learning-works")
def go_learning():
    """dummy development page"""
    return render_template("learningworks.html")

@app.route("/courses")
def go_courses():
    """dummy development page"""
    cat_details = Category.query.order_by(Category.cat_no).all()
    
    return render_template("courses.html", cat_details=cat_details)

@app.route("/request-info")
def request_info():
    """dummy development page"""
    return render_template("request_info.html")

@app.route("/go-enroll")
def go_enroll():
    """dummy development page"""
    return render_template("coming_soon.html")

@app.route("/coming-soon")
def coming_soon():
    """dummy development page"""
    return render_template("coming_soon.html")

