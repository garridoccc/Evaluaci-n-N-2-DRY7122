import requests

API_KEY = 'TU_API_KEY_MAPQUEST'

def get_route(origin, destination):
    url = f'http://www.mapquestapi.com/directions/v2/route?key={API_KEY}&from={origin}&to={destination}'
    response = requests.get(url)
    return response.json()

def print_route_info(route):
    distance = route['route']['distance'] * 1.60934  # convert miles to kilometers
    time_seconds = route['route']['time']
    fuel_used = route['route']['fuelUsed'] * 3.78541  # convert gallons to liters

    hours, remainder = divmod(time_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    narrative = route['route']['legs'][0]['narrative']

    print(f"Distancia: {distance:.2f} km")
    print(f"Duración del viaje: {int(hours)} horas, {int(minutes)} minutos, {int(seconds)} segundos")
    print(f"Combustible requerido: {fuel_used:.2f} litros")
    print("Narrativa del viaje:")
    for maneuver in route['route']['legs'][0]['maneuvers']:
        print(maneuver['narrative'])

def main():
    while True:
        origin = input("Ciudad de Origen (o 'q' para salir): ")
        if origin.lower() == 'q':
            break
        destination = input("Ciudad de Destino: ")

        route = get_route(origin, destination)
        if route['info']['statuscode'] == 0:
            print_route_info(route)
        else:
            print("Error al obtener la ruta. Por favor, verifica las ciudades ingresadas.")

if __name__ == "__main__":
    main()
