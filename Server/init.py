'''

Code comments :

    Exit codes reference :
        -1 : Wrong server arguments passed


    Server Startup:
        python init.py <hostname> <port> (ex. python init.py localhost 22236)

    Documentation (please add all the links and api references here):

        1. <nitin> : recommended production deployment, but for the demo we'll use only this Flask shit!



                +----------+
                | Client 2 |
                +----------+
                      |
                      V
+----------+      +-------+      +----------+
| Client 1 |----->| nginx |<-----| Client 3 |
+----------+      +-------+      +----------+
                      ^
                      |
                      V
           /--------------------\
           | useful nginx stuff |
           | like asset serving |
           | and rate limiting  |
           \--------------------/
                      |
                      V
               +-------------+
               | WSGI server |
               +-------------+

            http://flask.pocoo.org/docs/deploying/


'''



'''******************************      IMPORTS     ******************************'''

import sys

# server startup check
if len(sys.argv) != 3:
    print "Startup usage : python init.py <hostname> <port>"
    exit(-1)

from flask import Flask, jsonify, redirect, url_for, request
import os
import subprocess

'''******************************     IMPORTS     ******************************'''













'''******************************     SETUP AND GLOBALS     ******************************p'''

app = Flask('vwe_server')

'''******************************     SETUP AND GLOBALS     ******************************p'''















'''******************************     UTILITY FUNCTIONS     ******************************p'''


'''******************************     UTILITY FUNCTIONS     ******************************p'''














'''******************************     MAIN FUNCTIONALITY     ******************************p'''

@app.route('/' , methods = ['GET','POST'])
def home():
    return redirect(url_for('help'))



# TODO : after adding any route please add it to the help response
@app.route('/help', methods = ['GET'])
def help():
    response = dict()
    response["status"] = "success"
    response["response"] = " 1. GET /help for options "
    return jsonify(response)

'''******************************     MAIN FUNCTIONALITY     ******************************p'''






'''******************************     PROGRAM FLOW     ******************************p'''

if __name__== '__main__':
    # leave debug on for trace
    app.run(host=sys.argv[1], port=int(sys.argv[2]), debug=True)

'''******************************     PROGRAM FLOW     ******************************p'''



