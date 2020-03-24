FROM alpine:latest

ENV CFLAGS "-I /usr/local/lib/python3.8/site-packages/numpy/core/include $CFLAGS"

RUN apk add --no-cache --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing py3-scipy py3-scikit-learn py3-numpy py3-numpy-dev py3-pandas gcc musl-dev g++ git && \
    pip3 install discord.py python-dateutil pytest pytz joblib nltk

COPY . .

CMD python3 insults/train.py
