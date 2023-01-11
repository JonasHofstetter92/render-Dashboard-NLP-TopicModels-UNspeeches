# -*- coding: utf-8 -*-
"""
Created on Mon May 31 11:10:14 2021

@author: josch
"""

# dash packages
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

# connect to app
from app import app
##...........................................................................


# Create subtitle page 1

subtitle_page2 = dbc.Container([
                              dbc.Row([
                                      dbc.Col([html.Div(children='''Page2: Explore the topics and terms of G20 speeches that were extracted by a Latent Dirichlet Allocation (LDA) model.''', 
                                              id='subtitle-page2', className='text-center , mb-4'),
                                      ],width=12)
                                      ])
                              ])
                             
##........................................................

# Create an input Group

input_group_page2 = dbc.Container([
                         dbc.Row([
                                dbc.Col([
                                    html.Label(['Inspect the Speeches´ Topics via an LDA Model for a Specific Decade (Changes Bottom Left Plot)'], 
                                               style={'font-weight': 'bold', "text-align": "center"}),
                                    dcc.Dropdown(
                                        id='LDA-model-selection',
                                        options=[
                                            {'label': 'LDA (1970-1979)', 'value': 'LDA_70s'},
                                            {'label': 'LDA (1980-1989)', 'value': 'LDA_80s'},
                                            {'label': 'LDA (1990-1999)', 'value': 'LDA_90s'},
                                            {'label': 'LDA (2000-2009)', 'value': 'LDA_2000s'},
                                            {'label': 'LDA (2010-2019)', 'value': 'LDA_2010s'},
                                        ],
                                        value='LDA_70s',
                                        searchable=False,
                                        clearable=False)
                                    ],width={'size':12}),
                                ])
                            ])

##...........................................................................

# bottom-plots on page 1
LDA_plot = dbc.Container([
                        dbc.Row([
                            dbc.Col([
                                    html.Div(id='container_plot_LDA', children=[]),
                                    ],width={'size':12}),
                               ])
                           ])


##...........................................................................


# title lda plot page 2
title_bottom_graph_page2 = dbc.Container([
                                dbc.Row([
                                    dbc.Col([
                                           html.Div([html.Label(['Latent Dirichlet Model (LDA) for Selected Decade'], 
                                           style={'font-weight': 'bold', "text-align": "center"}),
                                           ])
                                       ],width={'size':12}),
                                    ])
                                ])

##...........................................................................

# link to pyLDAviz documentation
link_pyLDAviz = dbc.Container([dbc.Row([
                                    dbc.Col([     
                                          html.Div(children='''
                                                   The interactive graphs for topic model vizualization (bottom graphs on page1 & page2) were created with the pyLDAvis package:
                                                   ''', id='ref-bottom-graph-page1'),
                                           ])
                                       ]),    
                                dbc.Row([
                                    dbc.Col([
                                             html.A("Link to external pyLDAvis documentation", href='https://readthedocs.org/projects/pyldavis/downloads/pdf/latest/', 
                                                    target="_blank", id='link-doc-bottom-graph-page1')
                                             ],width={'size':12})
                                       ])
                                ])

##...........................................................................

# legend of bottom-plot page 1

pyLDAviz_legend = dbc.Container([
                                dbc.Row([
                                    dbc.Col([dcc.Markdown('''
                                      # How to interpret pyLDAviz graphs: #
                                      
                                      **Circle size**: hovering directly over the circle shows the `marginal distribution` of a topic where the circle size corresponds to the topic's overall prevalence in the corpus of speeches. Hovering over a single term on the right side of pyLDAviz graph changes the size of the circles that now indicate the `conditional distribution` of the topics given the specific term.
                                
                                      **Distances between circles**: indicate inter-topic distances as computed by the Jensen-Shannon divergence metric. Two dimensional down-scaling of these distances is achieved through Principal Component Analysis (PCA).   
                                
                                      **The red bars**: represent the frequency of each word given a selected topic.
                                      
                                      **The blue bars**: represent the overall frequency of a word in the entire corpus of speeches.
                                
                                      **The 'lambda slider'**: determines the weight that is placed on the frequency of a word the lower and closer the value for lambda is to 0, the more weight is placed on the frequency of a word within the topic (red bar). The higher and closer the value for lambda is to 1, less weight is placed on frequency of word given a topic, in favor of overall word frequency. 
                                      ''')],width={'size':12}),
                                      ])
                                                          
                              ])
##...........................................................................

# notes on analyzed data

G20_countries = dbc.Container([
                                dbc.Row([
                                    dbc.Col([     
                                          html.H1(children='''
                                                  Notes on raw data:
                                                   ''', id='ref-bottom-graph-page1'),
                                           ],width={'size':12}),
                                       ]),    
                                dbc.Row([
                                    dbc.Col([
                                             html.A("Link to analyzed corpus of speeches", href='https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/0TJX8Y', 
                                                    target="_blank", id='link-LDA-paper')
                                             ],width={'size':12}),
                                       ]),
                                dbc.Row([
                                    dbc.Col([dcc.Markdown('''
                                        **Countries from G20-group included in analysis**: Canada, France, Germany, USA, UK, Italy, Japan, Argentina, Australia, Brasil, India, Indonesia, Mexico, Russia, Saudi Arabia, Sout Korrea, Turkey, China.  
                                        **Countries from G20-group NOT included in analysis**: South Africa, EU representatives.
                                        ''')],width={'size':12})
                                       ])
                                ])

##...........................................................................



# layout - bootstrap container page 2

layout = dbc.Container([
            subtitle_page2,   
            html.Hr(),
            input_group_page2,
            html.Hr(),
            title_bottom_graph_page2,
            html.Hr(),
            LDA_plot,
            link_pyLDAviz,
            pyLDAviz_legend,
            G20_countries,
        ],fluid=True
    )   


##...........................................................................

# Callback function for dependency bottom left graph page1 
# on dropdown 'LDA-model-selection' 
@app.callback(
    Output('container_plot_LDA','children'), 
    Input('LDA-model-selection','value'),
) 
def bottom_plot_page1_models(value):
    new_child = html.Div(children=[
        dbc.Row([dbc.Col(html.Iframe(id="Bottom_Plot_LDA_Page1",
                                src=app.get_asset_url('{}.html'.format(value)), 
                                style={"height": "1200px", "width": "100%"}),md=12)
                    ],align="center"
                )   
        ])     
    return new_child