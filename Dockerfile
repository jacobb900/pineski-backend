FROM python:3.11-slim

# Ustawiamy zmienne środowiskowe, żeby Python nie tworzył śmieci
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Instalujemy zależności systemowe
RUN apt-get update && apt-get install -y libpq-dev gcc

# Kopiujemy listę bibliotek (jeśli masz plik requirements.txt)
# Jeśli nie masz, zaraz go zrobimy
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kopiujemy resztę kodu
COPY . .

EXPOSE 8000

# Odpalamy serwer Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]