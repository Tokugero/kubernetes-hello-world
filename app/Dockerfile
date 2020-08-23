FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && \
	apt-get install -y \
		curl \
		openssh-server \
		net-tools \
		dnsutils \
		iproute2

ADD ./.profile.d /app/.profile.d

RUN rm /bin/sh && ln -s /bin/bash /bin/sh
	
RUN echo "healthy" >> /tmp/healthy && \
	cat /tmp/healthy

ENV FLASK_ENV=development
ENV FLASK_APP=myapp.py

COPY myapp.py .

CMD python3 myapp.py
