# sse [Chat Grop]
implement sse using flask sse.
- requirement
    redis

``` git clone https://github.com/xhijack/sse

``` cd sse
``` virtualenv env
``` . env/bin/activate
``` pip install requirement.txt
``` gunicorn sse:app --worker-class gevent --bind 127.0.0.1:8000

# TODO:
- Improve when there is new user the new user didn't know who has join the group.
- Test Coverage
