# docker-env

simple docker image that shows the use of environment variables to affect the application at runtime

## Usage

e.g. set background colour to yellow

`docker run --env APP_COLOUR=yellow -p 5000:5000 docker-env`
