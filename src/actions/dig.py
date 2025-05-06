

import itertools
from operator import mul
from uuid import uuid4
from src.soren.abstractv1 import IAction


class Dig(IAction):
    long_running_process = True
    jobId=""
    
    
    def getJobId(self):
        return self.jobId
    
    
    def run(self,input):
        self.jobId = generateUUID()
        target=self.findTargetValue(input)
        return dict({"status":"running","jobId":self.getJobId(),"target":target["value"]})


    def getParams(self):
        return {
            "name": "dig",        # Unique identifier for the action
            "title": "Scraper",      # Human-readable action title
            "description": "Web Target Scraper", # action description
            "params": [ # a list of required parameters
                {
                # Parameter configuration
                "attr": {
                    "regex_pattern": {         # Input validation
                    "pattern": "^?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?$",
                    "message": "Domain names are like sorenhq.com"
                    },
                    "input_type": "string",    # supported input type (string|number|boolean)
                    "secret": False,             # Whether the value should be masked or not
                    "required": True             # The necessity of the parameter
                },
                "options":[],
                "key": "target",                # Parameter name
                "placeholder": "Enter Domain Name", # Input placeholder for front-end view
                "value": [],        # Default value, and values themselves
                "title": "Enter Domain Name",        # Parameter title
                "description": "Enter Domain Name as Target" # Parameter description
                }

            ]
            }

    def whoami(self):
        return 	{
		"method": "dig",
		"description": "web site Scraper",
		"title": "Scraper",
		"icon":"data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz4NCg0KPCFET0NUWVBFIHN2ZyBQVUJMSUMgIi0vL1czQy8vRFREIFNWRyAxLjEvL0VOIiAiaHR0cDovL3d3dy53My5vcmcvR3JhcGhpY3MvU1ZHLzEuMS9EVEQvc3ZnMTEuZHRkIj4NCjwhLS0gVXBsb2FkZWQgdG86IFNWRyBSZXBvLCB3d3cuc3ZncmVwby5jb20sIEdlbmVyYXRvcjogU1ZHIFJlcG8gTWl4ZXIgVG9vbHMgLS0+CjxzdmcgZmlsbD0iIzAwMDAwMCIgaGVpZ2h0PSI4MDBweCIgd2lkdGg9IjgwMHB4IiB2ZXJzaW9uPSIxLjEiIGlkPSJMYXllcl8xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiANCgkgdmlld0JveD0iMCAwIDUwMCA1MDAiIGVuYWJsZS1iYWNrZ3JvdW5kPSJuZXcgMCAwIDUwMCA1MDAiIHhtbDpzcGFjZT0icHJlc2VydmUiPg0KPHBhdGggZD0iTTMwNiwxOTJoLTQ4di00OGMwLTQuNC0zLjYtOC04LThzLTgsMy42LTgsOHY0OGgtNDhjLTQuNCwwLTgsMy42LTgsOHMzLjYsOCw4LDhoNDh2NDhjMCw0LjQsMy42LDgsOCw4czgtMy42LDgtOHYtNDhoNDgNCgljNC40LDAsOC0zLjYsOC04UzMxMC40LDE5MiwzMDYsMTkyeiIvPg0KPC9zdmc+"
	    }
    
    def findTargetValue(self,body):
        for p in body["params"]:
            if p["key"] == "target":
                return p



def generateUUID()->str:
    return str(uuid4())