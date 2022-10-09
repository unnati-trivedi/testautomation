import pytest
from collections import defaultdict

#from cucumber_tag_expressions import parse

#from step_definitions.test_product_api_steps import *

from lib.report import pytest_terminal_summary

"""
def pytest_configure(config):
    config.option.keyword = 'automated'
"""

def pytest_addoption(parser):
    parser.addoption('--tags',
                     metavar="str",
                     help='Will filter tests by given tags')