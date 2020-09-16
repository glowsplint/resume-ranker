## Resume Ranker

This repository contains the codebase for the [resume-ranker project](resumeranker.herokuapp.com). Given a set of input keywords, it ranks a pool of `.pdf` and `.docx` candidate profiles profiles by semantical relevance. This project is built with a Django backend, Vue frontend, and the Heroku platform for hosting.

### Dependencies

We categorise the primary dependencies by those used in production and in development. The development dependencies allow the Django development server to hot-reload off the Vue development server, enabling updates to be seen quickly without creating a production build each time.

| Production                                          | Version    |
| --------------------------------------------------- | ---------- |
| [**vuetify**](https://github.com/vuetifyjs/vuetify) | **2.2.28** |
| [axios](https://github.com/axios/axios)             | 0.19.2     |
| [fastapi](https://github.com/tiangolo/fastapi)      | 0.61.1     |
| [uvicorn](https://github.com/encode/uvicorn)        | 0.11.8     |
| [lodash](https://github.com/lodash/lodash)          | 4.17.15    |

| Development                                                                            | Version |
| -------------------------------------------------------------------------------------- | ------- |
| [webpack-bundle-tracker](https://www.npmjs.com/package/webpack-bundle-tracker/v/0.4.3) | 0.4.3   |

\*_In the dependency table above,_ **bold text** _denotes a Vue plugin._

The full npm dependency table can be found at `./vue-frontend/package.json` and can be installed via `cd vue-frontend npm install`.
The full python dependency table can be found at `./requirements.txt` and can be installed via `pip install -r requirements.txt`. Note that the `gunicorn` dependency is only used in Heroku deployment, but not in development.

## Deployment to Heroku

### Instructions

You will need to comment/uncomment certain lines in the vue.config.js file, located at `./vue-frontend/vue.config.js`. This will allow us to toggle between hot-reloading from the Vue development server while in development, to the built files in the `./vue-frontend/dist` directory in production.

Heroku is connected to GitHub. Simply `git push origin master` and Heroku will deploy from the latest version of the `master` branch.

### Heroku configurations

| Argument                | Value         |
| ----------------------- | ------------- |
| `DEBUG_COLLECTSTATIC`   | 1             |
| `DISABLE_COLLECTSTATIC` | 0             |
| `SECRET_KEY`            | \<SECRET_KEY> |

<!-- https://www.youtube.com/watch?v=dxgbgYtNzCw -->

## To-do

- Migrate to FastAPI + deploy
- Add deployment instructions
- Allow multi-part upload while retaining previously uploaded information in the same session
- Fix the font not rendering properly
- Fix the Heroku app providing different relevance scores from the offline version (check if caching is an issue)
- Add login with facebook/gmail
- Save data for logged in user
