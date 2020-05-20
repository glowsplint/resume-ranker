## Stack

|          | Chosen     | ~~Alternative~~ |
| -------- | ---------- | --------------- |
| Backend  | **Django** | ~~Flask~~       |
| Frontend | **Vue**    | ~~React~~       |
| Platform | **Heroku** | ~~Firebase~~    |

## MVP by end of May:

1. Uses batch processing (instead of one-by-one processing)
2. Uses Levenshtein distance for comparison -- more lightweight
3. Uses sum of partial ratio as the final value
4. No logins
5. Single page application with one button "Upload" that sends files and input text to server, waits on response from server
6. Server should execute the script with the uploaded files and input text, and send a response back to the client

## Tasks

1. ~~Set up Django project~~ (5/5)
2. ~~Set up Vue project~~ (6/5)
3. ~~Enable Django hot-reloading in development serving Vue frontend~~ (8/5)
4. ~~Rewrite the script to use Levenshtein distance instead of the spaCy language models~~ (11/5)
5. ~~Deploy Vue frontend with Django backend on Heroku platform~~ (12/5)
6. ~~Set up Vue upload file dialog~~ (13/5)
7. ~~Set up Vue text input space~~ (13/5)
8. ~~Set up REST API between Django and Vue~~ (19/5)
9. ~~Set up Python script to run on the API call from client~~ (20/5)
10. ~~Set up Vue frontend to display the API response from server~~ (20/5)
11. Fix the CSRF token security issue
12. Fix the /admin login bug to allow superuser access

## Dependencies

### Main dependencies

We categorise the dependencies by those used in production and in development. The development dependencies allow the Django development server to hot-reload off the Vue development server, enabling updates to be seen quickly without creating a production build each time.

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
The full python dependency table can be found at `./requirements.txt` and can be installed via `python install -r requirements.txt`. Note that the `gunicorn` dependency is only used in Heroku deployment and not development.

## Transitioning from development to deployment

You will need to comment/uncomment certain lines in the vue.config.js file, located at `./vue-frontend/vue.config.js`. This will allow us to toggle between hot-reloading from the Vue development server while in development, to the built files in the `./vue-frontend/dist` directory in production.

## Heroku configuration

| Argument                | Value         |
| ----------------------- | ------------- |
| `DEBUG_COLLECTSTATIC`   | 1             |
| `DISABLE_COLLECTSTATIC` | 0             |
| `SECRET_KEY`            | \<SECRET_KEY> |

<!-- https://www.youtube.com/watch?v=dxgbgYtNzCw -->
