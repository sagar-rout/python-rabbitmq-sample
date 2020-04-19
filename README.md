# Python Rabbitmq Sample

- Connect with rabbitmq server
- Create connection
- Publish message to rabbitmq exchange
- Consume message from rabbitmq queue


## Libs
- Pika https://github.com/pika/pika
- Rabbitmq https://github.com/rabbitmq

## Start rabbitmq server
I like docker. :)

Get rabbitmq docker - https://hub.docker.com/_/rabbitmq (Choose rabbitmq version you need), I am downloading latest rabbitmq version. 

```bash
docker pull rabbitmq
docker run -d --hostname docker-rabbit --name some-rabbit -p 4369:4369 -p 5671:5671 -p 5672:5672 -p 15672:15672 rabbitmq
docker exec some-rabbit rabbitmq-plugins enable rabbitmq_management
```
Default username/password : guest/guest

### Setup rabbitmq
1. Go to management console : http://localhost:15672/ use guest/guest as username/password
2. Go to exchange section : http://localhost:15672/#/exchanges  and you can see some default exchange with different types.
3. Click on default exchange "amq.topic"
4. Add binding from this section, pass queue name as "sagar" and routingKey as "sagar".

Yes, there is no queue "sagar" yet but our code will create it.