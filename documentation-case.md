## Documentation test

Events from Kafka are available in Json and Delta format on S3. Events in Json format are fully available, while events in Delta format contain only fields that are explicitly described in the schema. To optimize query performance, it is recommended to use the Delta format when possible, as it can provide significant speed improvements over the Json format.

To check which fields are available in the schema, you can use the following operation: dl-show-fields table-name. If you need to convert an event to Delta format, make sure the data follows the guidelines provided in this link. Once the data complies with the guidelines, send an email to abc@cde.de to request the conversion. The event will be converted within 24 hours.

For instance, if you have an event called "abc" and queries associated with it are slow, consider converting it to Delta format to optimize performance. Ensure that the data meets the necessary requirements and follow the email request process as described above.

User question: I have an event "abc", right now queries that work with it are slow, is there any way how you could help us optimize our queries.

## First iteration

Task: Could you update the current documentation to include information from an expert based on chat conversation below:

## Hint

**Current documentation:**
Events from the event bus are available in Json and Delta format on S3.

Events in Json format contain all fields from the event bus and events in Delta format contain only fields that are explicitly described in the schema. In order to check which fields are available you could use operation: `dl-show-fields table-name`.

Json events are available by default for all datasets, but we are trying to deprecate them. Delta events could be created on-demand. In order to create delta fields the schemas should follow the following guidelines (link) and you should write an email to: abc@cde.de and event will be converted in 24 hours.

**Chat conversation:**
User: I have an event `abc`, right now queries that work with it are slow, is there any way how you could help us optimize our queries.
Expert: I've checked that this query is available in JSON format, there is an opportunity to convert to Delta format, and it will work significantly faster. You could ensure that the data follows the following guidelines (link), and send an email to abc@cde.de.

**Chat conversation 2:**
User: I have an event `abc`. We have started publishing a new field `cde`, but I couldn't find it in the data lake, when should it become available?
Expert: Do you use the dataset in Json or Delta format?
User: In delta, the path is: `s3://delta-events/abc`.
Expert: Got it, thank you. I've checked the schema registry, and I couldn't find the field `cde`. Once you add it, it should become available in 60 minutes.

**Chat conversation 3:**
User: My event `abc2` is available in Json, I would like to convert it to delta to speed it up, could you help me?
Expert: You could ensure that the data follows the following guidelines (link), and send an email to abc@cde.de to convert your dataset to the delta format.

## Second iteration

Task: Could you update the current documentation to include information from an expert based on chat conversation below:

**Current documentation:**
Events from the event bus are available in Json and Delta format on S3.

Events in Json format contain all fields from the event bus, while events in Delta format contain only fields explicitly described in the schema. To check which fields are available, you can use the operation: dl-show-fields table-name.

Json events are available by default for all datasets, but we are working to deprecate them due to performance issues. Delta events, on the other hand, offer significantly faster query performance and can be created on-demand. If you are experiencing slow queries with an event, such as event abc, consider converting it to Delta format. To do so, ensure that the data follows the guidelines provided (link) and send an email to abc@cde.de. The event will be converted within 24 hours.

**Chat conversation:**
User: I have an event `abc`. We have started publishing a new field `cde`, but I couldn't find it in the data lake, when should it become available?
Expert: Do you use the dataset in Json or Delta format?
User: In delta, the path is: `s3://delta-events/abc`.
Expert: Got it, thank you. I've checked the schema registry, and I couldn't find the field `cde`. Once you add it, it should become available in 60 minutes.


## Third iteration

Task: Could you update the current documentation if needed to include the new information from the chat conversation below.

**Current documentation:**
Events from the event bus are available in Json and Delta format on S3.

Events in Json format contain all fields from the event bus, while events in Delta format contain only fields explicitly described in the schema. To check which fields are available, you can use the operation: dl-show-fields table-name.

Json events are available by default for all datasets, but we are working to deprecate them due to performance issues. Delta events, on the other hand, offer significantly faster query performance and can be created on-demand. If you are experiencing slow queries with an event, such as event abc, consider converting it to Delta format. To do so, ensure that the data follows the guidelines provided (link) and send an email to abc@cde.de. The event will be converted within 24 hours.

When adding a new field to an existing Delta event, make sure to update the schema registry. Once the new field is added to the schema, it should become available in the data lake within 60 minutes. For example, if you have an event abc in Delta format and started publishing a new field cde, ensure that the field cde is added to the schema registry. After the update, the new field will be accessible in the data lake at the path s3://delta-events/abc within an hour.

**Chat conversation:**
User: My event `abc2` is available in Json, I would like to convert it to delta to speed it up, could you help me?
Expert: You could ensure that the data follows the following guidelines (link), and send an email to abc@cde.de to convert your dataset to the delta format.

## 3rd iteration (better task, to be checked withthe examples above)

Task: There is a current documentation and a chat conversation below, could you highlight, which new information do you see in the chat conversation that may improve the documentation quality and clarity? Could you estimate, how useful this information will be in the documentation. And decide based on that, whether this information, should be added to the documentation.

**Current documentation:**
Events from the event bus are available in Json and Delta format on S3.

Events in Json format contain all fields from the event bus, while events in Delta format contain only fields explicitly described in the schema. To check which fields are available, you can use the operation: dl-show-fields table-name.

Json events are available by default for all datasets, but we are working to deprecate them due to performance issues. Delta events, on the other hand, offer significantly faster query performance and can be created on-demand. If you are experiencing slow queries with an event, such as event abc, consider converting it to Delta format. To do so, ensure that the data follows the guidelines provided (link) and send an email to abc@cde.de. The event will be converted within 24 hours.

When adding a new field to an existing Delta event, make sure to update the schema registry. Once the new field is added to the schema, it should become available in the data lake within 60 minutes. For example, if you have an event abc in Delta format and started publishing a new field cde, ensure that the field cde is added to the schema registry. After the update, the new field will be accessible in the data lake at the path s3://delta-events/abc within an hour.

**Chat conversation:**
User: I have an event `abc`. We have started publishing a new field `cde`, but I couldn't find it in the data lake, when should it become available?
Expert: Do you use the dataset in Json or Delta format?
User: In json, the path is: `s3://delta-events/abc`.
Expert: Got it, thank you. I've checked the schema registry, and I couldn't find the field `cde`. Once you add it, it should become available in 60 minutes.

## Experiments

1. Redo with the new prompt
2. Redo with the new structure

## Second piece of information — old pipeline

### Chat 4
User: Hello, i have an event `bca`, I added a new field both in schema registry and we have started to send this field to the event bus, but I couldn't see it in my table in the delta format.
Expert: I'm sorry to tell, but your pipeline is still supported by the old Delta pipeline. It is deprecated, but we haven't migrated all the datasets yet, and it has a little bit different schema configuration. All the schemas of this pipeline are explicitly defined in git in the old-pipeline repository please use this link, and add your new field there please and send us an email (to abc@cde.de), we will redeploy our pipeline, and the new field will become available afterwards.

### Chat 5
User: Hello, i have an event `bca2`, it is not updated for the last 10 hours.
Expert: Do you use json or delta version?
User: Delta.
Expert: I see, your dataset is converted using the old pipeline (you could check it using this link). Sorry to say, but this pipeline contains a known issue, and sometimes it could be stuck, we have a monitoring for it, it works well for frequently written events, and it may take time for other events to have enough data to alert. We will restore this pipeline soon. As the long term fix, in the next months, we are planning to migrate all events to the new pipeline.

