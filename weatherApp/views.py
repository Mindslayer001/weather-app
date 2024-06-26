from django.shortcuts import render
import requests

def postWeather(request,city):
    api = "enter your api key"
    url = f"https://api.weatherapi.com/v1/current.json?q={city}&key={api}"
    response = requests.get(url)
    data = response.json()
    
    context = {
        "location": data['location']['name'],
        "temp_c": data['current']['temp_c'],
        "condition_text": data['current']['condition']['text'],
        "icon_url": "https:" + data['current']['condition']['icon']
    }

    return render(request, 'weather_template.html', context)


def getInput(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        return postWeather(request, city)
    else:
        return render(request, 'input_form.html')
