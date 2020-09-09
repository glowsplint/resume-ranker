## Resume Ranker

This repository contains the codebase for the [resume-ranker project](resumeranker.herokuapp.com). Given a set of input keywords, it ranks a pool of `.pdf` and `.docx` candidate profiles profiles by semantical relevance. This project is built with a Django backend, Vue frontend, and the Heroku platform for hosting.

### Dependencies

We categorise the primary dependencies by those used in production and in development. The development dependencies allow the Django development server to hot-reload off the Vue development server, enabling updates to be seen quickly without creating a production build each time.

| Production                                                                    | Version    |
| ----------------------------------------------------------------------------- | ---------- |
| [**vuetify**](https://github.com/vuetifyjs/vuetify)                           | **2.2.28** |
| [axios](https://github.com/axios/axios)                                       | 0.19.2     |
| [django-heroku](https://www.npmjs.com/package/webpack-bundle-tracker/v/0.4.3) | 0.4.3      |
| [djangorestframework](https://github.com/axios/axios)                         | 3.11.0     |
| [gunicorn](https://github.com/benoitc/gunicorn)                               | 20.0.4     |
| [lodash](https://github.com/lodash/lodash)                                    | 4.17.15    |

| Development                                                                            | Version |
| -------------------------------------------------------------------------------------- | ------- |
| [django-cors-headers](https://github.com/adamchainz/django-cors-headers)               | 3.2.1   |
| [django-webpack-loader](https://github.com/axios/axios)                                | 0.7.0   |
| [webpack-bundle-tracker](https://www.npmjs.com/package/webpack-bundle-tracker/v/0.4.3) | 0.4.3   |

\*_In the dependency table above,_ **bold text** _denotes a Vue plugin._

The full npm dependency table can be found at `./vue-frontend/package.json` and can be installed via `cd vue-frontend npm install`
The full python dependency table can be found at `./requirements.txt` and can be installed via `pip install -r requirements.txt`. Note that the `gunicorn` dependency is only used in Heroku deployment, but not in development.

## Transitioning from development to deployment

You will need to comment/uncomment certain lines in the vue.config.js file, located at `./vue-frontend/vue.config.js`. This will allow us to toggle between hot-reloading from the Vue development server while in development, to the built files in the `./vue-frontend/dist` directory in production.

## Heroku configuration

| Argument                | Value         |
| ----------------------- | ------------- |
| `DEBUG_COLLECTSTATIC`   | 1             |
| `DISABLE_COLLECTSTATIC` | 0             |
| `SECRET_KEY`            | \<SECRET_KEY> |

<!-- https://www.youtube.com/watch?v=dxgbgYtNzCw -->

### To-do

1. Fix "Upload" button clearing the keywords
2. Allow multi-part upload while retaining previously uploaded information in the same session
3. Fix the CSRF token security issue
4. Fix the /admin login bug to allow superuser access
5. Fix the font not rendering properly
6. Fix the Heroku app providing different relevance scores from the offline version (check if caching is an issue)
