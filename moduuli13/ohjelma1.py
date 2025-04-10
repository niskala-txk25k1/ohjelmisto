#!/usr/bin/env python3
from flask import Flask, request

def is_prime(val):
    for n in range(2, val):
        if (val % n == 0):
            return False
    return True

app = Flask(__name__)
@app.route('/alkuluku/<num>')
def handle(num):
    ret = {
        "Number" : num,
        "isPrime" : is_prime(int(num))
    }
    return ret

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
