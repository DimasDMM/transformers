#!/bin/bash

SCRIPT_PATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
source ${SCRIPT_PATH}/environment-vars.sh

if [ -z ${no_down} ] && [ "$no_down" = true ]
then
    $SCRIPT_PATH/down.sh
fi

cd $SCRIPT_PATH/../../
docker-compose -f docker-compose.yml -p $PROJECT_USER up -d --build
cd -
