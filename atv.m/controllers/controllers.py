from flask import Blueprint, render_template
from models.models import personagens  

personagens_de = Blueprint('personagens', __name__)

@personagens_de.route('/')
def index():
    
    return render_template('index.html', personagens=personagens)
