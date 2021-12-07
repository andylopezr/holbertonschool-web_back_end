#!/usr/bin/env python3
""" Python module """


from pymongo import MongoClient


client = MongoClient()
db = client.logs
collection = db.nginx


def log_stats(mongo_collection) -> None:
    """
    log_stats: returns a string with nginx logs stats from mongodb
    """
    GET = mongo_collection.count_documents({"method": "GET"})
    POST = mongo_collection.count_documents({"method": "POST"})
    PUT = mongo_collection.count_documents({"method": "PUT"})
    PATCH = mongo_collection.count_documents({"method": "PATCH"})
    DELETE = mongo_collection.count_documents({"method": "DELETE"})
    STATUS = mongo_collection.count_documents({
                                                "method": "GET",
                                                "path": "/status"
                                            })
    LOGS = mongo_collection.count_documents({})
    pipeline = [
            {
                "$group": {"_id": "$ip", "total": {"$sum": 1}}
            },
            {
                "$sort": {"total": -1}
            },
            {
                "$limit": 10
            }
        ]
    IP_LIST = mongo_collection.aggregate(pipeline)

    print(f"{LOGS} logs")
    print("Methods:")
    print(f"\tmethod GET: {GET}")
    print(f"\tmethod POST: {POST}")
    print(f"\tmethod PUT: {PUT}")
    print(f"\tmethod PATCH: {PATCH}")
    print(f"\tmethod DELETE: {DELETE}")
    print(f"{STATUS} status check")
    print("IPs:")
    for ip in IP_LIST:
        print(f"\t{ip.get('_id')}: {ip.get('total')}")


if __name__ == "__main__":

    log_stats(collection)
