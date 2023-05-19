from flask import Flask, request, jsonify
import requests
import random
from datetime import datetime

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json()

    order_id = req['queryResult']['parameters']['order_id']

    api_url = 'https://orderstatusapi-dot-organization-project-311520.uc.r.appspot.com/api/getOrderStatus'
    send = {'orderId': order_id}
    response = requests.post(api_url, json=send)

    if response.status_code == 200:
        data = response.json()
        shipment_date = data['shipmentDate']
        order_id = int(order_id)
        shipment_date = datetime.fromisoformat(shipment_date).strftime("%A, %d %b %Y")

        fulfillment_text = random.choice([f"The shipment date for order ID {order_id} is {shipment_date}.",
        f"Your order with ID {order_id} is scheduled to be shipped on {shipment_date}.",
        f"We have planned to ship your order, which has the ID {order_id}, on {shipment_date}.",
        f"The shipment for your order, identified by the ID {order_id}, is set to take place on {shipment_date}.",
        f"We have arranged for the shipment of your order, bearing the ID {order_id}, on {shipment_date}.",
        f"Your order {order_id} will be dispatched for shipment on {shipment_date}.",
        f"We are preparing to ship your order {order_id} on {shipment_date}.",
        f"The estimated shipping date for your order {order_id} is {shipment_date}.",
        f"We have scheduled your order {order_id} to be shipped on {shipment_date}.",
        f"Your order {order_id} is planned to be sent out for shipment on {shipment_date}.",
        f"The anticipated shipment date for your order {order_id} is {shipment_date}."])
        
    else:
        fulfillment_text = "Sorry, there was an error while fetching the shipment date."

    return jsonify({'fulfillmentText': fulfillment_text})

if __name__ == '__main__':
    app.run()