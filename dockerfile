FROM python

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ENV ENV=env
# Install pip requirements
WORKDIR /app
COPY requirements.txt /app
RUN pip3 install -r requirements.txt

RUN apt update && apt install -y vim
RUN apt install -y chromium
CMD ["pytest", "--headless", "--dashboard", "-v", "--pls=none", "--sjw"]
