# -*- coding: utf-8 -*-
from flask import Flask, redirect, url_for, render_template, request, send_file, send_from_directory, make_response
import requests
import datetime
import json
import random
import trash
global false, null, true
false = null = true = ""
app = Flask(__name__)


@app.route('/trash', methods=['POST'])
def what_trash():
    trash_name = request.form['trash']
    res = trash.trash(trash_name)
    status = 0
    if '属于' in res:
        status = 1
    ans = {
        'status': status,
        'content': res
    }
    return json.dumps(ans)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=1026)  # host='0.0.0.0', port=80,
