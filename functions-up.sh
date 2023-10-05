#!/bin/bash
set -ex

if [ -n "$1" ]; then
  filter="--filter $1"
else
  filter=""
fi

ssh   -i vultr-openfaas-ssh-key   root@149.28.222.79   faas-cli -f functions.yaml up $filter
