from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    """
    Podstawowy widok sprawdzający poprawność konfiguracji środowiska.
    Ten widok zostanie użyty w Assignment 0 do weryfikacji setup'u.
    """
    context = {
        'title': 'Django Workshop - Environment Check',
        'message': 'Gratulacje! Twoje środowisko Django jest poprawnie skonfigurowane.',
        'status': 'SUCCESS',
        'next_steps': [
            'Przejdź do Assignment 1',
            'Utwórz swoją pierwszą aplikację Django',
            'Rozpocznij naukę modeli i widoków'
        ]
    }
    
    return render(request, 'home.html', context)


def health_check(request):
    """
    Endpoint sprawdzający stan aplikacji - używany przez autograding
    """
    return HttpResponse("OK", status=200)