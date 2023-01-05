FROM python:3.10

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy requirements.txt into work dir
COPY ../requirements.txt .

# install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt --no-cache-dir

COPY ./entrypoint.sh .

RUN chmod +x ./entrypoint.sh
# copy project
COPY . .

ENTRYPOINT ["sh", "./entrypoint.sh"]