#!/usr/bin/env python3
"""Flask app which is basic."""
from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def find_index() -> str:
    """Index page for the home."""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
