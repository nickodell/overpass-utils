#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
. vars.sh

if pgrep -u overpass dispatcher; then
    echo "Dispatcher is already running!"
    exit 1
fi

rm -f /dev/shm/osm3s_v0.7.55_osm_base
rm -f /opt/osm-3s/db/osm3s_v0.7.55_osm_base

$EXEC_DIR/bin/dispatcher --osm-base --db-dir=$DB_DIR
