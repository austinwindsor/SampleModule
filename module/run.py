

class Run:
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
	"""

	def __init__(self):
		pass

	def run(parameter1=2, parameter2='apple',parameter3=False):
		"""Example function with types documented in the docstring.

		`PEP 484`_ type annotations are supported. If attribute, parameter, and
		return types are annotated according to `PEP 484`_, they do not need to be
		included in the docstring:

		Args:
			param1 (int): The first parameter.
			param2 (str): The second parameter.

		Returns:
			bool: The return value. True for success, False otherwise.
		"""
		return 