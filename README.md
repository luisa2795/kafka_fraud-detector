# kafka_fraud-detector
Implementation of a streaming fraud detection system with Kafka after a tutorial by Florimond Manca

This repository contains the code that was created following this tutorial: https://florimond.dev/en/posts/2018/09/building-a-streaming-fraud-detection-system-with-kafka-and-python/

The components of the fraud detection pipeline are:

- A local Kafka cluster that acts as a centralised streaming platform.
- A transaction generator which produces transactions to the cluster.
- A fraud detector which processes transactions, detects potentially fraudulous ones and produces the results in two separate topics.

To run it follow the steps described in the original git repository here: https://github.com/florimondmanca/kafka-fraud-detector
