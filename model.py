from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
import datetime

db = SQLAlchemy()

def connect_to_db(flask_app, dbname='kamusta_psql', echo=False):  
    
    #organization info
    flask_app.config['ORG_NAME'] = 'Kamusta Kids'
    flask_app.config['APP_TITLE'] = 'Website & System'
    flask_app.config['APP_DESC'] = 'Kamusta Kids external website and internal administrative system'

    #database
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql:///' + dbname
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    #Flask-Admin config
    flask_app.config['DEBUG'] = True
    flask_app.config['HOST'] = 'localhost'
    flask_app.config['PORT'] = 8000
    
    db.app = flask_app
    db.init_app(flask_app)
    
    print('Connected to the db!')

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Helper Functions
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                    # def sku_get_intake_quantity(sku):
                    #     """quantity from intake"""

                    #     return Intake.query.filter(Intake.sku == sku).first()

                    # def sku_get_sale_quantity(sku):
                    #     """add quantity of all sales"""
                        
                    #     items_with_sku = Item.query.filter(Item.sku == sku).all()
                    #     return_data = {"quantity_total": 0, "sale_records":[]}
                        
                    #     for item in items_with_sku:
                    #         return_data["quantity_total"] += item.quantity
                    #         return_data["sale_records"].append(item)
                            
                    #     return return_data     

                    # def sku_get_sample_quantity(sku):   
                    #     """add quantity of all samples out"""
                        
                    #     sampleitems_with_sku = SampleItem.query.filter(SampleItem.sku == sku).all()
                    #     return_data = {"sampleout":{"quantity_total": 0, "sample_records":[]}, "returned": {"quantity_total": 0, "sample_records":[]}}
                        
                    #     for sampleitem in sampleitems_with_sku:
                            
                    #         sample_record = Sample.query.filter(Sample.id == sampleitem.sale_id).first()
                    #         if sample_record.movement == "sampleout":
                    #             return_data["sampleout"]["quantity_total"] += sampleitem.quantity
                    #             return_data["sampleout"]["sample_records"].append(sampleitem.id)
                    #         if sample_record.movement == "samplereturn":
                    #             return_data["returned"]["quantity_total"] += sampleitem.quantity
                    #             return_data["returned"]["sample_records"].append(sampleitem.id)

                    #     return return_data  

                    # def calculate_quantity_instock(sku):
                    #     """quantity left = intake minus sales, minus samples out, add sample returned"""

                    #     quant_intake = sku_get_intake_quantity(sku)
                    #     quant_sold = sku_get_sale_quantity(sku)
                    #     quant_dict = sku_get_sample_quantity(sku)
                    #     quant_sample_out = quant_dict["sampleout"]
                    #     quant_sample_returned = quant_dict["returned"]
                        
                    #     quant_instock = quant_intake - quant_sold["quantity_total"] - quant_sample_out["quantity_total"] + quant_sample_returned["quantity_total"]
                        
                    #     return quant_instock

                    # # By Product ~~~~~~~~~~~~~~

                    # def prod_get_intake_quantity(product_id):
                    #     """all intake with given product id"""
                        
                    #     intake_quant = 0
                    #     intake_with_id = Intake.query.filter(Intake.product_id == product_id).all()
                        
                    #     for intake in intake_with_id:
                    #             intake_quant += intake.quantity
                        
                    #     return intake_quant
                    
                    # def prod_get_sale_quantity(product_id):
                    #     """from sales - add quantity with given product id"""

                    #     sale_quant = 0
                    #     items_with_id = Item.query.filter(Item.product_id == product_id).all()
                        
                    #     for item in items_with_id:
                    #             sale_quant += item.quantity
                        
                    #     return sale_quant
                        
                    # def prod_get_sample_quantity(product_id): 
                    #     """from samples - add quantity with given product id"""

                    #     sampleitems_with_id = SampleItem.query.filter(SampleItem.product_id == product_id).all()
                    #     return_data = {"sampleout":{"quantity_total": 0, "sample_records":[]}, "returned": {"quantity_total": 0, "sample_records":[]}}
                        
                    #     for sampleitem in sampleitems_with_id:
                            
                    #         sample_record = Sample.query.filter(Sale.id == sampleitem.sale_id).first()
                    #         if sample_record.movement == "sampleout":
                    #             return_data["sampleout"]["quantity_total"] += sampleitem.quantity
                    #             return_data["sampleout"]["sample_records"].append(sampleitem.sample_record_id)
                    #         if sample_record.movement == "samplereturn":
                    #             return_data["returned"]["quantity_total"] += sampleitem.quantity
                    #             return_data["returned"]["sample_records"].append(sampleitem.sample_record_id)

                    #     return return_data  

                    # def prod_calculate_quantity_instock(product_id):
                    #     """quantity left = intake minus sales, minus samples out, add sample returned"""

                    #     quant_intake = prod_get_intake_quantity(product_id)
                    #     quant_sold = prod_get_sale_quantity(product_id)
                    #     quant_dict = prod_get_sample_quantity(product_id)
                    #     quant_sample_out = quant_dict["sampleout"]
                    #     quant_sample_returned = quant_dict["returned"]
                        
                    #     quant_instock = quant_intake - quant_sold["quantity_total"] - quant_sample_out["quantity_total"] + quant_sample_returned["quantity_total"]
                        
                    #     return quant_instock


                    # # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~           
                    # # Money Calculations
                    # # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                    # # Item Instance Calc ~~~~~~~~~~~~~~

                    # def calc_sub_total(quantity, item_instance):
                        
                    #     prem_disc = item_instance.sale.prem_disc_percentage
                    #     prem_disc = (100 + prem_disc) / 100
                    #     new_price = item_instance.intake_instance.selling_price *  prem_disc
                        
                    #     print("premium or discount: ", prem_disc)
                    #     print("quantity: ", quantity)
                    #     print("new price per item: ", new_price)
                        
                    #     sub_total = quantity * new_price

                    #     print("subtotal: ", sub_total)

                    #     return sub_total

                    # def calc_cogs(quantity, item_instance):
                        
                    #     cost_per_unit = item_instance.intake_instance.cost_per_unit
                    #     licensing_per_unit = item_instance.intake_instance.licensing_fee
                        
                    #     cogs_of_item = quantity * (cost_per_unit + licensing_per_unit)
                        
                    #     return cogs_of_item


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# People models
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
class Category(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    cat_no = db.Column(db.String(3), unique=True, nullable=False)
    cat_name = db.Column(db.String(45), unique=True)
    pre_req = db.Column(db.Text, unique=True)
    
    #--relationship--#
    courses = db.relationship("Course", backref="category")
    
    def __repr__(self):
        return f'< Order = {self.cat_no} User = {self.cat_name} >'

    def __init__(self, cat_no, cat_name, pre_req="None"):
        self.cat_name, self.cat_no, self.pre_req = (cat_name, int(cat_no), pre_req)

class Course(db.Model):
    """An staff member."""
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    course_no = db.Column(db.String(3), unique=True, nullable=False)
    course_name = db.Column(db.String(150), unique=True, nullable=False)
    description = db.Column(db.Text, unique=True, nullable=False)
    registration_link = db.Column(db.String, nullable=False)
    category_id = db.Column(db.Integer(), db.ForeignKey(Category.id))
    image_url = db.Column(db.String, nullable=False)


    def __repr__(self):
        return f'< Level = {self.course_name} >'

    def __init__(self, course_no, course_name, category_id, registration_link="N/A", description="N/A", image_url="https://i.ibb.co/K0Rm9fW/Screen-Shot-2021-12-07-at-2-03-56-PM.png"):
        
        self.course_no, self.course_name, self.category_id, self.registration_link, self.description, self.image_url= (int(course_no), course_name, int(category_id), registration_link, description, image_url)
    
if __name__ == '__main__':
    from app import app
    
    connect_to_db(app)
    Bootstrap(app)
    
    db.create_all()
    db.session.commit()
            
            