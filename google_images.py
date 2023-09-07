import requests

# Función para buscar imágenes en Google Images
def buscar_imagenes(query, google_api_key, google_cse_id):
    base_url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'q': query,
        'key': google_api_key,
        'cx': google_cse_id,
        'searchType': 'image',
        'num': 5
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        if 'items' in data:
            return data['items']
    return []
