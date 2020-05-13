## Stack

|          | Choice 1   | Choice 2       |
| -------- | ---------- | -------------- |
| Backend  | **Django** | ~~Flask~~      |
| Database | ~~SQLite~~ | **PostgreSQL** |
| Frontend | ~~React~~  | **Vue**        |
| Platform | **Heroku** | ~~Firebase~~   |

The Django framework was chosen because of the ease of implementing login functionality at a later stage. Vue was chosen as I have experience working in it over React. Heroku is chosen arbitrarily (could have used Firebase as well).

## MVP by end of May:

1. Uses batch processing (instead of one-by-one processing)
2. Uses Levenshtein distance for comparison -- more lightweight
3. Uses sum of partial ratio as the final value
4. No persistent file storage; no logins

## Tasks

1. ~~Set up Django project~~ (5/5)
2. ~~Set up Vue project~~ (6/5)
3. ~~Enable Django hot-reloading in development serving Vue frontend~~ (8/5)
4. ~~Rewrite the script to use Levenshtein distance instead of the spaCy language models~~ (11/5)
5. ~~Deploy Vue frontend with Django backend on Heroku platform~~ (12/5)
6. ~~Set up Vue upload file dialog~~ (13/3)
7. ~~Set up Vue text input space~~ (13/3)
8. Set up API between frontend and backend
9. Set up Python script to run on the API call
10. Set up Vue frontend to display the API response
11. Fix the /admin login thingy

## Dependencies

| Dependency                                                                             | Version |
| -------------------------------------------------------------------------------------- | ------- |
| [**vuetify**](https://github.com/vuetifyjs/vuetify)                                    | 2.2.28  |
| [vue-file-agent](https://github.com/safrazik/vue-file-agent)                           | 1.7.1   |
| [webpack-bundle-tracker](https://www.npmjs.com/package/webpack-bundle-tracker/v/0.4.3) | 0.4.3   |

\*_In the dependency table above,_ **bold text** _denotes a Vue plugin._

## Transitioning from development to deployment

You will need to comment/uncomment certain lines in the vue.config.js file, located at `'.\vue-frontend\vue.config.js'`.
