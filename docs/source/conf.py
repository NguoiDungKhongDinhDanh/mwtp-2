project = 'mwtp'
author = 'NDKDD'
copyright = '2023, NDKDD'
version = '2.0'

extensions = [
	'sphinx.ext.autodoc',
	'sphinx.ext.autosectionlabel',
	'sphinx.ext.autosummary'
]

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

master_doc = 'index'
