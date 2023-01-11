# -*- coding: utf-8 -*-
"""
Created on Thu May 13 11:48:03 2021
@author: jonas
"""
## import packages
import numpy as np
import pandas as pd
##.....................................................

# Function 1: Translate displayed topic nbr in  
#             pyLDAviz DTM graph to topic nbr in ldaseq model
         
def translate_topic_number(topic):
    
    if topic == 2:
        topic_nbr_in_model = 0
    elif topic == 10:
        topic_nbr_in_model = 1
    elif topic == 1:
        topic_nbr_in_model = 2
    elif topic == 4:
        topic_nbr_in_model = 3
    elif topic == 5:
        topic_nbr_in_model = 4
    elif topic == 7:
        topic_nbr_in_model = 5
    elif topic == 3:
        topic_nbr_in_model = 6
    elif topic == 9:
        topic_nbr_in_model = 7
    elif topic == 6:
        topic_nbr_in_model = 8
    elif topic == 8:
        topic_nbr_in_model = 9
    
    return topic_nbr_in_model



# Function 2: Create dataframe with evolutions of selected term probabilities 
#             within selected topic number. 

def create_df_termprob(ldaseq, topic):
    
    # extract topic evolution from DTM model
    ev = ldaseq.print_topic_times(topic=topic) 
            
    # extract only terms from tuples of all time slices
    term_evolution = [[item[0] for item in time_sl] for time_sl in ev]
            
    # extract only term probabilities from tuples of all time slices
    prob_evolution = [[item[1] for item in time_sl] for time_sl in ev]
            
    # convert evolutions of terms into dataframe
    df_term_evolution = pd.DataFrame.from_records(term_evolution)
            
    # convert evolutions of term probability into dataframe
    df_prob_evolution = pd.DataFrame.from_records(prob_evolution)
            
    # transpose both dataframes 
    df_term_evolution = df_term_evolution.transpose()
            
    df_prob_evolution = df_prob_evolution.transpose()
            
    # rename columns to corresponding year number
    df_term_evolution.rename(columns = {0: 1970, 1: 1971, 2: 1972, 3: 1973, 
                                        4: 1974, 5: 1975, 6: 1976, 7: 1977, 
                                        8: 1978, 9: 1979, 10: 1980, 11: 1981,
                                        12: 1982, 13: 1983, 14: 1984, 15: 1985,
                                        16: 1986, 17: 1987, 18: 1988, 19: 1989,
                                        20: 1990, 21: 1991, 22: 1992, 23: 1993, 
                                        24: 1994, 25: 1995, 26: 1996, 27: 1997,
                                        28: 1998, 29: 1999, 30: 2000, 31: 2001,
                                        32: 2002, 33: 2003, 34: 2004, 35: 2005,
                                        36: 2006, 37: 2007, 38: 2008, 39: 2009,
                                        40: 2010, 41: 2011, 42: 2012, 43: 2013,
                                        44: 2014, 45: 2015, 46: 2016, 47: 2017,
                                        48: 2018, 49: 2019}, 
                                          inplace = True)
        
    # rename columns to corresponding year number
    df_prob_evolution.rename(columns = {0: 1970, 1: 1971, 2: 1972, 3: 1973, 
                                        4: 1974, 5: 1975, 6: 1976, 7: 1977, 
                                        8: 1978, 9: 1979, 10: 1980, 11: 1981,
                                        12: 1982, 13: 1983, 14: 1984, 15: 1985,
                                        16: 1986, 17: 1987, 18: 1988, 19: 1989,
                                        20: 1990, 21: 1991, 22: 1992, 23: 1993, 
                                        24: 1994, 25: 1995, 26: 1996, 27: 1997,
                                        28: 1998, 29: 1999, 30: 2000, 31: 2001,
                                        32: 2002, 33: 2003, 34: 2004, 35: 2005,
                                        36: 2006, 37: 2007, 38: 2008, 39: 2009,
                                        40: 2010, 41: 2011, 42: 2012, 43: 2013,
                                        44: 2014, 45: 2015, 46: 2016, 47: 2017,
                                        48: 2018, 49: 2019}, 
                                          inplace = True)

    return df_term_evolution, df_prob_evolution





# Function 3: Create final df for plotting evolutions
def create_df_viz(df_term_evolution, df_prob_evolution,
                        term1 = 'NA',term2 = 'NA',term3 = 'NA',
                        term4 = 'NA',term5 = 'NA',term6 = 'NA'):

    # create list of terms 
    terms = [term1,term2,term3,term4,term5,term6]
    
    # create empty list of lists for term probabilities
    prob_term = np.zeros((6, 50))
    
    # extract term probabilities
    for term in range(len(terms)):
        for year in range(len(df_term_evolution.columns)):
            if df_term_evolution[1970+year].str.contains(terms[term]).any():
                row_idx = df_term_evolution.index[df_term_evolution[1970+year] == terms[term]]                     
                prob_term[term,year] = df_prob_evolution.iloc[row_idx[0],year]        
            else: 
                prob_term[term,year] = 0.0
    
    # create dataframe in one step
    viz_df = pd.DataFrame({terms[0]:prob_term[0,:],
                           terms[1]:prob_term[1,:],
                           terms[2]:prob_term[2,:],
                           terms[3]:prob_term[3,:],
                           terms[4]:prob_term[4,:],
                           terms[5]:prob_term[5,:]})
    
    # transpose dataframe and label columns as years
    viz_df = viz_df.rename(index={0: 1970, 1: 1971, 2: 1972, 3: 1973, 
                                  4: 1974, 5: 1975, 6: 1976, 7: 1977, 
                                  8: 1978, 9: 1979, 10: 1980, 11: 1981,
                                  12: 1982, 13: 1983, 14: 1984, 15: 1985,
                                  16: 1986, 17: 1987, 18: 1988, 19: 1989,
                                  20: 1990, 21: 1991, 22: 1992, 23: 1993, 
                                  24: 1994, 25: 1995, 26: 1996, 27: 1997,
                                  28: 1998, 29: 1999, 30: 2000, 31: 2001,
                                  32: 2002, 33: 2003, 34: 2004, 35: 2005,
                                  36: 2006, 37: 2007, 38: 2008, 39: 2009,
                                  40: 2010, 41: 2011, 42: 2012, 43: 2013,
                                  44: 2014, 45: 2015, 46: 2016, 47: 2017,
                                  48: 2018, 49: 2019})
    
    # use years as separate column
    viz_df = viz_df.reset_index().rename(columns= {'index':'year'})
    
    # melt to longformat
    viz_df = pd.melt(viz_df, id_vars='year', value_vars=[term1,term2,term3,term4,term5,term6])
    
    # rename column names
    viz_df = viz_df.rename(columns= {'variable':'term','value':'term_frequency'})

    return viz_df