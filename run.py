import pika
import json

# Run all docker commands from README.md file

URL = 'amqp://guest:guest@localhost'
params = pika.URLParameters(URL)
params.socket_timeout = 5


connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='sagar')


# Publish message

personal_information = {
    "name": "Sagar",
    "profession": "Software-developer",
    "hobbies": ["Unknown"]
}


channel.basic_publish(exchange='amq.topic', routing_key='sagar', body=json.dumps(personal_information))

# Consume message


def callback(ch, method, properties, body):
    print(" [x] Received " + str(body))


# set up subscription on the queue
channel.basic_consume('sagar',  callback, auto_ack=True)

# start consuming (blocks)
channel.start_consuming()

connection.close()
