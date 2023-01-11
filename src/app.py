# -*- coding: utf-8 -*-
"""
Created on Thu May 13 08:25:53 2021
@author: jonas
"""
import dash
import dash_bootstrap_components as dbc
#........................................

# meta_tags are required for the app layout to be molbile responsive
app = dash.Dash(__name__, suppress_callback_exceptions=True,
                external_stylesheets=[dbc.themes.JOURNAL], 
                title = "MDA Project - Bahamas Group",
                meta_tags = [{'name':'viewport',
                              'content': 'width=device-width, initial-scale=1.0'}]
               )
# Declare server for render deployment. Needed for Procfile.
server = app.server