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
brand_with_id_8 = Brand.query.get(8)
print brand_with_id_8

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
models_name_corvette = Model.query.filter(Model.name == 'Corvette', Model.brand_name == 'Chevrolet').all()
print models_name_corvette

# Get all models that are older than 1960.
models_older_1960 = Model.query.filter(Model.year < 1960).all()
print models_older_1960

# Get all brands that were founded after 1920.
brands_after_1920 = Brand.query.filter(Brand.founded > 1920).all()
print brands_after_1920

# Get all models with names that begin with "Cor".
models_begin_cor = Model.query.filter(Model.name.like('%Cor%')).all()
print models_begin_cor

# Get all brands with that were founded in 1903 and that are not yet discontinued.
brands_founded_1903_not_disc = Brand.query.filter(Brand.founded == 1903, Brand.discontinued == None).all()
print brands_founded_1903_not_disc

# Get all brands with that are either discontinued or founded before 1950.
brands_disc_founded_before_1950 = Brand.query.filter( (Brand.discontinued != None) | (Brand.founded < 1950)).all()
print brands_disc_founded_before_1950

# Get any model whose brand_name is not Chevrolet.
models_not_chevrolet = Model.query.filter( ~ Model.brand_name.in_(['Chevrolet']) ).all()
print models_not_chevrolet

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    model_info = db.session.query.filter(Model.year, Model.brand_name, Brand.headquarters).all()
    print model_info

def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    pass

# -------------------------------------------------------------------


# Part 2.5: Advanced and Optional
def search_brands_by_name(mystr):
    pass


def get_models_between(start_year, end_year):
    pass

# -------------------------------------------------------------------

# Part 3: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?
# <flask_sqlalchemy.BaseQuery object at 0x107da8150>

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?
# An association table that is created and used to connect multiple tables in a database with many-to-many relationships. The associative table 
#is able to map two or more tables together by referencing their Primary Keys. It may also reference other foreign keys, which connect to
#to other individual tables in a many-to-one relationship.
