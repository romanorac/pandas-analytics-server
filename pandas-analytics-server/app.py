import logging
import uuid
from os import path

import matplotlib
from flask import Flask, render_template, request

import logging_conf
from data_service import data_service
from strategy_service import strategy_service

matplotlib.use("agg")

logger = logging.getLogger()
ds = None
ss = None


def init_services():
    global ds, ss

    ds = data_service.DataService()
    ds.start()
    ss = strategy_service.StrategyService(data_service=ds)
    ss.start()


def create_app():
    app = Flask(__name__)
    logging_conf.init_logging()
    init_services()
    return app


app = create_app()


@app.route('/')
def index():
    return 'Hellow Sir! I am ready to serve.'


@app.route('/plot')
def plot():
    logger.info('Rendering plot')
    n_entries = request.args.get('n_entries', default=50, type=int)
    n_entries = n_entries if 1 < n_entries <= 50 else 50

    image_name = str(uuid.uuid4()) + '.png'
    image_filepath = path.join('static', 'images', image_name)

    fig = ss.plot(n_entries)
    if not fig:
        return 'Data is not synced yet'
    fig.savefig(image_filepath)
    return render_template('plot.html', name='Plot', url=image_filepath)


if __name__ == '__main__':
    app.run(debug=False)
