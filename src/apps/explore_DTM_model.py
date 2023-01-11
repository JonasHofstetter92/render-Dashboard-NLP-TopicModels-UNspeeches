# -*- coding: utf-8 -*-
"""
Created on Thu May 20 16:46:41 2021

@author: jonas
"""
# dash packages
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

# load/save packages and manipulate file paths
import pickle
import pathlib
import os

# visualization
import plotly.express as px

# import own functions
from own_functions import translate_topic_number, create_df_termprob, create_df_viz

# connect to app
from app import app
##........................................................

# Get relative file path of saved DTM model & load DTM model

#parent_folder_path = pathlib.Path(__file__).parent # ..move to parent folder
#model_folder_path = parent_folder_path.joinpath("../saved_models").resolve()
#DTM_path = model_folder_path.joinpath("finalDTM_model")
#norm_DTM_path = os.path.normpath(DTM_path) # normalize the specified path
#ldaseq = ldaseqmodel.LdaSeqModel.load(norm_DTM_path) # load DTM model

parent_folder_path = pathlib.Path(__file__).parent # ..move to parent folder
model_folder_path = parent_folder_path.joinpath("../saved_models").resolve()
DTM_path = model_folder_path.joinpath("final.pkl")
norm_DTM_path = os.path.normpath(DTM_path) # normalize the specified path
ldaseq = pickle.load(open(norm_DTM_path,'rb')) # load DTM model

##........................................................

# Create grand title

grand_title =   dbc.Container([
                              dbc.Row([
                                      dbc.Col([html.H1('Explore Topic Models Built on Speeches Held by G20-Country Representatives at the UN General Assembly', 
                                              id='title-page1', className='text-center , mb-4'),
                                      ],width=12)
                                     ])
                             ])

##........................................................

# Create subtitle page 1

subtitle_page1 = dbc.Container([
                              dbc.Row([
                                      dbc.Col([html.Div(children='''Page1: Explore the topics and terms of G20 speeches that were extracted by a Dynamic Topic Model (DTM).''', 
                                              id='subtitle-page1', className='text-center , mb-4'),
                                      ],width=12)
                                      ])
                              ])
                             
##........................................................

# Create an input Group

input_group_page1 = dbc.Container([
        dbc.Row([
            dbc.Col([
                html.Label(['Inspect the Speeches´ Topics via a Dynamic Topic Model (DTM) for a Single Year (Changes Bottom Plot)'], 
                           style={'font-weight': 'bold', "text-align": "center"}),
                dcc.Dropdown(
                    id='year-selection-DTM',
                       options=[
                                {"label":"1970", "value":0},
                                {"label":"1971", "value":1},
                                {"label":"1972", "value":2},
                                {"label":"1973", "value":3},
                                {"label":"1974", "value":4},
                                {"label":"1975", "value":5},
                                {"label":"1976", "value":6},
                                {"label":"1977", "value":7},
                                {"label":"1978", "value":8},
                                {"label":"1979", "value":9},
                                {"label":"1980", "value":10},
                                {"label":"1981", "value":11},
                                {"label":"1982", "value":12},
                                {"label":"1983", "value":13},
                                {"label":"1984", "value":14},
                                {"label":"1985", "value":15},
                                {"label":"1986", "value":16},
                                {"label":"1987", "value":17},
                                {"label":"1988", "value":18},
                                {"label":"1989", "value":19},
                                {"label":"1990", "value":20},
                                {"label":"1991", "value":21},
                                {"label":"1992", "value":22},
                                {"label":"1993", "value":23},
                                {"label":"1994", "value":24},
                                {"label":"1995", "value":25},
                                {"label":"1996", "value":26},
                                {"label":"1997", "value":27},
                                {"label":"1998", "value":28},
                                {"label":"1999", "value":29},
                                {"label":"2000", "value":30},
                                {"label":"2001", "value":31},
                                {"label":"2002", "value":32},
                                {"label":"2003", "value":33},
                                {"label":"2004", "value":34},
                                {"label":"2005", "value":35},
                                {"label":"2006", "value":36},
                                {"label":"2007", "value":37},
                                {"label":"2008", "value":38},
                                {"label":"2009", "value":39},
                                {"label":"2010", "value":40},
                                {"label":"2011", "value":41},
                                {"label":"2012", "value":42},
                                {"label":"2013", "value":43},
                                {"label":"2014", "value":44},
                                {"label":"2015", "value":45},
                                {"label":"2016", "value":46},
                                {"label":"2017", "value":47},
                                {"label":"2018", "value":48},
                                {"label":"2019", "value":49},
                                ],
                    value=0,
                    clearable=False,
                    searchable=False)
             ],width={'size':6}), 
        
          
        dbc.Col([
             html.Label(['Within a Single Topic of the DTM Model: Plot the Evolution of Term Frequencies (Changes Evolution Plot)'], 
                  style={'font-weight': 'bold', "text-align": "center"}),
                   dcc.Dropdown(
                    id='topic-selection',
                       options=[
                                {"label":"Topic 1", "value":1},
                                {"label":"Topic 2", "value":2},
                                {"label":"Topic 3", "value":3},
                                {"label":"Topic 4", "value":4},
                                {"label":"Topic 5", "value":5},
                                {"label":"Topic 6", "value":6},
                                {"label":"Topic 7", "value":7},
                                {"label":"Topic 8", "value":8},
                                {"label":"Topic 9", "value":9},
                                {"label":"Topic 10", "value":10},
                                ],
                    value=1,
                    clearable=False,
                    searchable=False
                  ),
                  dcc.Input(id='input-1-state', type='text', value='peace'),
                  dcc.Input(id='input-2-state', type='text', value='security'),
                  dcc.Input(id='input-3-state', type='text', value='wish'),
                  dcc.Input(id='input-4-state', type='text', value='conflict'),
                  dcc.Input(id='input-5-state', type='text', value='middle_east'),
                  dcc.Input(id='input-6-state', type='text', value='hope'),
                  html.Button(id='submit-button-state', n_clicks=0, children='Submit'),
                  html.Div(id='output-state')
                  ], width={'size':6}),
      ])
    ])



##...........................................................................

# evolution-plot on page 1
top_plot = dbc.Container([
                        dbc.Row([
                            dbc.Col([
                                    html.Div(id='container_top_plot_page1', children=[]),
                                    ],width={'size':12})
                               ])
                           ])

##...........................................................................

# bottom-plots on page 1
bottom_plot = dbc.Container([
                        dbc.Row([
                            dbc.Col([
                                    html.Div(id='container_bottom_plot_DTM', children=[]),
                                    ],width={'size':12})
                               ])
                           ])

##...........................................................................

# title of bottom-plot on page 1
title_bottom_graphs = dbc.Container([
                                dbc.Row([
                                    dbc.Col([
                                            html.Label(['Dynamic Topic Model (DTM) for Selected Year'], 
                                                  style={'font-weight': 'bold', "text-align": "center"}),
                                            ],width={'size':12}),
                                       ])
                                    ])

##...........................................................................

# link to pyLDAviz documentation

link_pyLDAviz  =   dbc.Container([
                                dbc.Row([
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
                                  
                                  **Circle size**: hovering directly over the circle shows the `marginal distribution` of a topic where the circle size corresponds to the topic's overall prevalence in the corpus of speeches. Hovering over single terms on the right side of pyLDAviz changes the size of the circles that now indicate the `conditional distribution` of the topics given the specific term.
                            
                                  **Distances between circles**: indicate inter-topic distances as computed by the Jensen-Shannon divergence metric. Two dimensional down-scaling of these distances is achieved through Principal Component Analysis (PCA). 
                            
                                  **The red bars**: represent the frequency of each word given a selected topic.
                                  
                                  **The blue bars**: represent the overall frequency of a word in the entire corpus of speeches.
                            
                                  **The 'lambda slider'**: determines the weight that is placed on the frequency of a word the lower and closer the value for lambda is to 0, the more weight is placed on the frequency of a word within the topic (red bar). The higher and closer the value for lambda is to 1, less weight is placed on frequency of word given a topic, in favor of overall word frequency. 
                                  ''')],width={'size':12})
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




# layout - bootstrap container page 1

layout = dbc.Container([
            grand_title,
            subtitle_page1,   
            top_plot,
            html.Hr(),
            input_group_page1,
            html.Hr(),
            title_bottom_graphs,
            html.Hr(),
            bottom_plot,
            link_pyLDAviz,
            pyLDAviz_legend,
            G20_countries,
        ],fluid=True
    )
                                     
##...........................................................................
   

# Callback function to receive term submission message 
@app.callback(Output('output-state', 'children'),
              Input('submit-button-state', 'n_clicks'),
              State('topic-selection', 'value'),
              State('input-1-state', 'value'),
              State('input-2-state', 'value'),
              State('input-3-state', 'value'),
              State('input-4-state', 'value'),
              State('input-5-state', 'value'),
              State('input-6-state', 'value'))
def update_output(n_clicks, topic_nbr, term1, term2, term3, term4, term5, term6):
    return u'''
        Submission #{}. 
        Within topic #{}, plot evolutions of within-topic frequencies 
        for:
        Term 1 - "{}",
        Term 2 - "{}",
        Term 3 - "{}",
        Term 4 - "{}",
        Term 5 - "{}",
        and Term 6 - "{}"
    '''.format(n_clicks, topic_nbr, term1, term2, term3, term4, term5, term6)                                     
        

# Callback function to update top graph page1 
@app.callback(Output('container_top_plot_page1', 'children'),
              Input('submit-button-state', 'n_clicks'),
              State('container_top_plot_page1', 'children'),
              State('topic-selection', 'value'),
              State('input-1-state', 'value'),
              State('input-2-state', 'value'),
              State('input-3-state', 'value'),
              State('input-4-state', 'value'),
              State('input-5-state', 'value'),
              State('input-6-state', 'value'))
def update_top_plot_page1(n_clicks, div_children, topic, term1, term2, term3, term4, term5, term6):
    # Using own function: translate displayed topic nbr in 
    # pyLDAviz graph to actual/corresponding topic nbr in ldaseq model  
    topic_in_model = translate_topic_number(topic)
    # Using own functions: Convert pre-trained DTM model into df for evolution plot
    df_term_evolution, df_prob_evolution = create_df_termprob(ldaseq, topic_in_model)
    viz_df = create_df_viz(df_term_evolution, df_prob_evolution, term1, term2, term3, term4, term5, term6)
    #plot term probability evolution
    fig = px.line(viz_df, x="year", y="term_frequency", color="term", 
                  title='Evolution of Term Frequencies Within Topic {}'.format(topic))
    div_children = dcc.Graph(id='top_plot_page1', figure= fig)
    return div_children
     
                     
# Callback function for dependency bottom right graph page1 
# on dropdown 'years-selection-DTM' 
@app.callback(
    Output('container_bottom_plot_DTM','children'), 
    Input('year-selection-DTM','value'),
) 
def bottom_plot_page1_DTM_years(value):
    new_child = html.Div(children=[
        dbc.Row([dbc.Col(html.Iframe(id="Bottom_Plot_DTM_Page1",
                                src=app.get_asset_url('DTM_{}.html'.format(1970+value)), 
                                style={"height": "1200px", "width": "100%"}),md=12)
                    ],align="center"
                )   
        ])     
    return new_child
