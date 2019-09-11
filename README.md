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

