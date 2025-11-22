# 🚀 Django Workshop - Assignment 0: Environment Check

Witamy w pierwszym zadaniu z serii Django Workshop! To zadanie sprawdza czy Twoje środowisko programistyczne jest poprawnie skonfigurowane i gotowe do nauki Django.

## 📋 Co sprawdza to zadanie?

Assignment 0 weryfikuje następujące elementy:

- ✅ **Django Installation** - Czy Django jest zainstalowane i działa
- ✅ **Dev Server** - Czy serwer deweloperski uruchamia się bez błędów  
- ✅ **URL Routing** - Czy podstawowy routing działa poprawnie
- ✅ **Templates** - Czy system szablonów jest skonfigurowany
- ✅ **Static Files** - Czy pliki statyczne są obsługiwane
- ✅ **Database** - Czy SQLite database działa
- ✅ **Admin Panel** - Czy panel administracyjny jest dostępny

## 🎯 Twoje zadanie

**To zadanie nie wymaga pisania kodu!** Wszystko jest już skonfigurowane. Musisz tylko:

### 1. Uruchomić serwer deweloperski

```bash
python manage.py runserver
```

### 2. Sprawdzić czy strona działa

Otwórz przeglądarkę i przejdź na:
- **http://localhost:8000** - Powinna pokazać się strona powitalną
- **http://localhost:8000/health/** - Powinno zwrócić "OK"

### 3. Sprawdzić autograding

Testy automatyczne sprawdzą czy wszystko działa:

```bash
# Uruchom wszystkie testy
DJANGO_SETTINGS_MODULE=workshop_project.settings python -m pytest tests/test_assignment_0.py -v

# Lub krótszy sposób (jeśli pytest.ini jest skonfigurowany):
python -m pytest tests/test_assignment_0.py -v
```

## ✅ Kryteria sukcesu

Zadanie jest zaliczone gdy:

1. **Wszystkie 13 testów przechodzą** ✅
2. **Strona główna wyświetla się poprawnie** na http://localhost:8000
3. **Health check endpoint** zwraca "OK" na /health/
4. **Brak błędów** w konsoli podczas uruchamiania serwera

## 🐛 Rozwiązywanie problemów

### Problem: "No module named django"
```bash
# Upewnij się że virtual environment jest aktywny
source venv/bin/activate  # Linux/Mac
# lub
venv\\Scripts\\activate     # Windows

# Zainstaluj zależności
pip install -r requirements.txt
```

### Problem: "Table doesn't exist"
```bash
# Uruchom migracje
python manage.py migrate
```

### Problem: "DJANGO_SETTINGS_MODULE is not set"
```bash
# Uruchom testy z explicit settings module
DJANGO_SETTINGS_MODULE=workshop_project.settings python -m pytest tests/test_assignment_0.py
```

### Problem: Port 8000 jest zajęty
```bash
# Użyj innego portu
python manage.py runserver 8080

# Lub zabij proces na porcie 8000
lsof -ti:8000 | xargs kill -9
```

## 🔧 Struktura projektu

```
django_workshop_template/
├── manage.py                    # Django management script
├── requirements.txt             # Python dependencies  
├── pytest.ini                  # Test configuration
├── db.sqlite3                  # SQLite database (po migracji)
│
├── workshop_project/            # Main Django project
│   ├── __init__.py
│   ├── settings.py              # Django settings
│   ├── urls.py                  # URL routing
│   ├── views.py                 # View functions
│   ├── wsgi.py                  # WSGI config
│   └── asgi.py                  # ASGI config
│
├── templates/                   # HTML templates
│   ├── base.html               # Base template
│   └── home.html               # Home page template
│
├── static/                      # Static files (CSS, JS, images)
│   └── (empty - dodasz pliki w kolejnych assignments)
│
├── tests/                       # Test files
│   ├── __init__.py
│   └── test_assignment_0.py     # Assignment 0 tests
│
└── .devcontainer/               # GitHub Codespaces config
    └── devcontainer.json        # Development environment setup
```

## 🎓 Co się nauczysz?

Po ukończeniu Assignment 0 będziesz wiedział:

- Jak uruchomić serwer deweloperski Django
- Jak działają podstawowe URL patterns
- Jak Django obsługuje templates i static files  
- Jak uruchamiać testy pytest-django
- Jak sprawdzać czy aplikacja działa poprawnie

## 🚀 Co dalej?

Po zaliczeniu Assignment 0 przechodzisz do **Assignment 1: Pierwszy Projekt i Aplikacja**, gdzie:

- Utworzysz pierwszą aplikację Django
- Dowiesz się czym różni się projekt od aplikacji
- Skonfigurujesz INSTALLED_APPS
- Napiszesz pierwszy własny widok

## 💡 Wskazówki

1. **Zawsze aktywuj virtual environment** przed pracą
2. **Sprawdź logi w konsoli** jeśli coś nie działa
3. **Użyj `python manage.py help`** aby zobaczyć dostępne komendy
4. **GitHub Codespaces** automatycznie skonfiguruje środowisko za Ciebie
5. **Autograding** automatycznie sprawdzi Twoje rozwiązanie przy każdym push

---

## 🆘 Potrzebujesz pomocy?

- **Discord/Slack**: Zadaj pytanie na kanale warsztatowym  
- **Issues**: Utwórz issue w repozytorium jeśli znajdziesz błąd
- **Instruktor**: Poproś o pomoc podczas warsztatów

---

**Powodzenia!** 🎉

> **Pamiętaj**: Assignment 0 to tylko sprawdzenie środowiska. Prawdziwa zabawa zacznie się w kolejnych zadaniach, gdzie będziesz budować prawdziwą aplikację Django krok po kroku!