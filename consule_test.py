import consul
import json

if __name__ == '__main__':
    c = consul.Consul()
    res, value = c.kv.get("config/v1/test")
    print(value["Value"])
    json_data = json.loads(value["Value"])
    print(json_data)
    with open("tst.json", "w") as output:
        json.dump(json_data, output)
