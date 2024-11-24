# Используем официальный образ Python
FROM python:3.12

# Отключаем буферизацию вывода
ENV PYTHONUNBUFFERED 1

# Устанавливаем рабочую директорию
WORKDIR /usr/src/app

# Копируем файл с зависимостями
COPY reqs.txt /usr/src/app

# Устанавливаем зависимости
RUN pip install -r reqs.txt

# Копируем остальные файлы проекта
COPY . /usr/src/app

CMD ["gunicorn", "app.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "6"]
