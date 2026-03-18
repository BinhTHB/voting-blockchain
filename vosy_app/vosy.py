from flask import Flask
from flask import render_template, redirect, request, jsonify, flash
from math import *

from utils import get_ip

import datetime, time
import json
import codecs
import requests
import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

app = Flask(__name__)
app.secret_key = 'super_secret_voting_key'
port = 8080

@app.context_processor
def my_utility_processor():

    def len_list(li):
        return len(li)

    def maxvote(post):
        maxvote = 0
        for answer, votes in post['answers'].items():
            maxvote = max(maxvote,len(votes))

        return maxvote

    return dict(len=len_list, maxvote=maxvote)


# The node with which our application interacts, there can be multiple
# such nodes as well.
CONNECTED_NODE_ADDRESS = "http://0.0.0.0:5000"

posts = []


def fetch_posts():
    """
    Function to fetch the chain from a blockchain node, parse the
    data and store it locally.
    """
    get_chain_address = "{}/open_surveys".format(CONNECTED_NODE_ADDRESS)
    response = requests.get(get_chain_address)
    if response.status_code == 200:
        content = []
        data = json.loads(response.content)
        surveys = data['surveys']

        global posts
        posts = sorted(surveys, key=lambda k: k['timestamp'],
                       reverse=True)


@app.route('/')
def index():
    fetch_posts()

    # Fetch chain data for Blockchain Explorer
    chain_address = "{}/chain".format(CONNECTED_NODE_ADDRESS)
    response = requests.get(chain_address)
    chain_data = []
    if response.status_code == 200:
        chain_data = json.loads(response.content).get('chain', [])
        # reverse the chain to show latest blocks first
        chain_data = chain_data[::-1]

    # Fetch pending transactions
    pending_tx_address = "{}/pending_tx".format(CONNECTED_NODE_ADDRESS)
    response = requests.get(pending_tx_address)
    pending_txs = []
    if response.status_code == 200:
        pending_txs = json.loads(response.content)

    return render_template('index.html',
                           title='Voting System Dashboard',
                           posts=posts,
                           chain=chain_data,
                           pending_txs=pending_txs,
                           node_address=CONNECTED_NODE_ADDRESS,
                           readable_time=timestamp_to_string)

@app.route('/mine', methods=['GET','POST'])
def mine():
    
    url = '{}/mine'.format(CONNECTED_NODE_ADDRESS)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            try:
                data = response.json()['response']
                flash(data, "success")
            except requests.exceptions.JSONDecodeError:
                flash(f"Lỗi phản hồi từ Node: Không thể phân tích chuỗi JSON. Raw: {response.text}", "danger")
            except KeyError:
                flash(f"Phản hồi từ Node thiếu thuộc tính 'response'. Raw: {response.text}", "danger")
        else:
            flash(f"Lỗi khi yêu cầu Node đào block. HTTP Status: {response.status_code}", "danger")
    except requests.exceptions.RequestException as e:
        flash(f"Không thể kết nối đến Node để đào block: {e}", "danger")
        
    return redirect('/')

@app.route('/pending_tx', methods=['GET','POST'])
def get_pending_tx():

    url = '{}/pending_tx'.format(CONNECTED_NODE_ADDRESS)
    response = requests.get(url)

    data = response.json()

    return jsonify(data)

@app.route('/list_nodes', methods=['GET','POST'])
def get_list_nodes():

    url = '{}/list_nodes'.format(CONNECTED_NODE_ADDRESS)
    response = requests.get(url)

    data = response.json()

    return jsonify(data)


@app.route('/submit', methods=['POST'])
def submit_textarea():
    """
    Endpoint to create a new transaction via our application.
    """

    author = get_ip(request.remote_addr)
    questionid = request.form["questionid"]
    question = request.form["question"]
    answersList = [a.strip() for a in request.form["answer"].split('|')]
    opening_time = int(request.form["opening_time"])*60
    answers = {}

    for answer in answersList:
        answers[answer] = []

    post_object = {
        'type' : 'open',
        'content' : {
            'questionid': questionid,
            'question': question,
            'answers': answers,
            'opening_time': opening_time,
            'status': 'opening',
            'author': author + ':' + str(port),
            'timestamp': time.time()
        }
    }

    # Submit a transaction
    new_tx_address = "{}/new_transaction".format(CONNECTED_NODE_ADDRESS)

    requests.post(new_tx_address,
                  json=post_object,
                  headers={'Content-type': 'application/json'})

    #call smart contract to count down
    contract_object = {
        'type' : 'execute',
        'content': {
            'contract': 'count_down_opening_time',
            'arguments': [opening_time, author, questionid, CONNECTED_NODE_ADDRESS],
            'author': author + ':' + str(port)
        }
    }

    requests.post(new_tx_address,
                  json=contract_object,
                  headers={'Content-type': 'application/json'})

    flash("Giao dịch tạo cuộc bầu cử đang chờ xử lý (Pending in Mempool)", "warning")
    return redirect('/')

@app.route('/close_survey', methods=['GET','POST'])
def close_survey():
    """
    Endpoint to create a new transaction via our application.
    """

    author = get_ip(request.remote_addr)
    questionid = request.args.get('id')

    post_object = {
        'type' : 'close',
        'content' : {
            'questionid': questionid,
            'author': author + ':' + str(port),
            'timestamp': time.time()
        }
    }

    # Submit a transaction
    new_tx_address = "{}/new_transaction".format(CONNECTED_NODE_ADDRESS)

    requests.post(new_tx_address,
                  json=post_object,
                  headers={'Content-type': 'application/json'})

    flash("Giao dịch đóng cuộc bầu cử đang chờ xử lý (Pending in Mempool)", "warning")
    return redirect('/')

@app.route('/vote', methods=['GET','POST'])
def vote():
    """
    Endpoint to create a new transaction via our application.
    """

    author = get_ip(request.remote_addr)
    questionid = request.args.get('id')
    answer = request.args.get('answer').strip()

    post_object = {
        'type' : 'vote',
        'content' : {
            'questionid': questionid,
            'author': author + ':' + str(port),
            'vote': answer,
            'timestamp': time.time()
        }
    }

    # Submit a transaction
    new_tx_address = "{}/new_transaction".format(CONNECTED_NODE_ADDRESS)

    requests.post(new_tx_address,
                  json=post_object,
                  headers={'Content-type': 'application/json'})

    flash("Giao dịch bỏ phiếu đang chờ xử lý (Pending in Mempool)", "warning")
    return redirect('/')

@app.route('/update_chaincode', methods=['GET','POST'])
def update_chaincode():
    file = os.path.join(__location__,'chaincode.py')
    code = ''

    with codecs.open(file,encoding='utf8',mode='r') as inp:
        code = inp.read()

    author = get_ip(request.remote_addr)

    post_object = {
        'type' : 'smartcontract',
        'content' : {
            'code': code,
            'author': author + ':' + str(port),
            'timestamp': time.time()
        }
    }

    # Submit a transaction
    new_tx_address = "{}/new_transaction".format(CONNECTED_NODE_ADDRESS)

    requests.post(new_tx_address,
                  json=post_object,
                  headers={'Content-type': 'application/json'})

    flash("Giao dịch cập nhật chaincode đang chờ xử lý (Pending in Mempool)", "warning")
    return redirect('/')
    

def timestamp_to_string(epoch_time):
    return datetime.datetime.fromtimestamp(epoch_time).strftime('%H:%M')


if __name__ == '__main__':
    from argparse import ArgumentParser

    myIP = get_ip()
    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=8080, type=int, help='port to listen on')
    parser.add_argument('--host', default='0.0.0.0', type=str, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    if ':' in args.host:
        CONNECTED_NODE_ADDRESS = 'http://{}'.format(args.host)
    else:
        CONNECTED_NODE_ADDRESS = 'http://{}:5000'.format(args.host)

    print('My ip address : ' + get_ip())

    app.run(host='0.0.0.0', port=port, debug = True, threaded = True)

