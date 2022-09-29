#!/usr/bin/env python
from datetime import datetime

import rides_pb2 as pb


request = pb.StartRequest(
    car_id = 95,
    driver_id = "Lixiang",
    passenger_ids = ["Lixiang", "Liu"],
    type = pb.POOL,
    location = pb.Location(lat=32.0, lng=120.0)
)

time = datetime.now()
request.time.FromDatetime(time)

# json
from google.protobuf.json_format import MessageToJson

data = MessageToJson(request)
print(data)

# size
print('encode size')
print('- json: ', len(data))
print('- pb: ', request.ByteSize())
print('- pb: ', len(request.SerializeToString()))