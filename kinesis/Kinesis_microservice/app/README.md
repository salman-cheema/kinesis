# Amazon Kinesis Data Streams

Kinesis Data Streams is a scalable real-time data streaming service.

## Concepts

Following are the key concepts of Kinesis Data Streams.

### Data Stream

A data stream is a logical grouping of shards. There are no bounds on the number of shards within a data stream (request a limit increase if you need more). A data stream will retain data for 24 hours, or up to 7 days when extended retention is enabled.

### Shard

A shard is an append-only log and a unit of streaming capability. A shard contains an ordered sequence of records ordered by arrival time. One shard can ingest up to 1000 data records per second, or 1MB/sec. Add more shards to increase your ingestion capability. Shards can be increased or decreased dynamically.

### Data Record

A record is the unit of data stored in an Amazon Kinesis stream. A record is composed of a sequence number, partition key, and data blob. A data blob is the data of interest your data producer adds to a stream. The maximum size of a data blob (the data payload after Base64-decoding) is 1 megabyte (MB).

### Partition Key

A partition key is typically a meaningful identifier, such as a user ID or timestamp. It is specified by your data producer while putting data into an Amazon Kinesis data stream, and useful for consumers as they can use the partition key to replay or build a history associated with the partition key. The partition key is also used to segregate and route data records to different shards of a stream.

### Data Producer

A data producer is an application that typically emits data records as they are generated to a Kinesis data stream. Data producers assign partition keys to records. Partition keys ultimately determine which shard ingests the data record for a data stream.

### Data Consumer

A data consumer is a distributed Kinesis application or AWS service retrieving data from all shards in a stream as it is generated. Most data consumers are retrieving the most recent data in a shard, enabling real-time analytics or handling of data.

### Sequence Number

A sequence number is a unique identifier for each data record. Sequence number is assigned by Amazon Kinesis Data Streams when a data producer calls PutRecord or PutRecords API to add data to an Amazon Kinesis data stream. Sequence numbers for the same partition key generally increase over time; the longer the time period between PutRecord or PutRecords requests, the larger the sequence numbers become.

### Shard Iterator

Retrieving a Data Record requires a Shard Iterator which determines how Data Records are ingested from the Kinesis Data Stream. There are five kinds of Shard Iterators.

| Shard Iterator | Explanation |
|:---:|---|
|LATEST| Starts consuming records sent after the consumer started. |
|AT_TIMESTAMP| Starts consuming records sent after a sepcific timestamp. |
|TRIM_HORIZON| Brings all the records that were sent after the retention period. |
|AT_SEQUENCE_NUMBER| Starts consuming records sent at (and after) the specified sequence number. |
|AFTER_SEQUENCE_NUMBER| Starts consuming records sent after the specified sequence number. |


## Reference

[Amazon Kinesis Data Streams - Documentation](http://docs.aws.amazon.com/kinesis/latest/dev/introduction.html)
