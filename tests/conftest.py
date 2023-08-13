import json
from pathlib import Path

import pytest

from mwtp.parser import Parser


class IIFE:
	
	def __init__(self, function):
		self.function = function
		function()
	
	def __call__(self, *args, **kwargs):
		return self.function(*args, **kwargs)


def generate_fixtures(file_path: Path):
	with open(file_path, encoding = 'utf-8') as file:
		data = json.load(file)
	
	@pytest.fixture(scope = 'session')
	def raw_data():
		yield data
	
	@pytest.fixture(scope = 'session')
	def parser():
		parser = Parser(
			data['namespaces'],
			data['namespacealiases']
		)
		
		yield parser
	
	file_name = file_path.name
	prefix = '_'.join(file_name.split('.')[:-2])
	raw_data_fixture_name = f'{prefix}_data'
	parser_fixture_name = f'{prefix}_parser'
	
	globals()[raw_data_fixture_name] = raw_data
	globals()[parser_fixture_name] = parser


@IIFE
def query_files():
	assets = Path(__file__).resolve().parent / 'assets'
	
	for file_path in assets.glob('*.json'):
		generate_fixtures(file_path)
