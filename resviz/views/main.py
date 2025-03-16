from flask import Blueprint, render_template, jsonify, current_app
import subprocess
import json

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/dig/<dn>')
def dig(dn):
    current_app.logger.info(dn)
    try:
        dig = subprocess.run(['dig', '+trace', '+all', dn], capture_output=True).stdout
        current_app.logger.info(dig)
        jc = subprocess.run(['jc', '--dig'], input=dig, capture_output=True).stdout
        current_app.logger.info(jc)
        j = json.loads(jc)
        return jsonify(j)
    except Exception as e:
        current_app.logger.error(e)

    return jsonify({})