import requests

while True:
    API_KEY = "8bb4ff781c10f7e725d2e91fff93a987"
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

    city = input("Enter a city name: ")
    request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"

    reply = requests.get(request_url)
    if reply.status_code == 200:
        data = reply.json()
        weather = data['weather'][0]['description']
        temperature = round(data['main']['temp'] - 273.15, 2)

        print("Weather:", weather)
        print("Temperature:", temperature, "°C")

    else:
        print("An error occured!")

    while True:
        answer = str(input('Would you like to check another city? (y/n): '))
        if answer in ('y', 'n'):
            break
        print("invalid input - try again!")
    if answer == 'y':
        continue
    else:
        print("Goodbye!")
        break