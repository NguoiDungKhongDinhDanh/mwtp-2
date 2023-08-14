project = 'mwtp'
author = 'NDKDD'
copyright = '2023, NDKDD'
version = '1.0'

extensions = [
	'sphinx.ext.autodoc',
	'sphinx.ext.autosectionlabel',
	'sphinx.ext.autosummary',
	'sphinx.ext.duration',
	'sphinx.ext.githubpages',
	'sphinx_rtd_theme'
]

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

master_doc = 'index'
