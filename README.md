## Resume Ranker

This repository contains the codebase for the [resume-ranker project](resumeranker.herokuapp.com). Given a set of input keywords, it ranks a pool of `.pdf` and `.docx` candidate profiles profiles by edit-distance relevance. This project is built with a FastAPI (Starlette) backend, Vue frontend, and the Heroku platform for deployment.

### Dependencies

The full npm dependency table can be found at `./vue-frontend/package.json` and can be installed via `cd vue-frontend npm install`.
The full Python dependency table can be found at `./requirements.txt` and can be installed via `pip install -r requirements.txt`.

## Deployment to Heroku

### Instructions

You will need to comment/uncomment certain lines in the vue.config.js file, located at `./vue-frontend/vue.config.js`. This will allow us to toggle between hot-reloading from the Vue development server while in development, to the built files in the `./vue-frontend/dist` directory in production.

Heroku is connected to GitHub. Simply `git push origin master` and manually deploy from the Heroku GUI. Heroku will deploy from the latest version of the `master` branch.

## To-do

- Allow multi-part upload while retaining previously uploaded information in the same session
- Fix the font not rendering properly
- Add login with facebook/gmail
- Save data for logged in user
