#!/bin/bash

MANAGER_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

cd $MANAGER_DIR
case $1 in
  docker:run)
    ${MANAGER_DIR}/misc/bin/run.sh
    ;;
  docker:down)
    ${MANAGER_DIR}/misc/bin/down.sh
    ;;
  bert)
    ${MANAGER_DIR}/misc/bin/python-container.sh bert
    ;;
  *)
    echo "Error: The command does not exist!!"
    exit 1
    ;;
esac
