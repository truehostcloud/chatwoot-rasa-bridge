#!/bin/bash

python -m gunicorn app:app -b 0.0.0.0 --workers="$GUNICORN_WORKERS" --threads="$GUNICORN_THREADS" --timeout="$GUNICORN_TIMEOUT"
