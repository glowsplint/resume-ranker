#!/usr/bin/env python
# coding: utf-8

import os

from collections import OrderedDict
from typing import List, Callable
from docx2txt import process as extract_docx
from pdfminer.high_level import extract_text as extract_pdf
from fuzzywuzzy import fuzz
from tempfile import SpooledTemporaryFile


class Document:
    """
    The Document class contains all the information of a single profile.
    When a class instance is created:
    1. The document is parsed from the provided <filename> via the <parsing_function>
    2. The associated score is generated and stored as self.score

    The <filename> parameter accepts both filepaths and InMemoryUploadedFile objects.
    This means that Documents can be created from either of these.
    """

    def __init__(self, filename, parsing_function: Callable[[str], str], input_phrases: str):
        self.parsing_function = parsing_function
        self.input_phrases = input_phrases
        self.filename = filename
        self.parsed_text = self.parsing_function(filename)
        self.parsed_text = Document.split_and_rejoin(self.parsed_text)

        if isinstance(self.filename, str):
            self.filename = self.filename
        elif isinstance(self.filename, SpooledTemporaryFile):
            self.filename = self.filename.filename
        else:
            self.filename = self.filename.name

    def __repr__(self) -> str:
        return f"Document(filename='{self.filename}')"

    @staticmethod
    def split_and_rejoin(text: str) -> str:
        return ' '.join(text.split())

    @property
    def score(self) -> int:
        """
        Calculates the relevance score as follows:
        1. Finds the partial ratio of every input phrase with the giant profile corpus in a generator
        2. The relevance score is the sum of all of these partial ratios
        """
        return sum((fuzz.partial_ratio(input_phrase, self.parsed_text) for input_phrase in self.input_phrases))


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
    update : Method
        Updates self.collated_documents with file_list: List[Document].
        Files within file_list must all be the same filename type (must be either .pdf or .docx)

    scores : Property
        Gets the scores of all the different loaded Document objects

    breakdown : NotImplemented
        Returns the breakdown of scores into its components (i.e. how the score was derived)
    """

    def __init__(self, file_list: List = None):
        self.collated_documents = set()
        if file_list is None:
            file_list = []
        self.update(file_list)

    def update(self, file_list: List[Document]):
        self.collated_documents.update(file_list)

    @property
    def scores(self):
        unsorted_scores = {
            document.filename: document.score for document in self.collated_documents}
        return OrderedDict(sorted(unsorted_scores.items(), key=lambda x: x[1], reverse=True))

    @property
    def breakdown(self):
        pass


if __name__ == '__main__':
    with open('./keywords.txt') as filename:
        input_phrases = filename.read().split('\n')
        input_phrases.remove('')
    print(f'input_phrases = {input_phrases}')

    def create_list(ending):
        target = 'data'
        return [f'{target}/{f}' for f in os.listdir(f'./{target}') if f.endswith(ending)]

    pdf_list = create_list('.pdf')
    docx_list = create_list('.docx')
    docx_doc_list = [Document(item, extract_docx, input_phrases)
                     for item in docx_list]
    pdf_doc_list = [
        Document(item, extract_pdf, input_phrases) for item in pdf_list]
    docx_doc_list.extend(pdf_doc_list)
    relevance = Relevance(docx_doc_list)


# relevance.scores
