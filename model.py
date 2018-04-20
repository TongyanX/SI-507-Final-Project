# -*- coding: utf-8 -*-
"""Database Operations"""

import sqlite3
import os


class Database(object):
    """Database Operator"""
    def __init__(self):
        self.db_name = 'National_University.sqlite'
        self.db_dir = os.path.dirname(os.path.abspath(__file__)) + '/project/database/'
        self.con = sqlite3.connect(self.db_dir + self.db_name)
        self.cur = self.con.cursor()
        self.translate_dict = {
            'Total Endowment (Million)': 'SUM([Endowment(M)])',
            'Average Endowment (Million)': 'AVG([Endowment(M)])',
            'Total Enrollment': 'SUM(Enrollment)',
            'Average Enrollment': 'AVG(Enrollment)',
            'Average Tuition in State': 'AVG(TuitionAndFeesInState)',
            'Average Tuition out of State': 'AVG(TuitionAndFeesOutOfState)',
            'Average Median Starting Salary': 'AVG(MedianStartingSalary)',
            'Average Student Faculty Ratio': 'AVG(StudentFacultyRatio)',
            'Average Female Percentage': 'AVG(FemalePercentage)',
            'Tuition Difference': 'TuitionAndFeesOutOfState - TuitionAndFeesInState'
        }

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.con.close()

    def check_database(self):
        """Check if Database is Complete"""
        if not self.check_table('State_Abbr'):
            from project.scripts import stateAbbrData
            stateAbbrData.main()

        if not self.check_table('National_University'):
            from project.scripts import universityData
            universityData.main()

        if not self.check_table('GDP_State'):
            from project.scripts import gdpData
            gdpData.main()

    def create_table(self, table_dict):
        """Create Table to Store Data"""
        t_name = table_dict['name']

        statement = 'DROP TABLE IF EXISTS {}'.format(t_name)
        self.cur.execute(statement)

        col_list = table_dict['column']
        col_name = [col[0] for col in col_list]
        col_type = [col[1] for col in col_list]
        statement = 'CREATE TABLE IF NOT EXISTS {} ('.format(t_name)
        for i in range(len(col_list)):
            statement += '\'{}\' {}, '.format(col_name[i], col_type[i])
            if table_dict.get('key', None) == col_name[i]:
                statement = statement[0:-2] + ' PRIMARY KEY AUTOINCREMENT, '

        statement = statement[:-2] + ')'

        self.cur.execute(statement)
        self.con.commit()

    def insert_data(self, data_list, statement):
        """Insert Data Tuples to a Given Table"""
        for data in data_list:
            self.cur.execute(statement, data)

        self.con.commit()

    def check_table(self, t_name):
        """Check If a Table Exists"""
        statement = 'SELECT name FROM sqlite_master WHERE type = \'table\' AND name = \'{}\''.format(t_name)
        self.cur.execute(statement)

        if self.cur.fetchone() is not None:
            return True
        else:
            return False

    def get_university_count(self, limit=20):
        """List States with Most National Universities"""
        statement = '''
                        SELECT s.StateName, COUNT(n.Id) FROM National_University AS n 
                        JOIN State_Abbr AS s 
                            ON n.StateId = s.Id 
                        GROUP BY n.StateId 
                        ORDER BY COUNT(n.ID) DESC 
                        LIMIT {}
                    '''.format(limit)
        self.cur.execute(statement)
        result_list = self.cur.fetchall()
        return result_list

    def get_university_gdp(self, additional_variable='Total Endowment'):
        """List Relationship between National University Amount and GDP"""
        arg = self.translate_dict[additional_variable]
        statement = '''
                        SELECT s.StateAbbr, s.StateName, COUNT(n.Id), g.Y2016, {} FROM National_University AS n 
                        JOIN State_Abbr AS s 
                            ON n.StateId = s.Id
                        JOIN GDP_State AS g 
                            ON s.Id = g.StateId
                        GROUP BY n.StateId
                    '''.format(arg)
        print(statement)
        self.cur.execute(statement)
        result_list = self.cur.fetchall()
        return result_list

    def get_public_private(self, x_axis='Enrollment', y_axis='MedianStaringSalary'):
        """Get Data to Show Difference between Public and Private National Universities"""
        if x_axis == 'Tuition Difference':
            x_axis = self.translate_dict[x_axis]
        elif x_axis == 'Endowment(M)':
            x_axis = '[Endowment(M)]'
        if y_axis == 'Tuition Difference':
            y_axis = self.translate_dict[y_axis]
        elif y_axis == 'Endowment(M)':
            y_axis = '[Endowment(M)]'

        statement = '''
                        SELECT {}, {}, Type, Name FROM National_University
                        WHERE {} IS NOT NULL AND {} IS NOT NULL
                    '''.format(x_axis, y_axis, x_axis, y_axis)
        self.cur.execute(statement)
        result_list = self.cur.fetchall()
        return result_list

    def get_state_gdp(self, state_abbr):
        """Get Historical GDP Data of A State"""
        statement = '''
                        SELECT s.StateName, g.Y1997, g.Y1998, g.Y1999, g.Y2000, g.Y2001, g.Y2002, g.Y2003, g.Y2004, 
                               g.Y2005, g.Y2006, g.Y2007, g.Y2008, g.Y2009, g.Y2010, g.Y2011, g.Y2012, g.Y2013, 
                               g.Y2014, g.Y2015, g.Y2016 FROM GDP_State AS g 
                        JOIN State_Abbr AS s 
                            ON g.StateId = s.Id
                        WHERE s.StateAbbr = \'{}\'
                    '''.format(state_abbr)
        self.cur.execute(statement)
        result = self.cur.fetchone()
        return result

    def get_gps_data(self, state_abbr):
        """Get GPS Data for All National Universities within A State"""
        statement = '''
                        SELECT n.Name, n.Latitude, n.Longitude FROM National_University AS n 
                        JOIN State_Abbr AS s 
                            ON n.StateId = s.Id
                        WHERE s.StateAbbr = \'{}\'
                    '''.format(state_abbr)
        self.cur.execute(statement)
        result_list = self.cur.fetchall()
        return result_list

    def get_tuition_difference(self):
        """Get Difference between In-State and Out-of-State Tuition and Fees of Public Universities"""
        statement = '''
                        SELECT TuitionAndFeesOutOfState - TuitionAndFeesInState FROM National_University
                        WHERE Type = 'Public'
                    '''
        self.cur.execute(statement)
        result_list = self.cur.fetchall()
        result_list = [result[0] for result in result_list if result[0] is not None]
        return result_list

    def get_state_univ(self, state_abbr):
        """Get All National Universities within A State"""
        statement = '''
                        SELECT n.Id, n.Name, n.Ranking, s.StateAbbr, n.City, n.Type, n.FoundYear, n.[Endowment(M)], 
                               n.TuitionAndFeesInState, n.TuitionAndFeesOutOfState, n.Enrollment, 
                               n.MedianStartingSalary, n.StudentFacultyRatio, n.FemalePercentage, 
                               n.Latitude, n.Longitude FROM National_University AS n 
                        JOIN State_Abbr AS s 
                            ON n.StateId = s.Id
                        WHERE s.StateAbbr = \'{}\' 
                    '''.format(state_abbr)
        self.cur.execute(statement)
        result_list = self.cur.fetchall()
        return result_list
