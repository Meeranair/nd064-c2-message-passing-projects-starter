import time
from concurrent import futures

import grpc

import location_pb2
import location_pb2_grpc


class LocationServicer(location_pb2_grpc.LocationServiceServicer):
    def Create(self, request, context):

        request_value = {
            "name": request.name,
            "brand_name": request.brand_name,
            "id": int(request.id),
            "weight": request.weight,
        }
        print(request_value)

        return location_pb2.ItemMessage(**request_value)


# Initialize gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
location_pb2_grpc.add_ItemServiceServicer_to_server(LocationServicer(), server)


print("Server starting on port 5005...")
server.add_insecure_port("[::]:5005")
server.start()
# Keep thread alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
