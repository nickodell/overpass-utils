#!/usr/bin/env python3
import requests
import re
from dateutil.parser import isoparse
from datetime import datetime, tzinfo, timezone

def get_local_replica_id():
    with open("/opt/osm-3s/db/replicate_id", "rt") as f:
        return f.read().strip()

def format_replica_id(id_):
    id_ = f"{int(id_):09d}"
    component1 = id_[0:3]
    component2 = id_[3:6]
    component3 = id_[6:9]
    components = "/".join([component1, component2, component3])
    url = f"https://planet.openstreetmap.org/replication/minute/{components}.state.txt"
    return url

current_replica_id = get_local_replica_id()
url = format_replica_id(current_replica_id)
resp = requests.get(url)
state = resp.content.decode('utf8')
timestamp = re.search("timestamp=(.*)", state).groups(1)[0].replace('\\', '')
timestamp = isoparse(timestamp)
now = datetime.now(timezone.utc)
#print(datetime.utcnow().tzinfo)
lag = now - timestamp
print(f"Replica is {int(lag.total_seconds()/60)} minutes behind")

