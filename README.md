# CeleryXFlask

## Task queue Celery with Flask 

Celery  is an asynchronous task queue used to run background tasks as a distributed architechture that will enable your application to scale.


### Installation components:

#### 1. Celery Client :

Runs with Flask application to issue background jobs


#### 2. Celery Workers : 

The processes that run in the background. These can be local (running with Flask on the same Machine) or remote.

#### 3. Message Broker :

Client communicates with Workers through "Message Queues" and Celery has various methods of implementing these queues. 
Example: RabbitMQ and Redis

##### Redis Installation :

Two ways to do this:

1. Quick setup : `run-redis.sh`
2. Follow the following steps

```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install redis-server
sudo systemctl enable redis-server.service
```

###### Configuration :

```
sudo vim /etc/redis/redis.conf
```
###### add 
```
maxmemory 256mb
maxmemory-policy allkeys-lru
```

```
sudo systemctl restart redis-server.service
```
###### Install Redis PHP Extension:
```
sudo apt-get install php-redis
```

###### test

```
redis-cli

127.0.0.1:6379> ping
PONG
127.0.0.1:6379>
```
