##Run this app locally via e.g. PyCharm or Spyder:

**1)** To be able to run the app locally you might have to add the following 
file paths to python:
- import sys
- sys.path.append("~/MyDashApp/apps")

**2)** Open the app inside a new environment that has package installations 
in line with the requirements_run_locally.txt file. 

**3)** Next Step:
- Open the 'MyDashApp' main folder as a project in e.g. PyCharm or Spyder.
- Run the index.py file. This file connects all modules of the app. 
- Copy the link that appears in your console to your browser to inspect the app.

**4)** Caveat/Bug:  
You can only run the the index.py file once.
If you make changes to the app and run index.py again in the same 
Spyder/PyCharm session then the app will not be displayed in your browser. 
Thus, after making changes to your app, save all files and restart Spyder/PyCharm.