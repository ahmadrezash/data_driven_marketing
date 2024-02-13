import requests
import json

headers = {
    "X-Client-Info": '{"version":"8.36.1","name":"web.vendor","deviceId":"gse63re2rhj"}',
    "sec-ch-ua": '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    "X-Creation-Tags": '{"app":"web","client":"vendor","os":"linux","device":"desktop","uri":"/orders?tab=COMPLECTED"}',
    "sec-ch-ua-mobile": "?0",
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxMSIsImp0aSI6ImIyMTVlMWNiYzI4OTkyZWQ3NjBmZWNiZjIyMjdiYjI3NjYxYTZjNDMzMTg1ZTc0MzdjNTMwMmQ0NDA2OWMyOTk5ZTA5NDU5ZTFjZmFkZDA0IiwiaWF0IjoxNzA2OTU4ODUxLjgxMzAxMiwibmJmIjoxNzA2OTU4ODUxLjgxMzAxNywiZXhwIjoxNzM4NTgxMjUxLjc5MTk3Niwic3ViIjoiMTE5NTc5MzMiLCJzY29wZXMiOltdLCJ1c2VyX2lkIjoxMTk1NzkzM30.WZ5_g6dPkwyZiJdh5xOwn3CEbQSbFDrV9AqTPpFxcaOcjfZtnVy-J3F8uidBXHGZrjX5wA6p0souCpXlL-5vZ8xRqTm4i6WmcyCvBMhgcwKqCgfsXBKI3h8Ys8WnVU03gamaT1iRn4-TsQ1juhq5NNkI3kfj2eiOuqFlMQHuRqjfoZiC4mJst87Mg8rbg-7KFxhD_sQ5l4K37mNQM8cS7o5H4o-0EAB7-qOOdpTVptTTR4PnnkepvuOOhShUtrJk3-2M-c0F1c1e1i6jnTqmYwPyvo8pNlReCx0GYB8Yb8vI0ZA_3jiX49cPezwnNrgAMy2i4uSM2fKKV8Tzw-u7z9sZenvQv_VtX_LNdCAVHRRgHtSWTUb40Q9FI6Ojb7hfrXwWyu150eLDONLVYLZRRaqJYn64n_9bRcCn7vfUBiriL4R9r9sQyhI1BR6kMBgdPr-fcbQ3koIjEqRMmFvezffxcOshBk2GBu4uFwBRjS6xanMn3Fdd92VNjT0RN_cu5Now0QLEAaeakVegFSZnh4QGn7ebFmQY7OVfd2DO2ak9f13P4PIdPwJYE1S5aAZNFMZJetO49uERRvLJmlmsIfcdneV-oGpTKjiTPXA9SGL78Xd6Fv8UQ_IVKjL6vO7vCx0Fj5p13eZ0wtERJJ9cttonR0ejci9j1itxzwZs2D4",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Referer": "https://vendor.basalam.com/",
    "sec-ch-ua-platform": '"Linux"',
}
data = []
import time

for i in range(10):
    time.sleep(1.5)
    params = {
        "tab": "COMPLECTED",
        "limit": "10",
        "offset": str(i * 10),
    }

    response = requests.get(
        "https://order-processing.basalam.com/v2/vendors/711303/orders",
        params=params,
        headers=headers,
    )
    print("offset:", params["offset"], response.status_code)
    data += response.json()["orders"]

with open("./_data.json", "w") as f:
    f.write(json.dumps(data, indent=4, ensure_ascii=False))
