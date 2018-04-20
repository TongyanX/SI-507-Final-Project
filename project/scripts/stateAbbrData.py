# -*- coding: utf-8 -*-
"""Request and Store of State Abbreviation Data"""

import json
import os

from model import Database

# Data Source:
# https://gist.githubusercontent.com/mshafrir/2646763/raw/8b0dbb93521f5d6889502305335104218454c2bf/states_hash.json
f_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/rawData/'
f_name = 'state_abbr.json'


def get_state_abbr_data():
    """Get State Abbreviations from JSON File"""
    with open(f_dir + f_name) as f:
        data_dict = json.loads(f.read())

    return data_dict


def state_abbr_table():
    """Initialize State Abbreviation Table"""
    t_name = 'State_Abbr'

    data_dict = get_state_abbr_data()
    data_dict['DC'] = 'District of Columbia'

    table_dict = dict(name=t_name,
                      column=[('Id', 'INTEGER'),
                              ('StateAbbr', 'TEXT'),
                              ('StateName', 'TEXT')],
                      key='Id')

    statement = 'INSERT INTO {} VALUES (NULL, ?, ?)'.format(t_name)

    with Database() as db_operator:
        db_operator.create_table(table_dict)
        db_operator.insert_data(list(data_dict.items()), statement)


def main():
    """Main Function to Initialize State Abbreviation Table"""
    state_abbr_table()


if __name__ == '__main__':
    main()
