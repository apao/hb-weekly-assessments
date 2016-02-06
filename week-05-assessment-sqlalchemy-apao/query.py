"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Start here.


# Part 2: Write queries

# Get the brand with the **id** of 8.
brand_id_8 = Brand.query.get(8)

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
Chev_Corv_models = Model.query.filter(Model.brand_name=="Chevrolet", Model.name=="Corvette").all()

# Get all models that are older than 1960.
models_older_than_1960 = Model.query.filter(Model.year < 1960).all()

# Get all brands that were founded after 1920.
brands_founded_after_1920 = Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor".
models_begw_cor = Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands with that were founded in 1903 and that are not yet discontinued.
brand_1903_not_disc = Brand.query.filter(Brand.founded==1903, Brand.discontinued==None).all()

# Get all brands with that are either discontinued or founded before 1950.
brands_disc_or_before_1950 = Brand.query.filter((Brand.discontinued.isnot(None)) | (Brand.founded < 1950)).all()

# Get any model whose brand_name is not Chevrolet.
models_not_chevrolet = Model.query.filter(Model.brand_name != "Chevrolet").all()

# Fill in the following functions. (See directions for more info.)

def get_model_info(model_year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    models = db.session.query(Model.name,
                              Model.brand_name,
                              Brand.headquarters).join(Brand, Model.brand_name==Brand.name).filter(Model.year==model_year).all()

    for model_name, brand_name, brand_hq in models:
        print "Model: %s, Brand: %s, Brand HQ: %s" % (model_name, brand_name, brand_hq)


def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    brand_and_models = db.session.query(Brand.name,
                                        Model.name, Model.year).join(Model, Brand.name==Model.brand_name).all()

    for brand_name, model_name, model_year in brand_and_models:
        print "Brand: %s, Model: %s, Year: %s" % (brand_name, model_name, model_year)


# -------------------------------------------------------------------


# Part 2.5: Advanced and Optional
def search_brands_by_name(mystr):
    """Prints out the brand name that matches or most closely matches the user input."""

    brands_by_keyword = db.session.query(Brand.name).filter(Brand.name.like("%" + mystr + "%")).all()

    for brand_name in brands_by_keyword:
        print "Brand: %s" % (brand_name) 


def get_models_between(start_year, end_year):
    """Prints out all models with their brand name and model year between given start and end years."""

    models_between_years = db.session.query(Model.name, Model.year, Model.brand_name).filter(Model.year < end_year, Model.year > start_year).order_by(Model.year).all()

    for model_name, model_year, model_brand in models_between_years:
        print "Model: %s, Year: %s, Brand: %s" % (model_name, model_year, model_brand)

# -------------------------------------------------------------------

# Part 3: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?
# ANSWER: Flask_SQLAlchemy Query Object that queries where the name of the brand is "Ford".


# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?
# ANSWER: An association table is a table that sits between and connects two tables, generally
# featurings a one-two-many/many-to-one relationship with each of those two tables.

