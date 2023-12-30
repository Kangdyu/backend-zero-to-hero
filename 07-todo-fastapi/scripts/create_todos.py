import requests

endpoint = "http://localhost:8000"

for i in range(1000):
    body = {"title": f"todo {i}", "content": f"this is todo {i}"}
    requests.post(f"{endpoint}/todos", json=body)
