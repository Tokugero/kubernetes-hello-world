FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN touch /tmp/healthy && echo "healthy" >> /tmp/healthy && cat /tmp/healthy

ENV FLASK_ENV=development
ENV FLASK_APP=myapp.py

COPY myapp.py .

CMD [ "python3", "myapp.py" ]

