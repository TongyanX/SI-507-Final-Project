# -*- coding: utf-8 -*-
"""Set up Server"""

import os
import webbrowser
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


@app.route('/table/<t_type>')
def table_data(t_type):
    """Table Page - University"""
    return render_template('table_data.html', type=t_type)


@app.route('/plot/')
def plot():
    """Plot Page"""
    plot_list = [
        dict(type='Bar plot', topic='State University', img='bar.png', func='bar', index=1,
             desc='To see top 10, 15, 20 states with highest amount of national universities.'),
        dict(type='Line plot', topic='State GDP', img='line.png', func='line', index=2,
             desc='To see GDP time trends (from 1997 to 2016) of all your interested states together. '
                  'Better within 20 states.'),
        dict(type='Histogram', topic='Tuition Difference', img='histo.png', func='histogram_plot', index=3,
             desc='To see discrimination of tuition and fees in public universities '
                  'for in-state and out-of-state students.'),
        dict(type='Bubble plot', topic='University vs GDP', img='bubble.png', func='bubble', index=4,
             desc='To see relationship between university amount and GDP value. '
                  'You can also add some other features.'),
        dict(type='Scatter plot', topic='Public vs Private', img='scatter.png', func='scatter', index=5,
             desc='To see differences between public and private universities. '
                  'You can choose features whatever you like.'),
        dict(type='Map Plot', topic='University Location', img='map.png', func='map', index=6,
             desc='To see a map including all universities in your interested state '
                  '(mapbox API key is required).')
    ]
    return render_template('plot.html', plot_list=plot_list)


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
    base_dir = os.path.dirname(os.path.abspath(__file__))
    with open(base_dir + '/requirements.txt') as r:
        module_list = [m.split('==')[0].lower() for m in r.readlines()]

    from pip import get_installed_distributions as gid

    module_list_exist = [m.key for m in gid()]
    print(module_list_exist)

    module_list_required = sorted(list(set(module_list) - set(module_list_exist)))

    for m in module_list_required:
        while True:
            command = input('Module <{}> is not found. Would you like to pip install it? (y/n) '.format(m))
            if command not in ['y', 'n']:
                print('Invalid Input.')
            else:
                break
        if command == 'y':
            os.system('pip3 install {}'.format(m))
        else:
            print('\n * Failed to run the project.\n')
            exit()

    print(' * All required modules are found. Try running the project...')
    plotly_setup()
    webbrowser.open('http://127.0.0.1:5000/')
    app.run()
