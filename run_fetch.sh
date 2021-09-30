#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
. vars.sh
cd $EXEC_DIR/bin

echo "Sleeping to let dispatcher start..."
sleep 10

if ! pgrep -u overpass dispatcher; then
    echo "Dispatcher is not running - OSC updates can't be applied."
    exit 1
fi

$EXEC_DIR/bin/fetch_osc_and_apply.sh https://planet.osm.org/replication/minute --meta=no
