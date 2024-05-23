import requests

# Token de acceso de MapQuest
MAPQUEST_API_KEY = 'fqFIEpLq2o4ochmdsoSAiN8CwYiadd2h'

def get_route_info(origin, destination):
    url = 'http://www.mapquestapi.com/directions/v2/route'
    params = {
        'key': MAPQUEST_API_KEY,
        'from': origin,
        'to': destination,
        'unit': 'k',  # unidad de medida en kilómetros
        'fuelEfficiency': 10  # valor de ejemplo para la eficiencia de combustible (en L/100 km)
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error al solicitar datos de la API de MapQuest.")
        return None

def print_route_info(data):
    if data:
        route = data['route']
        distance_km = route['distance']
        duration_sec = route['time']
        fuel_liters = route.get('fuelUsed', 0) * 3.78541  # Convertir galones a litros si está disponible

        # Si no se proporciona el consumo de combustible, calcularlo manualmente
        if fuel_liters == 0:
            # Usar una eficiencia de combustible estimada (L/100 km)
            fuel_efficiency_l_per_100km = 10  # Ajustar según el vehículo
            fuel_liters = (distance_km / 100) * fuel_efficiency_l_per_100km

        # Convertir duración a horas, minutos y segundos
        hours, remainder = divmod(duration_sec, 3600)
        minutes, seconds = divmod(remainder, 60)

        # Narrativa del viaje
        narrative = "\n".join([maneuver['narrative'] for maneuver in route['legs'][0]['maneuvers']])

        print(f"Distancia: {distance_km:.2f} km")
        print(f"Duración: {int(hours)}h {int(minutes)}m {int(seconds)}s")
        print(f"Combustible requerido: {fuel_liters:.2f} litros")
        print("Narrativa del viaje:")
        print(narrative)

def main():
    while True:
        print("\nIngrese 'q' para salir del programa.")
        origin = input("Ciudad de Origen: ")
        if origin.lower() == 'q':
            break
        destination = input("Ciudad de Destino: ")
        if destination.lower() == 'q':
            break

        data = get_route_info(origin, destination)
        print_route_info(data)

if __name__ == "__main__":
    main()
