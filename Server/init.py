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

        2. <nitin> : QR Code generation in python : https://pypi.org/project/PyQRCode/

                Create an SVG based on transaction id
                Store SVG with name transaction_id.svg in the transactions_dir
                send the image through HTTP response




'''



'''******************************      IMPORTS     ******************************'''

import sys

# server startup check
if len(sys.argv) != 3:
    print "Startup usage : python init.py <hostname> <port>"
    exit(-1)

from flask import Flask, jsonify, redirect, url_for, request
import os
import pyqrcode
'''******************************     IMPORTS     ******************************'''













'''******************************     SETUP AND GLOBALS     ******************************p'''

app = Flask('vwe_server')

# Hack instead of using db
storage_dir = os.getcwd() + "/Storage/" # ../../whatever/VWE/Storage
merchant_dir = storage_dir + "merchants/"
transactions_dir = storage_dir + "transactions/"

'''******************************     SETUP AND GLOBALS     ******************************p'''















'''******************************     UTILITY FUNCTIONS     ******************************p'''

def checkMerchantStatus(merchantId):
    if not os.path.isfile(merchant_dir+merchantId):
        return False
    return True

def generateGUID():
    # TODO
    pass

def storeTransaction(uniqueGUID,merchantId,items_list):
    # TODO
    pass


def generateQR(uniqueGUID):
    # TODO : check documentation
    qr = pyqrcode.create(uniqueGUID)
    qr.svg(transactions_dir+uniqueGUID+".svg", scale=8)

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


# STEP 1
# recieves a json object with items/amounts, creates a transaction entry, returns QR code
@app.route('/registerTransaction/<string:merchantId>', methods = ['POST'])
def registerTransaction(merchantId):
    response = {}

    # Check for merchant existance and permissions
    if not checkMerchantStatus(merchantId):
        response["status"] = False
        return jsonify(response)

    items_list = request.get_json()
    print "Transaction registration recieved : " + str(items_list)

    # generate unique transaction id (GUID)
    uniqueGUID = generateGUID()

    # create a file in the transactions_dir with the required details and name it with transaction id
    storeTransaction(uniqueGUID,merchantId,items_list)

    # generate QR code with transaction id from previous step (image https://pypi.org/project/PyQRCode/)
    # store QR image in transaction_dir
    generateQR(uniqueGUID)

    # wrap image in response and return it
    # TODO

    response["status"] = True
    return jsonify(response)




'''******************************     MAIN FUNCTIONALITY     ******************************p'''






'''******************************     PROGRAM FLOW     ******************************p'''

if __name__== '__main__':
    # leave debug on for trace
    app.run(host=sys.argv[1], port=int(sys.argv[2]), debug=True)

'''******************************     PROGRAM FLOW     ******************************p'''



