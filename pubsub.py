from google.cloud import pubsub_v1


def publish_data(client: pubsub_v1.PublisherClient, topic_name: str, topic_project_id: str, data, **attrs):
    """Publishes multiple messages to a Pub/Sub topic."""

    msg_payload = data.encode()
    project_id = topic_project_id

    publisher = client
    topic_path = f"projects/{topic_project_id}/topics/{topic_name}"

    future = publisher.publish(topic_path, msg_payload, **attrs)

    print(future.result())
    print(f"Published messages to {topic_path}.")
