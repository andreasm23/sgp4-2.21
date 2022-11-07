#!/bin/bash -ue

if [ $# -eq 0 ]
then
  echo "Need one input argument: NORAD Id"
  exit 3
fi

curl -s https://celestrak.org/NORAD/elements/gp.php?CATNR=$1