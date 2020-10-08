## Resume Ranker

This repository contains the code for the [resume-ranker project](resumeranker.herokuapp.com). Given a set of input keywords, it ranks a pool of `.pdf` and `.docx` candidate profiles profiles by edit-distance relevance, allowing the recruiter to identify and prioritise the most relevant candidates from a large pool of candidates. This project is built with a FastAPI (Starlette) backend, Vue frontend; and uses the Heroku platform for deployment.

### Dependencies

The full npm dependency table can be found at `./vue-frontend/package.json` and can be installed via `cd vue-frontend npm install`.
The full Python dependency table can be found at `./requirements.txt` and can be installed via `pip install -r requirements.txt`.

## Deployment to Heroku

### Instructions

You will need to comment/uncomment certain lines in the vue.config.js file, located at `./vue-frontend/vue.config.js`. This will allow us to toggle between hot-reloading from the Vue development server while in development, to the built files in the `./vue-frontend/dist` directory in production.

Heroku is connected to this GitHub. Run `git push origin master` and deploy manually from the Heroku GUI. Heroku will deploy from the latest version of the `master` branch.

## Developer Usage

1. Document class: Calculates the score value of a profile, from a file, parsing function, and input phrases.
2. Relevance class: Aggregates the score value across all the profiles, by taking in a list of Document objects.

## Usage

The Relevance class takes in a list of Document objects:

```python
docx_doc_list = [Document(item, extract_docx, input_phrases) for item in docx_list]
pdf_doc_list = [Document(item, extract_pdf, input_phrases) for item in pdf_list]
```

After that, we create an instance of the Relevance class:

```python
relevance = Relevance(docx_doc_list)
relevance.update(pdf_doc_list)
```

or:

```python
relevance = Relevance()
relevance.update(docx_doc_list)
relevance.update(pdf_doc_list)
```

or, alternatively:

```python
docx_doc_list.extend(pdf_doc_list)
relevance = Relevance(docx_doc_list)
```

All three approaches are functionally equivalent. We find the scores by inspecting the `scores` property of the Relevance instance:

## Rationale for metric

We use partial_ratio over token_set_ratio because we want to preserve the order of input words. Currently, our final metric is simply the sum of partial ratios. However, the metric used here should be extensively tested. Other ideas include taking the mean of partial ratios (scaled by the number of words in the profile Document) - the idea being that there should be a penalty for being too verbose in your profile.

## To-do

1. Rank keyword search by importance - must have (mandatory skills) vs. optional
2. Relevance breakdown
3. Move logic to client-side
   - Find pdf parser
   - Find docx parser
   - Find levenshtein implementation
   - Find/write partial ratio in JS (https://github.com/seatgeek/fuzzywuzzy/blob/master/fuzzywuzzy/fuzz.py)
4. Implement CI/CD solution
