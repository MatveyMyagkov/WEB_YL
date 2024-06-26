from flask import Flask, render_template
from flask_login import LoginManager
from data import db_session
from data.__all_models import User
from views import users, navigator, game, api
from data.utils import load_cards


app = Flask(__name__)
app.config.from_pyfile('config.cfg')
if 'SECURITY_PASSWORD_SALT' not in app.config:
    app.config['SECURITY_PASSWORD_SALT'] = app.config['SECRET_KEY']
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id: int) -> User:
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/')
@app.route('/index')
def root() -> str:
    param = {
        'title': "Navigator in IT",
    }
    return render_template('Navigator/main.html', **param)


def main() -> None:
    db_session.global_init("db/db.db")
    load_cards("data/cards.json")
    app.register_blueprint(users.blueprint)
    app.register_blueprint(navigator.blueprint)
    app.register_blueprint(game.blueprint)
    app.register_blueprint(api.blueprint)
    app.run(host='127.0.0.1', port=5000)


if __name__ == '__main__':
    main()
