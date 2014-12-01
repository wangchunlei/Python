#!/usr/bin/env python
from flask import Flask, Response, request, json,send_file
from subprocess import check_output
import xml.etree.ElementTree as ET

app = Flask(__name__)


@app.route('/', methods=['GET'])
def api_root():
    return 'Domas linux build server!'


@app.route('/build/qml_demo', methods=['POST'])
def api_post():
    data = request.get_json(force=True)
    company = data['company']
    product = data['product']
    copyright = data['copyright']
    version = data['version']
    fileversion = data['fileversion']
    buildversion = data['buildversion']
    tree = ET.parse('./config.xml')
    root = tree.getroot()
    for ele in root:
        if ele.tag == 'Company':
            ele.text = company
        elif ele.tag=='Product':
        	ele.text=product
        elif ele.tag=='CopyRight':
        	ele.text=copyright
        elif ele.tag=='Version':
        	ele.text=version
        elif ele.tag=='FileVersion':
        	ele.text=fileversion
        elif ele.tag=='BuildVersion':
        	ele.text=buildversion

    tree.write('./config.xml', encoding="UTF-8")
    out = check_output(['./compileproject'])
    return send_file('./%s/bin/domas' % buildversion, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
