from flask import Flask, request
from flask_restful import    Resource
from .models import Order, orders

# ADMIN VIEWS

class SpecificOrder(Resource):
    

    def get(self, id):
        order = Order().get_by_id(id)
        
        if order:
            return {"order": order.serialize()}, 200

        return {"message":"Order not found"}, 404

    def delete(self, id):
       
        order = Order().get_by_id(id)

        if order:
            orders.remove(order)
            return {"message":"order deleted successfully"},200
        return {"message":"Order not found"}, 404


class AcceptStatus(Resource):
    def put(self, id):
        # data = request.get_json()
        order = Order().get_by_id(id)

        if order:
            
            if order.status != "Pending":
                return {"message":"order already {}".format(order.status)},200

            order.status="approved"
            return {"message":"your order has been approved"},200
                
        return {"message":"Order not found"}, 404


class NewOrders(Resource):

    def post(self):
        
        data = request.get_json()
        # food_order= Order().get_food_by_name(data['name'])
        # if food_order:
        #     return {"message":"food with name {} already exists".format(food_order.name)}
        order = Order(data['name'], data["price"],data['description'])
        orders.append(order)

        return {"message":"Food order created"}, 201



class GetOrders(Resource):
    def get(self):
        return {"orders":[order.serialize() for order in orders]},200


class DeclineOrder(Resource):
    def put(self, id):
        # data = request.get_json()
        order = Order().get_by_id(id)

        if order:
            

            if order.status != "Pending":
                return {"message":"order already {}".format(order.status)}
            order.status = "declined"
            return {"message":"Order declined"}
        return {"message":"Order not found"}


class GetAcceptedOrders(Resource):
    '''Get the Orders accepted by admin'''
    def get(self):
        return {"orders":[order.serialize() for order in orders if order.status == "approved"]}




class CompleteOrder(Resource):
    '''mark an order as completed'''
    def put(self,id):
        order = Order().get_by_id(id)

        if order:
            if order.status == "completed" or order.status == "declined":
                return {"message":"order already {}".format(order.status)}

            if order.status == "Pending":
                return {"message":"please approve the order first "}

            if order.status == "approved":
                order.status = "completed"
                return {"message":"Your has been order completed awaiting delivery"}

        return {"message":"Order not found"}
class DeclinedOrders(Resource):
    def get(self):
        '''return all orders'''
        return {"declined orders":[order.serialize() for order in orders if order.status == "declined"]}

# view completed orders
class CompletedOrder(Resource):
    def get(self):
        return {"completed orders":[order.serialize() for order in orders if order.status == "completed"]},200



        


