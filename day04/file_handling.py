
import json

server = {
    "hostname": "web01",
    "ip": "10.0.0.10",
    "status": "healthy"
}

with open("server.json", "w") as file:
    json.dump(server, file, indent=4)

with open("server.json", "r") as file:
    server_data = json.load(file)

print(server_data)
print(server_data["hostname"])