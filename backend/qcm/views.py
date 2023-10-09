from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
import requests


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        # Remplacez 'YOUR_API_KEY' par votre clé d'accès Dummyjson
        api_key = "YOUR_API_KEY"
        url = "https://dummyjson.com/api/data?api_key={}&schema=my-schema".format(
            api_key
        )

        # Effectuez une requête GET à l'API Dummyjson pour obtenir des données factices
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                # Redirigez l'utilisateur vers la page principale ou une autre page après la connexion
                return redirect("page_principale")
            else:
                return render(
                    request, "login.html", {"error_message": "Identifiants incorrects"}
                )
        else:
            return render(
                request,
                "login.html",
                {"error_message": "Échec de la récupération des données factices"},
            )

    return render(request, "login.html")
