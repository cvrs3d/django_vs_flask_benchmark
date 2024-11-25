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

CMD ["gunicorn", "main:app", "--bind", "0.0.0.0:5000", "--workers", "6"]