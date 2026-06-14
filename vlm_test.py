import base64
import requests

IMAGE_PATH = "sample_chart.png"

with open(IMAGE_PATH, "rb") as f:
    image = base64.b64encode(f.read()).decode("utf-8")

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "moondream",
        "prompt": "Describe this chart and summarize the key information it presents.",
        "images": [image],
        "stream": False,
    },
)

print(response.json()["response"])