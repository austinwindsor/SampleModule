import logging
log = logging.getLogger(__name__)
import pandas as pd
from abstract_classes.run import AbstractRun

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