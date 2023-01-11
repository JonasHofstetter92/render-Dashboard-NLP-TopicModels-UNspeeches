# -*- coding: utf-8 -*-
"""
Created on Thu May 13 20:59:38 2021

@author: jonas
"""
## import packages
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Connect to main app.py file
from app import app
from app import server

# Connect to my 2 app pages
from apps import explore_DTM_model, explore_LDA_model, info_models
##.....................................................

# grand layout
app.layout =    dbc.Container([
                              dcc.Location(id='url', pathname = '/apps/explore_DTM_model', refresh= False),
                 dbc.Row([
                      dbc.Col(html.Div(children='''
                                   Use the three red links below to select one of the 3 pages of this app! 
                                   ''', id='app-navigation-info', className='text-center , mb-4'),
                              width=12)
                            ]),
                 dbc.Row([
                      dbc.Col(html.Div([
                           dcc.Link('Page 1: Explore DTM Model|', href='/apps/explore_DTM_model'),
                           dcc.Link('Page 2: Explore LDA Model|', href='/apps/explore_LDA_model'),
                           dcc.Link(' Page 3: Info About Models', href='/apps/info_models'),
                      ], className="text-center , mb-4"),
                              width=12)
                            ]),
                 html.Div(id='page-content', children=[])
               ], fluid = True)

                              
# provide links to select between the app´s page1 and page2
@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname): 
    if pathname == '/apps/explore_DTM_model':
        return explore_DTM_model.layout
    elif pathname == '/apps/explore_LDA_model':
        return explore_LDA_model.layout
    elif pathname == '/apps/info_models':
        return info_models.layout
    else:
        return "404 Page Error. Please choose link!"


# run app on server
if __name__ == '__main__':
    app.run_server(debug=False)