#!/usr/bin/env python
# coding: utf-8

# # Resume Ranker
# Developed by [Tym Teo](https://www.linkedin.com/in/tym-teo/), May 2020.

# ## Overview
# This script allows the recruiter to identify and prioritise the most relevant candidates from a large pool of candidates, by ranking a provided set of profiles by relevance. It requires a provided set of input keywords (rankings are provided based on the number of keyword matches), and prints the output to a text file `Ranking.txt` in the current directory.

# ## Usage
# ### This script can be used in several ways:
# 1. Run the `ranker.ipynb` notebook directly
# 2. Run the `ranker.py` python script directly (`ranker.py` is the `.py` version of the notebook)
# 3. Import the `ranker.py` into a separate python script (we use this approach in the app version of this)
#     - The app version can be found [here](https://resumeranker.herokuapp.com).
#
# ### For options 1 and 2:
# It currently assumes that the inputs will be structured as follows:
# 1. Resumes/Profiles in a subdirectory `./Resumes/*`
# 2. Input key phrases in the same directory `./keywords.txt`
#
# This script only supports `.pdf` and `.docx` files.

# ## Dependencies
# - `pdfminer.six` module for parsing .pdf documents. The latest version has to be used, as older versions do not contain the `high_level` submodule
# - `docx2txt` module for parsing .docx files.

# ## Classes
# 1. Document class: Calculates the score value of a profile, from a file, parsing function, and input phrases.
# 2. Relevance class: Aggregates the score value across all the profiles, by taking in a list of Document objects.

# ## Usage
# The Relevance class takes in a list of Document objects - let's define that first:
# ```python
# docx_doc_list = [Document(item, extract_docx, input_phrases) for item in docx_list]
# pdf_doc_list = [Document(item, extract_pdf, input_phrases) for item in pdf_list]
# ```
#
# After that, we create an instance of the Relevance class. You could do this:
#
# ```python
# relevance = Relevance(docx_doc_list)
# relevance.add(pdf_doc_list)
# ```
#
# or, alternatively:
#
# ```python
# relevance = Relevance()
# relevance.add(docx_doc_list)
# relevance.add(pdf_doc_list)
# ```
#
# Both the above code blocks will achieve the same outcome. You could even merge the two lists before adding it to the Relevance instance. The resulting code would be neater and is the preferred approach.
#
# ```python
# docx_doc_list.extend(pdf_doc_list)
# relevance = Relevance(docx_doc_list)
# ```
#
# We find the scores by inspecting the scores() property of the Relevance instance:
# ```python
# relevance.scores
# ```

# ## Rationale
# We use partial_ratio over token_set_ratio because we want to preserve the order of input words. Currently, our final metric is simply the sum of partial ratios. However, the metric used here should be extensively tested. Other ideas include taking the mean of partial ratios (scaled by the number of words in the profile Document) - the idea being that there should be a penalty for being too verbose in your profile.
#
# ## Possible areas of improvement
# 1. Experiment with the metric
# 2. Add the spaCy language model version to the app if Heroku's free dyno constraints are not binding
# 3. Illustrate the breakdowns of how the final score metric came to be, for every profile

# In[1]:


import json
import os

from collections import OrderedDict
from typing import List, Callable
from docx2txt import process as extract_docx
from pdfminer.high_level import extract_text as extract_pdf
from fuzzywuzzy import fuzz
from tempfile import SpooledTemporaryFile


# In[2]:


class Document:
    """
    The Document class contains all the information of a single profile.
    When a class instance is created:
    1. The document is parsed from the provided <filename> via the <parsing_function>
    2. The associated score is generated and stored as self.score

    The <file> parameter accepts both filepaths and InMemoryUploadedFile objects.
    This means that Documents can be created from either of these.
    """

    def __init__(self, file, parsing_function: Callable[[str], str], input_phrases: str):
        self.parsing_function = parsing_function
        self.input_phrases = input_phrases
        self.file = file
        self.parsed_text = self.parsing_function(file)
        self.parsed_text = Document.split_and_rejoin(self.parsed_text)

        if isinstance(self.file, str):
            self.filename = self.file
        elif isinstance(self.file, SpooledTemporaryFile):
            self.filename = self.file.filename
        else:
            self.filename = self.file.name

    def __repr__(self):
        return f"Document(file='{self.file}')"

    @staticmethod
    def split_and_rejoin(text: str) -> str:
        return ' '.join(text.split())

    @property
    def score(self):
        """
        Calculates the relevance score as follows:
        1. Finds the partial ratio of every input phrase with the giant profile corpus in a generator
        2. The relevance score is the sum of all of these partial ratios
        """
        return sum((fuzz.partial_ratio(input_phrase, self.parsed_text) for input_phrase in self.input_phrases))


# In[3]:


class Relevance:
    """
    The Relevance class contains all the information across all profiles.

    ----------
    Attributes
    ----------
    collated_documents : Attribute
        A list of Document objects (can be either .pdf or .docx)

    -------
    Methods
    -------
    add : Method
        Adds file_list of type <List[Document]> to self.collated_documents.
        Files within file_list must all be the same file type (must be either .pdf or .docx)

    scores : Property
        Gets the scores of all the different loaded Document objects

    breakdown : NotImplemented
        Returns the breakdown of scores into its components (i.e. how the score was derived)
    """

    def __init__(self, file_list: List = None):
        self.collated_documents = []
        if file_list is None:
            file_list = []
        self.add(file_list)

    def add(self, file_list: List[Document]):
        # Ensures that there are no duplicate Document objects in self.collated_documents
        for document in file_list:
            if document not in self.collated_documents:
                self.collated_documents.append(document)

    @property
    def scores(self):
        unsorted_scores = {
            document.filename: document.score for document in self.collated_documents}
        return OrderedDict(sorted(unsorted_scores.items(), key=lambda x: x[1], reverse=True))

    @property
    def breakdown(self):
        pass


# In[4]:


# %%time
if __name__ == '__main__':
    with open('./keywords.txt') as file:
        input_phrases = file.read().split('\n')
        input_phrases.remove('')
    print(f'input_phrases = {input_phrases}')

    def create_list(ending):
        target = 'resumes'
        return [f'{target}/{f}' for f in os.listdir(f'./{target}') if f.endswith(ending)]

    pdf_list = create_list('.pdf')
    docx_list = create_list('.docx')
    docx_doc_list = [Document(item, extract_docx, input_phrases)
                     for item in docx_list]
    pdf_doc_list = [
        Document(item, extract_pdf, input_phrases) for item in pdf_list]
    docx_doc_list.extend(pdf_doc_list)
    relevance = Relevance(docx_doc_list)


# In[5]:


# relevance.scores
