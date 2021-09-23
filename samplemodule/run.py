import logging
log = logging.getLogger(__name__)
import pandas as pd
# from abstract_classes.run import AbstractRun

class AbstractRun:
	def __init__(self):
		pass

	def run(self,parameter = 'sample'):
		"""
## Short Description written in Markdown

Long Description Written in Markdown

Args:
	parameter (str, optional): description about argument {list, of, acceptable, values}

Return:
	DataFrame: the output of the analysis
		"""
		return pd.DataFrame()

	def get_argparser(self, run_method='run'):
		"""Summary
		
		Args:
		    run_method (str, optional): Description
		
		Returns:
		    argparse.Namespace: Description
		"""
		docstring = getattr(self, run_method).__doc__
		parsed_docstring = self._parse_docstring(docstring)
		parser = self._make_argparser(parsed_docstring)
		return parser.parse_args()

	def _make_argparser(self, docstring_obj):
		parser = argparse.ArgumentParser(docstring_obj.short_description + "\n" + docstring_obj.long_description)
		parser.add_argument("module_name", help="the module name of the task to reference", nargs='?')
		for param in docstring_obj.params:
			parser.add_argument("--"+param.arg_name, help=param.description, choices=self._parse_options(param.description), 
								default=param.default, required=not param.is_optional)
		return parser

	def _parse_docstring(self, docstring):
		"""Summary
		
		Args:
		    docstring (TYPE): Description
		
		Returns:
		    TYPE: Description
		"""
		return docstring_parser.parse(docstring)

	def _parse_options(self, string, regex_expression="\{(.+)\}"):
		"""extracts the options a parameter takes in and return a set of strings
		
		Args:
		    string (str): the decsription of a parameter
		    regex_expression (str, optional): expression used to extract the options stored in a set
		
		Returns:
		    Union(set of {str}, NoneType): if there is a set of options, it return a set of strings, otherwise, None
		"""
		results = re.findall(regex_expression, string)
		return set(results[0].split(',')) if results else None



class Run(AbstractRun):

	def __init__(self):
		pass

	def run(self, parameter1=2, parameter2='apple',parameter3=False, *args):
		"""
# Module Name
This class `__doc__` string should be written in Markdown to render formatting in the GUI.

This Run class should have	

1. a `run()` method with parameters and a fully fleshed `__doc__` string using ***Google Documentation format***  
2. Links to any documentation included in this class `__doc__` string  
3. an example of parameters to run
```
Parameter1		2
Parameter2		Apple
Parameter3		False
```
4. Any additonal business or other contextual knowledge needed to run this tool

Args:
	parameter1 (int): The first parameter {1,2,3,4,5}.
	parameter2 (str): The second parameter.
	parameter3 (file): either base64 encoding of file or path to file

Returns:
	bool: The return value. True for success, False otherwise.
		"""
		logging.warning("Let's put a message here to see if it appears")
		return pd.DataFrame({'b':[0,0,0]})