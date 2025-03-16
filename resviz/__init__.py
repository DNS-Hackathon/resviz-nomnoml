import click
import json
from flask import Flask


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('application.cfg', silent=True)

    prefix = app.config.get('PREFIX', '')
    app.url_map = app.url_map_class()
    app.static_url_path = prefix + '/static'
    app.add_url_rule(
        app.static_url_path + '/<path:filename>',
        endpoint='my_static',
        view_func=app.send_static_file,
    )

    from resviz.views import main
    app.register_blueprint(main.bp, url_prefix=prefix+main.bp.url_prefix)

    return app
