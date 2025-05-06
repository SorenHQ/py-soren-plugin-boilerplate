

import itertools
from src.soren.abstractv1 import IAction


class Alpha(IAction):
    def run(self,input):
        numbersValue = self.getValue(input)
        return numbersValue[0]

    def getParams(self):
        return {
            "name": "akpha",        # Unique identifier for the action
            "title": "Alpha",      # Human-readable action title
            "description": "Set Alpha Value", # action description
            "params": [ # a list of required parameters
                {
                # Parameter configuration
                "attr": {
                    "regex_pattern": {         # Input validation
                    "pattern": "^[\d]+$",
                    "message": "Input numbers must be between 0 to 99999"
                    },
                    "input_type": "number",    # supported input type (string|number|boolean)
                    "secret": False,             # Whether the value should be masked or not
                    "required": True             # The necessity of the parameter
                },
                "options":[],
                "key": "num",                # Parameter name
                "placeholder": "input number", # Input placeholder for front-end view
                "value": [],        # Default value, and values themselves
                "title": "Enter Number",        # Parameter title
                "description": "Enter numbers" # Parameter description
                },
            ]
            }

    def whoami(self):
        return 	{
		"method": "alpha",
		"description": "set alpha value",
		"title": "ALPHA",
		"icon":"data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz4NCg0KPCFET0NUWVBFIHN2ZyBQVUJMSUMgIi0vL1czQy8vRFREIFNWRyAxLjEvL0VOIiAiaHR0cDovL3d3dy53My5vcmcvR3JhcGhpY3MvU1ZHLzEuMS9EVEQvc3ZnMTEuZHRkIj4NCjwhLS0gVXBsb2FkZWQgdG86IFNWRyBSZXBvLCB3d3cuc3ZncmVwby5jb20sIEdlbmVyYXRvcjogU1ZHIFJlcG8gTWl4ZXIgVG9vbHMgLS0+CjxzdmcgZmlsbD0iIzAwMDAwMCIgaGVpZ2h0PSI4MDBweCIgd2lkdGg9IjgwMHB4IiB2ZXJzaW9uPSIxLjEiIGlkPSJMYXllcl8xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiANCgkgdmlld0JveD0iMCAwIDUwMCA1MDAiIGVuYWJsZS1iYWNrZ3JvdW5kPSJuZXcgMCAwIDUwMCA1MDAiIHhtbDpzcGFjZT0icHJlc2VydmUiPg0KPHBhdGggZD0iTTMwNiwxOTJoLTQ4di00OGMwLTQuNC0zLjYtOC04LThzLTgsMy42LTgsOHY0OGgtNDhjLTQuNCwwLTgsMy42LTgsOHMzLjYsOCw4LDhoNDh2NDhjMCw0LjQsMy42LDgsOCw4czgtMy42LDgtOHYtNDhoNDgNCgljNC40LDAsOC0zLjYsOC04UzMxMC40LDE5MiwzMDYsMTkyeiIvPg0KPC9zdmc+"
	    }
    
    def getValue(self,body):
        return list(itertools.chain.from_iterable([p["value"] for p in body["params"] ]))

