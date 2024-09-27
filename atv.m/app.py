from flask import Flask
from controllers.controllers import personagens_de  

app = Flask(__name__)


app.register_blueprint(personagens_de)

if __name__ == '__main__':
    app.run(debug=True)
