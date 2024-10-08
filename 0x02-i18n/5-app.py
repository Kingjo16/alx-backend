#!/usr/bin/env python3
"""A Flask app with mock user login."""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """Configuration for Babel and Flask app."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


def get_user():
    """Retrieve the user based on the login_as parameter."""
    try:
        user_id = int(request.args.get("login_as"))
        return users.get(user_id)
    except (ValueError, TypeError):
        return None


@app.before_request
def before_request():
    """Set the current user in the global object if any."""
    g.user = get_user()


@babel.localeselector
def get_locale():
    """Determine the best match for supported languages or use the URL parameter."""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    if g.user and g.user.get("locale") in app.config['LANGUAGES']:
        return g.user.get("locale")
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """The home/index page."""
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
