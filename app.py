from datetime import datetime
import pickle
import warnings
import flask
app = flask.Flask(__name__)

warnings.filterwarnings("ignore")
load = pickle.load(open('phishing.pkl','rb'))

@app.route('/')
def index():
   print('Request for index page received')
   return flask.render('index.html')


@app.route('/hello', methods=['POST'])
def hello():
   name = flask.request.form.get('name')

   if name:
       print('Request for hello page received with name=%s' % name)
       name = load.predict([name])
       return flask.render('hello.html', name = name)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return flask.redirect(flask.url_for('index'))


if __name__ == '__main__':
   app.run()
