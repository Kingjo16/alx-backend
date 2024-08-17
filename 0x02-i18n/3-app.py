#!/usr/bin/env python3
"""A Flask app with Babel and template translation."""
from flask import Flask, render_template
from flask_babel import Babel, _


class Config:
    """Configuration for Babel and Flask app."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)

@babel.localeselector
def get_locale() -> str:
    """Determine the best match for supported languages."""
    return request.accept_languages.best_match(app.config["LANGUAGES"])

@app.route('/')
def find_index() -> str:
    """The home/index page."""
    return render_template('3-index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
