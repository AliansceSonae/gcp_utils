from google.cloud import pubsub_v1


def publish_data(topic_name, project_id, data, **attrs):
    """Publishes multiple messages to a Pub/Sub topic."""

    msg_payload = data.encode()
    project_id = project_id

    publisher = pubsub_v1.PublisherClient()
    topic_path = f"projects/{project_id}/topics/{topic_name}"

    future = publisher.publish(topic_path, msg_payload, **attrs)

    print(future.result())
    print(f"Published messages to {topic_path}.")
