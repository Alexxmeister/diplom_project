import configuration
import requests
import data



def post_new_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=order_body,
                         headers = data.headers)

response = post_new_order(data.order_body)
print(response.json())

number_of_order = response.json()["track"]

def get_order ():
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH,
                        params={"t": number_of_order})

response = get_order()
print("Проверка созданного заказа")
print(response.status_code)
print(response.json())