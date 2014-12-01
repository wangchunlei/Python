# all the imports
from flask import Flask, send_file
# create our little application :)
app = Flask(__name__)


@app.route('/download/')
def download():
    return send_file('./%s.sql' % 'schema', as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
