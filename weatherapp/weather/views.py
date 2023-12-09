from django.shortcuts import render
from decouple import config
import json
import urllib.request


def index(request):
    if request.method == 'POST':
        city = request.POST.get('city', '')
        API_KEY = config('API_KEY')
        url = 'https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=' + API_KEY

        try:
            res = urllib.request.urlopen(url).read()
            json_data = json.loads(res)

            if 'cod' in json_data and str(json_data['cod']) == '404':
                # Ciudad no encontrada
                data = {
                    'error_message': 'La ciudad no fue encontrada. Por favor, verifica el nombre de la ciudad.'}
            else:
                # Ciudad encontrada, procesar datos
                data = {
                    'country_code': str(json_data['sys']['country']),
                    'coordinate': str(json_data['coord']['lon']) + ' ' + str(json_data['coord']['lat']),
                    'temp': str(round(json_data['main']['temp'] - 273.15, 1)) + '°C',
                    'pressure': str(json_data['main']['pressure']),
                    'humidity': str(json_data['main']['humidity']),
                }
        except Exception as e:
            # Manejar otros errores de la API
            error_message = f'Error al obtener datos de la API. Detalles: {str(e)}'
            data = {'error_message': error_message}
    else:
        city = ''
        data = {}

    return render(request, 'index.html', {'city': city, 'data': data})
