# check=error=true
FROM python:3.12.8
EXPOSE 8000

WORKDIR /usr/src/app

COPY requirements ./
RUN pip install --no-cache-dir -r requirements

COPY . .

CMD [ "fastapi", "run", "main.py", "--host", "0.0.0.0", "--port", "8000", "--no-reload", "--proxy-headers"]