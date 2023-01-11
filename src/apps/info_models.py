# -*- coding: utf-8 -*-
"""
Created on Fri May 21 13:41:59 2021

@author: jonas
"""
# dash packages
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

##....................................................................

# Create subtitle page 3

subtitle_page3 = dbc.Container([
                              dbc.Row([
                                      dbc.Col([
                                          html.Div(children='''
                                                   Page3: Info about DTM and LDA models, and about our preprocessing pipeline applied to the G20 speeches before modelling. 
                                                   ''', id='subtitle-page3', className='text-center , mb-4'),       
                                      ],width=12)
                                      ])
                              ])
                 

##.....................................................................                                                   

# text Intro

text_intro = dbc.Container([
                dbc.Row([
                dbc.Col([dcc.Markdown('''
                                      ## Introduction to Topic Modelling ##
                                      Two types of models were used to extract topics from the UN General Assembly speeches corpus. First, LDA models were used to produce 'static' models for what we termed 'decade slices' (70s, 80s, 90s, 2000s, 2010s). The idea is that by modelling in decade slices, we can capture relevant topics of each of the decades. The drawback, however, is that such an approach does not allow to adequately track the evolution of the speech topics throughout the years. Therefore, as a second type of model, a dynamic topic model, which builds on LDA, was used. This model allows to explore the evolution of the topics, i.e. which words characterise them, and thus what their content is as a function of time. In the paragraphs below, the intuition behind the models is provided.
                                      ''')
                        ],width={'size':12}),
                        ])                        
                        ]) 
                                                          
                                                   
##.....................................................................
                                                  
# text explaining DTM

text_DTM = dbc.Container([
                dbc.Row([
                dbc.Col([dcc.Markdown('''
                                      ## Dynamic Topic Modelling - DTM ##
                                      One of the drawbacks of using LDA models is that we only get a 'static' view of the topics in the respective corpus the model was trained on, in our cases the five different decades. In other words, we do not get a sense on how the topics evolve over time, aside from just comparing the different 10 extracted topics from each of the models, which is not an ideal way of working. Another more technical issue is that documents and the words embedded in them are treated as being exchangeable. However, our collection of documents reflects content that evolves over time. Whatever is talked about during those UN Assembly speeches reflects contemporary events, that are very prone to the dynamic environment of the world we live in. As a result of this evolving content, the words used to describe this content also evolve. This is unfortunately not something that can be captured by our approach of using five 'static' LDA models, and LDA models in general. A solution for this issue is proposed by training a dynamic topic model (proposed by Blei and colleagues in 2006), which does take the evolving nature of documents and their words throughout time into account. In short, we leverage the sequential nature of the data (speeches can be grouped by year, and as such have a dynamic component) to take the sequential nature of the 'yearly' speeches into account when extracting the topics. In addition, it provides insight in how the topics evolve over time, based on the word frequency for the given topics. This allows us to track trends in more systematic way, i.e. yearly across topics, rather than comparing five broad models and their extracted topics. 
                                      ''')
                        ],width={'size':12}),
                        ])                        
                        ]) 
##....................................................................
                                                  
# text explaining LDA

text_LDA = dbc.Container([
                dbc.Row([
                dbc.Col([dcc.Markdown('''
                                      ## Latent Dirichlet Allocation - LDA ##
                                      Answering the question, 'what are the topics discussed in the UN Assembly speeches?' requires the understanding of what topics like 'cold war' or 'peace negotiations' entail. The human brain is good at understanding context, detecting similarity and extract meaning from texts like speeches, and can thus easily distinguish topics from each other in text documents. This, however, is not the case for 'machines', for which understanding topics is problematic. Latent Dirichlet Allocation (LDA; Blei, Ng and Jordan, 2003), is an unsupervised technique that can be used to tackle the issue of topic modelling. 

                                      LDA 'explains' why sets of words occur together by assuming that these words are related to underlying, 'latent', topics. These topics can then, in turn, be used to explain how and why certain documents are similar. In other words, LDA assumes that every document consists of certain topics, and that topics themselves consist of words characterizing them. Therefore, the assumption is also made that words 'carry semantic information', and as such that documents reflecting similar topics will also consist of similar sets of words.

                                      Technically speaking, documents are probability distributions over latent topics, and topics are probability distributions over words. For instance, take a speech from the 80s by, for instance the UK, that heavily emphasizes tensions between the USA and the Soviet Union. Vocabulary that we as humans relate to this will be more present, and because other speeches in the data place the same words together regarding these tensions, there will be an underlying topic in the 80s speeches that is built up from these sets of words. As such, topics will have a certain probability of occurring in this speech, including a topic related to the cold war, but maybe also more general topics such as global economic evolution. However, given the stronger emphasis on the cold war, by having more words present relating to that topic, the probability that this speech tackles a topic that we as humans label 'cold war' will be higher than any of the other topics. 

                                      Note that this is an exploratory and unsupervised technique. The amount of topics to be extracted can be specified by the user. The most important criterion is that the topics are coherent to a certain extent that topic labels can be assigned. We settled for ten topics given that they were mostly coherent and that for every decade often a wide variety of topics are brought forward in these UN Assembly addresses. To be consistent across decades, the choice for ten topics was maintained across all decades. 
                                      ''')
                        ],width={'size':12}),
                        ])                        
                        ]) 
                                     
##....................................................................
                                                  
# text explaining Preprocessing

text_preprocessing = dbc.Container([
                dbc.Row([
                dbc.Col([dcc.Markdown('''
                                      ## Preprocessing of G20 Speeches ##
                                      The individual speeches are stored in text files that are organised into directories based on the year they were delivered. Using a for loop, each speech is loaded into a pandas dataframe for later manipulation. Each row includes a single speech, along with the ISO code of the country and the year it was delivered. In our analysis we focus on G20 countries. The G20 countries are some of the most influential countries represented in the United Nations and their speeches are therefore representative of some of the most important and pressing issues. Speeches held at the General Debate cover a wide range of topics within a relatively short time. We therefore segment the speeches into individual paragraphs before analysing them, as this yields better results when extracting topics. A full stop followed by a line break segments the text into different paragraph. Due to the different shapes of each document, this method most reliably separates speeches into its components.

                                      For different analyses, we are interested in different time slices, depending on the analysis used we first split the dataset into the time slice of interest. The pre-processing that follows is the same for every subsequent model. We have written a pre-processing function that will take the textual data that we put into the function and then provides an output in the final form that our model requires. In short this function, using regular expression, first cleans the artefacts that occurred during OCR, removes all numbers and all further characters that are not letters or spaces. Finally trailing spaces are also removed, such that we are only left with individual words. We now apply lemmatisation using the spacy lemmatiser on the cleaned text. Spacy has the benefit that it does part of speech (POS) tagging in the first run through the data and in a second run returns the lemmatised words (according to their POS) to a list. 

                                      Then, using the phrases function (gensim package) we built bi-grams and tri-grams to find terms such as "security council". The bi-gram and tri-gram phraser is trained on the whole text corpus, identifying words that frequently occur next to each other across all documents. The trained phraser is then called in the pre-processing function, where it identifies the bi-grams and tri-grams that are present in the text and joins them together with underscores. This leaves us with our final dataset that can subsequently be used to train LDA and DTM models. 
                                      ''')
                        ],width={'size':12}),
                        ])                        
                        ]) 
                                      

##....................................................................
                                      
# Links for LDA and DTM

links_paper_models = dbc.Container([
                                dbc.Row([
                                    dbc.Col([     
                                          html.H3(children='''
                                                   Papers on LDA and DTM
                                                   ''', id='ref-papers-page3'),
                                           ],width={'size':12}),
                                       ]),    
                                dbc.Row([
                                    dbc.Col([
                                             html.A("Blei, D. M., Ng, A. Y., & Jordan, M. I. (2003). Latent dirichlet allocation. the Journal of machine Learning research, 3, 993-1022.", href='https://www.jmlr.org/papers/volume3/blei03a/blei03a.pdf?TB_iframe=true&width=370.8&height=658.8', 
                                                    target="_blank", id='link-LDA-paper')
                                             ],width={'size':12}),
                                       ]),
                                dbc.Row([
                                    dbc.Col([
                                             html.A("Blei, D. M., & Lafferty, J. D. (2006, June). Dynamic topic models. In Proceedings of the 23rd international conference on Machine learning (pp. 113-120).", href='https://dl.acm.org/doi/pdf/10.1145/1143844.1143859', 
                                                    target="_blank", id='link-DTM-paper')
                                             ],width={'size':12}),
                                       ])
                                ])
##....................................................................


# Create layout with embedded explanations about
# models (LDA/DTM) and preprocessing pipeline

layout = dbc.Container([
                        subtitle_page3,    
                        html.Hr(),
                                text_intro,
                        html.Hr(),
                                text_LDA,
                        html.Hr(),
                                text_DTM,
                        html.Hr(),
                                text_preprocessing,
                        html.Hr(),
                                links_paper_models,
                    ],fluid=True
                  )
