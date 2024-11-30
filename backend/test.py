import requests
import json
from datetime import date

url = "http://127.0.0.1:5000/insertorder"
payload = {
    "data": json.dumps({
        'customer_name': 'avhishek',
        'total': 800,
        'date_time': date.today().isoformat(),  # Convert to ISO format string
        'order_details': [
            {'product_id': 5, 'quantity': 2, 'total_price': 50}
        ]
    })
}

response = requests.post(url, data=payload)
print(response.json())
