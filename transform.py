import json
import pandas as pd
from datetime import datetime
import jdatetime

with open("_data.json") as f:
    data = json.load(f)
    orders = data
    order_data = []
    all_order_items = []
    date_convert = (
        lambda date: datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
        .date()
        .strftime("%Y-%m-%d")
    )
    jdate_convert = lambda date: jdatetime.datetime.fromgregorian(
        year=int(date.split("-")[0]),
        month=int(date.split("-")[1]),
        day=int(date.split("-")[2]),
    ).strftime("%Y-%m")
    for order in orders:
        data_temp = {
            "id": order["id"],
            "due_date": order["due_date"],
            "paid_at": order["paid_at"],
            "order_at": date_convert(order["paid_at"]),
            "order_at_j": jdate_convert(date_convert(order["paid_at"])),
            "order_value": order["order_value"],
            "delayed": order["delayed"],
            "customer_id": order["customer_data"]["user"]["id"],
            "customer_name": order["customer_data"]["recipient"]["name"],
            "customer_phone": order["customer_data"]["recipient"]["mobile"],
            "customer_city_id": order["customer_data"]["city"]["id"],
            "customer_city": order["customer_data"]["city"]["title"],
            "customer_state_id": order["customer_data"]["city"]["parent"]["id"],
            "customer_state": order["customer_data"]["city"]["parent"]["title"],
            "shipping_method_id": order["shipping_method"]["method"]["id"],
            "shipping_method_title": order["shipping_method"]["method"]["title"],
            "order_status_id": order["status"]["id"],
            "order_status": order["status"]["title"],
            "order_quantity": len(order["items"]),
        }
        order_data.append(data_temp)

        for order_item in order["items"]:
            order_items = {
                "order_id": order["id"],
                "product_id": order_item["id"],
                "quantity": order_item["quantity"],
                "weight": order_item["weight"],
                "product_id": order_item["product"]["id"],
                "product_name": order_item["product"]["name"],
                "product_category_id": order_item["product"]["category_id"],
            }
            all_order_items.append(order_items)

    df = pd.DataFrame(order_data)
    df.to_csv("orders.csv", index=False)
    df = pd.DataFrame(all_order_items)
    df.to_csv("order_items.csv", index=False)
