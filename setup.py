# -*- coding: utf-8 -*-
"""Plotting Functions"""

from flask import Flask, request, render_template
from project.scripts.tableFunc import *
from project.scripts.plotFunc import *

app = Flask(__name__)


@app.route('/')
def index():
    """Index Page"""
    return render_template('index.html')


@app.route('/table/')
def table():
    """Table Page"""
    return render_template('table.html')


@app.route('/table/univ/')
def table_univ():
    """Table Page - University"""
    return render_template('table_univ.html')


@app.route('/table/gdp/')
def table_gdp():
    """Table Page - GDP"""
    return render_template('table_gdp.html')


@app.route('/plot/')
def plot():
    """Plot Page"""
    return render_template('plot.html')


@app.route('/univ/', methods=['GET', 'POST'])
def univ():
    """University Table"""
    state_list = request.args.get('state', '').split(',')
    return state_univ(state_list)


@app.route('/gdp/', methods=['GET', 'POST'])
def gdp():
    """GDP Table"""
    state_list = request.args.get('state', '').split(',')
    return state_gdp(state_list)


@app.route('/plot/bar/', methods=['GET', 'POST'])
def bar():
    """Bar Plot"""
    limit = int(request.args.get('limit', '0'))
    return bar_state_univ(limit=limit)


@app.route('/plot/line/', methods=['GET', 'POST'])
def line():
    """Line Plot"""
    state_list = request.args.get('state', '').split(',')
    return line_gdp(abbr_list=state_list)


@app.route('/plot/histogram/', methods=['GET', 'POST'])
def histogram():
    """Histogram Plot"""
    return histogram_difference_tuition()


@app.route('/plot/bubble/', methods=['GET', 'POST'])
def bubble():
    """Bubble Plot"""
    add_param = request.args.get('add_param', '')
    return scatter_university_gdp(input_phrase=add_param)


@app.route('/plot/scatter/', methods=['GET', 'POST'])
def scatter():
    """Scatter Plot"""
    cor = request.args.get('cor', ',')
    x_axis = cor.split(',')[0]
    y_axis = cor.split(',')[1]
    return scatter_public_private(x_axis=x_axis, y_axis=y_axis)


@app.route('/plot/map/', methods=['GET', 'POST'])
def mapbox():
    """Map Plot"""
    state = request.args.get('state', '')
    return mapbox_univ(state_abbr=state)


if __name__ == '__main__':
    app.run(debug=True)
