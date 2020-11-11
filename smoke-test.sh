#!/usr/bin/env bash

export url=$1
sleep 45
export status_code=$(curl -LI $url -o /dev/null -w '%{http_code}\n' -s)

if [[ $status_code != "200" ]]; then
  exit 1;
fi
exit 0;