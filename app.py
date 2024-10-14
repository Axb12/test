from flask import Flask

from controllers import bp
from settings import settings

def register_blueprints(app: Flask):
    app.register_blueprint(bp)

def create_app() -> Flask:
    app = Flask(__name__)
    register_blueprints(app)
    return app


app = create_app()

@app.route('/')
def hello():
    return "Hello World!"

def run():
    app.run(debug=settings.DEBUG)

if __name__ == '__main__':
    run()
