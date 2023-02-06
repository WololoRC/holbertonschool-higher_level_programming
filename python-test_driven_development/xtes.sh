#!/bin/bash

if [ $# -ne 1 ]; then
  echo "Se requiere un argumento: el nombre del archivo doctest.txt"
  exit 1
fi

if [ ! -f "$1" ]; then
  echo "El archivo $1 no existe o no es un archivo regular."
  exit 1
fi

doctest_file="$1"

python3 -m doctest -v "$doctest_file"
