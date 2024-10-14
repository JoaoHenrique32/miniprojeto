import requests

client_id = "cliente1"
image_path = "imagem.jpg"

with open(image_path, 'rb') as f:
    response = requests.post('http://localhost:5000/upload', files={'image': f}, data={'client_id': client_id})

print(response.json())
