import pytest
from pyredactkit.core_redactor import CoreRedactorEngine

data = """John, please get that article on www.linkedin.com to me by 5:00PM on Jan 9th 2012. 4:00 would be ideal, actually. If you have any questions, You can reach me at(519)-236-2723 or get in touch with my associate at harold.smith@gmail.com
this is my IP: 102.23.5.1
My router is : 10.10.10.1
71.159.188.33
81.141.167.45
165.65.59.139
64.248.67.225

https://tech.gov.sg

My email is harold@mail.com

this is my IP: 102.23.5.1
My router is: 10.10.10.1
71.159.188.33
81.141.167.45
165.65.59.139
64.248.67.225

Card_Number,Card_Family,Credit_Limit,Cust_ID
8638-5407-3631-8196,Premium,530000,CC67088
7106-4239-7093-1515,Gold,18000,CC12076
6492-5655-8241-3530,Premium,596000,CC97173
2868-5606-5152-5706,Gold,27000,CC55858
1438-6906-2509-8219,Platinum,142000,CC90518
2764-7023-8396-5255,Gold,50000,CC49168
4864-7119-5608-7611,Premium,781000,CC66746
5160-8427-6529-3274,Premium,490000,CC28930
6691-5105-1556-4131,Premium,640000,CC76766
1481-2536-2178-7547,Premium,653000,CC18007
1355-1728-8274-9593,Premium,660000,CC23267
9621-6787-7890-7470,Platinum,53000,CC52613
6385-4594-8055-9081,Premium,737000,CC96267
2595-8621-2855-9119,Premium,564000,CC22050
7214-4915-6387-5429,Platinum,172000,CC72302
7908-3850-6633-2606,Gold,43000,CC71044
"""


people_names = "John,Jones,Alex,Bruce"
mask_names = "\u2588" * 15
count_names = 4
hash_table = {}


@pytest.fixture
def redactor_obj():
    return CoreRedactorEngine()


def test_check_python_file(redactor_obj):
    assert redactor_obj.check_file_type(
        __file__) == 'text/x-python', 'Failed python file check'


def test_number_of_allowed_types(redactor_obj):
    assert len(redactor_obj.get_allowed_files()
               ) == 10, 'Number of allowed tests does not match expected'


def test_current_file_is_allowed(redactor_obj):
    assert redactor_obj.allowed_file(__file__), f'{__file__} should be allowed'


def test_valid_option_function_should_return_tuple(redactor_obj):
    assert type(redactor_obj.valid_options()
                ) == tuple, 'redact function should return tuple'


def test_redact_all_function_should_return_string_and_dictionary(redactor_obj):
    set1 = ("This is a string", hash_table)
    assert type(redactor_obj.redact_all(data)
                ) == type(set1), "redact_all function should return a tuple"


# def test_read_custom_patterns_should_return_list(redactor_obj):
#     assert type(redactor_obj.read_custom_patterns(os.path.dirname(os.path.abspath(__file__)) + '/../custom.json')) == type(list), "custom_patterns function should return a tuple"


# def test_redact_custom_function_should_return_string_and_dictionary(redactor_obj):
#     set1 = ("This is a string", hash_table)
#     assert type(redactor_obj.redact_custom(data, )
#                 ) == type(set1), "redact_custom function should return a tuple"
