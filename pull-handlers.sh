#!/bin/bash
set -ex

cd
cd das
git fetch
git checkout meetup
git pull origin meetup

cd
cd DAS-function
git fetch
git checkout main
git pull origin main
