from django.shortcuts import render
import requests
def home(request):
    if request.method == 'POST':
        city = request.POST['city']
        api_key = ""
        url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
        response = requests.get(url)
        data = response.json()
        context = {"city": city, "temperature": data['current']['temp_c'], 
        "condition":data['current']['condition']['text'], 'icon': data['current']['condition']['icon']}
        return render(request, 'main.html', context)
    return render(request, 'main.html')
