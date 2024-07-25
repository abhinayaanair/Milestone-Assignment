from flask import Flask, Blueprint

app = Flask(__name__)

# Create a Blueprint
simple_page = Blueprint('simple_page', __name__)

@simple_page.route('/')
def home():
    return 'This is a Blueprint route!'

# Register the Blueprint
app.register_blueprint(simple_page)

if __name__ == "__main__":
    app.run(debug=True)