#!/bin/bash
set -ex

scp   -i vultr-openfaas-ssh-key   functions.yaml    root@149.28.222.79:functions.yaml
scp   -i vultr-openfaas-ssh-key   pull-handlers.sh   root@149.28.222.79:pull-handlers.sh

ssh   -i vultr-openfaas-ssh-key   root@149.28.222.79   bash pull-handlers.sh
