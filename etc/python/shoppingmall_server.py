import pymongo
from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db= client.dbsparta

def run_server():
    server = Flask('주문서버')

    @server.route('/')
    def home():
        return render_template('Homework1.html')

    @server.route('/orders', methods=['POST'])
    def write_order():
        name_receive = request.form['name_give']
        count_receive = request.form['count_give']
        address_receive = request.form['address_give']
        number_receive = request.form['number_give']
        order = {
            'name' : name_receive,
            'count' : count_receive,
            'address' : address_receive,
            'number' : number_receive
        }
        db.orders.insert_one(order)
        return jsonify({'result':'success', 'msg': '주문 성공!'})

    @server.route('/orders', methods=['GET'])
    def read_order():
        orders = list(db.orders.find({},{'_id':0}))
        return jsonify({'result':'success', 'orders': orders})

    server.run('0.0.0.0', port=5000, debug=True)

run_server()
