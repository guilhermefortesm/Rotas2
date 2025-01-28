from flask import Flask, request, jsonify
import googlemaps
import qrcode
from PIL import Image
import random
import string
import math
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
from dotenv import load_dotenv
import os
from geopy.geocoders import Nominatim

app = Flask(__name__)

# Carrega a chave da API do Google Maps
load_dotenv()
API_KEY = os.getenv('GOOGLE_MAPS_API_KEY')

if not API_KEY:
    raise ValueError("Chave da API do Google Maps não encontrada. Verifique o arquivo .env.")

# Funções auxiliares (calcular_distancia, resolver_tsp, etc.) permanecem as mesmas
# (Copie as funções do seu código original aqui)

@app.route('/criar-rota', methods=['POST'])
def criar_rota():
    data = request.json
    enderecos = data.get('enderecos')
    ponto_inicio = data.get('ponto_inicio')

    # Lógica para criar a rota (adaptar do código original)
    # ...

    # Gerar o link da rota no Google Maps
    route_url = 'https://www.google.com/maps/dir/...'

    # Gerar o QR Code
    qr = qrcode.QRCode()
    qr.add_data(route_url)
    qr.make()

    # Salvar o QR Code como imagem
    nome_imagem = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8)) + '.png'
    qr.make_image().save(nome_imagem)

    return jsonify({'qr_code_url': nome_imagem, 'route_url': route_url})

if __name__ == '__main__':
    app.run(debug=True)