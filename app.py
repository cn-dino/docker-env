# for later
#  docker run --env VAR1=foo alpine:3 env



import os
from flask import Flask
app = Flask(__name__)

# get colour from environment, if not default to grey
colour = os.environ.get('APP_COLOUR', "grey")
print(colour)

@app.route('/')
def hello():
    return '<body style="background-color:{}">'.format(colour)

if __name__ == '__main__':
    app.run()
