from flask import Flask
from flask_restful import Api
from config import app_config
from .orders import SpecificOrder, NewOrders, GetOrders,DeclineOrder,AcceptStatus,GetAcceptedOrders,DeclinedOrders,CompleteOrder,CompletedOrder

def create_app(config_stage):
    app = Flask(__name__)
    app.config.from_object(app_config[config_stage])

    api = Api(app)

    api.add_resource(SpecificOrder, '/api/v1/orders/<int:id>')
    api.add_resource(NewOrders, '/api/v1/orders')
    api.add_resource(GetOrders, '/api/v1/orders/allorders')
    api.add_resource(DeclineOrder, '/api/v1/orders/denied/<int:id>')
    api.add_resource(AcceptStatus,'/api/v1/orders/approve/<int:id>')
    api.add_resource(GetAcceptedOrders,'/api/v1/orders/approved')
    api.add_resource(DeclinedOrders,'/api/v1/orders/declinedorders')
    api.add_resource(CompleteOrder,'/api/v1/orders/completeorder/<int:id>')
    api.add_resource(CompletedOrder,'/api/v1/orders/completedorders')




    return app
