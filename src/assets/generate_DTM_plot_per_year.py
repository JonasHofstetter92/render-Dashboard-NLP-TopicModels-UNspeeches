# -*- coding: utf-8 -*-
"""
Created on Thu May 13 08:22:19 2021
@author: jonas
"""
## import packages

# save and load
import pickle

# gensim
from gensim.models import ldaseqmodel

# vizualization
import pyLDAvis
##.....................................................

## Dynamic Topic Modelling (DTM)
# Produce & export interactive .html files for specific years of DTM:

# Load pre-trained DTM model from disk.
ldaseq = ldaseqmodel.LdaSeqModel.load('C:/Users/josch/Dropbox/MDA/exam_project/MDA_Multipage_App/saved_models/finalDTM_model')

# Load corresponding saved bow_corpus from disk
file_name = "C:/Users/josch/Dropbox/MDA/exam_project/MDA_Multipage_App/saved_models/bow_corpus_DTM.pkl"
open_file = open(file_name, "rb")
bow_corpus = pickle.load(open_file)
open_file.close()       
       
# Export .html files of DTM for specific time slice (year)
for time in range(0,49):
    # extract viz objects from DTM model
    doc_topic, topic_term, doc_lengths, term_frequency, vocab = ldaseq.dtm_vis(time=time, corpus=bow_corpus)
    # prepare viz
    vis_dtm = pyLDAvis.prepare(topic_term_dists=topic_term, doc_topic_dists=doc_topic, doc_lengths=doc_lengths, vocab=vocab, term_frequency=term_frequency)
    # save as .html file
    pyLDAvis.save_html(vis_dtm, 'C:/Users/josch/Dropbox/MDA/exam_project/MDA_Multipage_App/assets/DTM_{}.html'.format(time+1970))