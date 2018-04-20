# -*- coding: utf-8 -*-
"""Request and Store of State Abbreviation Data"""

import unittest


class TestDataRequest(unittest.TestCase):
    """Test Case to Test Data Request Functions"""

    def test_get_national_university_data(self):
        """Test Function <get_national_university_data>"""
        from project.scripts.universityData import get_national_university_data
        univ_dict = get_national_university_data('/best-colleges/university-of-michigan-9092')

        self.assertEqual(univ_dict.get('name'), 'University of Michigan--Ann Arbor')
        self.assertEqual(univ_dict.get('ranking'), '28')
        self.assertEqual(univ_dict.get('state'), 'MI')
        self.assertEqual(univ_dict.get('city'), 'Ann Arbor')
        self.assertEqual(univ_dict.get('type'), 'Public')
        self.assertEqual(univ_dict.get('found_year'), 1817)
        self.assertEqual(univ_dict.get('endowment'), 9600)
        self.assertEqual(univ_dict.get('tuition_in_state'), 14826)
        self.assertEqual(univ_dict.get('tuition_out_state'), 47476)
        self.assertEqual(univ_dict.get('enrollment'), 44718)
        self.assertEqual(univ_dict.get('median_salary'), 58400)
        self.assertEqual(univ_dict.get('student_faculty'), 15)
        self.assertEqual(univ_dict.get('female'), 0.502)

    def test_get_national_university_page(self):
        """Test Function <get_national_university_page>"""
        from project.scripts.universityData import get_national_university_page
        univ_list = get_national_university_page(1)

        self.assertEqual(len(univ_list), 20)
        self.assertIsInstance(univ_list[0], dict)
        self.assertEqual(univ_list[0].get('name'), 'Princeton University')
        self.assertEqual(univ_list[1].get('ranking'), '2')

    def test_get_gdp_data(self):
        """Test Function <get_gdp_data>"""
        from project.scripts.gdpData import get_gdp_data
        column_name, column_data = get_gdp_data()

        self.assertEqual(len(column_name), 21)
        self.assertEqual(column_name[0], 'Area')
        self.assertEqual(column_name[1], 'Y1997')
        self.assertEqual(column_name[-1], 'Y2016')
        self.assertEqual(column_data[2][0], 'Alaska')
        self.assertEqual(column_data[2][2], '24030')
        self.assertEqual(column_data[5][1], '1081444')

    def test_get_state_abbr_data(self):
        """Test Function <get_state_abbr_data>"""
        from project.scripts.stateAbbrData import get_state_abbr_data
        state_dict = get_state_abbr_data()

        self.assertEqual(state_dict['MI'], 'Michigan')
        self.assertEqual(state_dict['CA'], 'California')


class TestNationalUniversity(unittest.TestCase):
    """Test Case to Test Class Definitions"""

    def setUp(self):
        """Create Testing Objects"""
        from project.scripts.universityData import get_national_university_data
        univ_dict = get_national_university_data('/best-colleges/university-of-michigan-9092')
        from project.scripts.classDef import NationalUniversity
        self.nu_obj1 = NationalUniversity(data_dict=univ_dict)
        self.nu_obj2 = NationalUniversity(name='University of California--Los Angeles', city='Los Angeles', state='CA')

    def test_attr_1(self):
        """Test Object 1's Variables' Values"""
        self.assertEqual(self.nu_obj1.name, 'University of Michigan--Ann Arbor')
        self.assertEqual(self.nu_obj1.ranking, '28')
        self.assertEqual(self.nu_obj1.state, 'MI')
        self.assertEqual(self.nu_obj1.city, 'Ann Arbor')
        self.assertEqual(self.nu_obj1.type, 'Public')
        self.assertEqual(self.nu_obj1.found_year, 1817)
        self.assertEqual(self.nu_obj1.endowment, 9600)
        self.assertEqual(self.nu_obj1.tuition_in_state, 14826)
        self.assertEqual(self.nu_obj1.tuition_out_state, 47476)
        self.assertEqual(self.nu_obj1.enrollment, 44718)
        self.assertEqual(self.nu_obj1.median_salary, 58400)
        self.assertEqual(self.nu_obj1.student_faculty, 15)
        self.assertEqual(self.nu_obj1.female, 0.502)
        self.assertEqual(self.nu_obj1.lat, 42.2850942)
        self.assertEqual(self.nu_obj1.lng, -83.73855669999999)

    def test_attr_2(self):
        """Test Object 1's Variables' Values"""
        self.assertEqual(self.nu_obj2.name, 'University of California--Los Angeles')
        self.assertEqual(self.nu_obj2.state, 'CA')
        self.assertEqual(self.nu_obj2.city, 'Los Angeles')
        self.assertEqual(self.nu_obj2.lat, 34.054276)
        self.assertEqual(self.nu_obj2.lng, -118.255787)


class TestDatabaseOperation(unittest.TestCase):
    """Test Case to Test Methods of Class Database Defined in dbOperation"""

    def setUp(self):
        """Generate Database Operator"""
        from model import Database
        self.db = Database()

    def test_exiting_table(self):
        """Test Existing Tables to Check <create_table>, <insert_data>, and <check_table> Methods"""
        statement = '''
                        SELECT * FROM National_University 
                        WHERE Name = 'University of Michigan--Ann Arbor' 
                    '''
        try:
            self.db.cur.execute(statement)
            result = self.db.cur.fetchall()
            self.assertEqual(len(result), 1)
            self.assertEqual(result[0][0], 28)
            self.assertEqual(result[0][4], 'Ann Arbor')
        except Exception:
            self.fail()

        statement = '''
                        SELECT * FROM GDP_State 
                        WHERE StateId = 27 
                    '''
        try:
            self.db.cur.execute(statement)
            result = self.db.cur.fetchall()
            self.assertEqual(len(result), 1)
            self.assertEqual(result[0][1], 302803)
        except Exception:
            self.fail()

        statement = '''
                        SELECT * FROM State_Abbr 
                        WHERE StateName = 'Michigan' 
                    '''
        try:
            self.db.cur.execute(statement)
            result = self.db.cur.fetchall()
            self.assertEqual(len(result), 1)
            self.assertEqual(result[0][1], 'MI')
        except Exception:
            self.fail()

    # def test_method(self):
    #     """Test Database Operator's Other Methods"""
    #     pass


if __name__ == '__main__':
    unittest.main()
