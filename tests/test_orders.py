import unittest
import json
from app import create_app


class TestOrders(unittest.TestCase):
    def setUp(self):
        self.app = create_app("testing")
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_create_order(self):
        data = {
            "name": "eggcurry",
            "price": 20,
            "description": "sweet eggs"
        }

        res = self.client.post(
            "/api/v1/orders",
            data=json.dumps(data),
            headers={"content-type": "application/json"}
        )

        self.assertEqual(res.status_code, 201)
        self.assertEqual(json.loads(res.data)['message'], "Food order created")

    def test_get_all_orders(self):

        res = self.client.get(
            "/api/v1/orders/allorders",
            headers={"content-type": "application/json"}
        )

        # print(res.data)

        self.assertEqual(res.status_code, 200)

    
    def test_order_by_id(self):
        '''get order by id'''

        res = self.client.get(
            "/api/v1/orders/1",
            headers={"content-type": "application/json"}
        )
        self.assertEqual(res.status_code, 200)

    def test_mark_order_as_completed(self):
        '''test for orders completed by admin'''

        res = self.client.put(
            "/api/v1/orders/completeorder/1",
            headers = {"content-type":"application/json"}
        )

        self.assertEqual(res.status_code,200)
        self.assertEqual(json.loads(res.data)['message'], "please approve the order first ")

    
    def test_declined_orders_by_admin(self):
        '''test for returning a list for orders declined by admin'''
        res = self.client.get(
            "/api/v1/orders/declinedorders",
            headers={"content-type":"application/json"}
        )
        self.assertEqual(res.status_code,200)


    def test_get_accepted_orders(self):
        '''test for getting a list of all orders accepted by admin'''
        res = self.client.get(
            "/api/v1/orders/approved",
            headers={"content-type":"application/json"}
        )
        self.assertEqual(res.status_code,200)







    def test_update_status_approved(self):
      '''test for an order whose status has been approved'''
      res = self.client.put(
            "/api/v1/orders/approve/1",
            headers={"content-type":"application/json"}
            )
            
      self.assertEqual(res.status_code,200)

      self.assertEqual(json.loads(res.data)['message'],"your order has been approved")

    def test_completed_orders(self):
        '''test for returning a list of completed orders'''

        res = self.client.get(
            "/api/v1/orders/completedorders",
            headers={"content-type":"application/json"}
        )
        self.assertEqual(res.status_code,200)

    

    def test_non_order_by_id(self):
        res = self.client.get(
            "/api/v1/orders/111",
            headers={"content-type": "application/json"}
        )
        self.assertEqual(res.status_code, 404)
        self.assertEqual(json.loads(res.data)[
                         'message'], "Order not found")


    def test_non_order_delete(self):
        res = self.client.delete(
            "api/v1/orders/1111111111",
            headers={"content-type": "application/json"}
        )
        self.assertEqual(res.status_code, 404)
        self.assertEqual(json.loads(res.data)[
                         'message'], "Order not found")

    def test_declined_orders_list(self):
        res = self.client.get(
        "/api/v1/orders/declinedorders",
        headers = {"content-type":"application/json"}
        )
        self.assertEqual(res.status_code,200)




    
    # def test_decline_order(self):
    #     '''test for an order which has been declined'''
    #     res = self.client.put(
    #         "/api/v1/orders/denied/1",
    #         headers={"content-type":"application/json"}
    #     )
    #     self.assertEqual(res.status_code,200)
