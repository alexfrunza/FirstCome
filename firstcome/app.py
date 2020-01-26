import flask

from data import mongo_setup

app = flask.Flask(__name__)


def setup_db():
    mongo_setup.global_init()


def register_blueprints():
    from firstcome.views import home_views
    from firstcome.views import users_views

    app.register_blueprint(home_views.blueprint)
    app.register_blueprint(users_views.blueprint)


def main():
    register_blueprints()
    app.run(debug=True)


setup_db()
register_blueprints()
if __name__ == '__main__':
    setup_db()
    main()
