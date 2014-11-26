from flask import Flask, Response, request
from subprocess import check_output

app = Flask(__name__)


@app.route('/build')
def api_root():
    args = request.args
    cmd = [args.get('cmd'), args.get('file'), '-o', args.get('out')]
    print cmd
    try:
        out = check_output(cmd)
        return out + "</br>Build Success!"
    except Exception, e:
        return e


if __name__ == '__main__':
    app.run()
