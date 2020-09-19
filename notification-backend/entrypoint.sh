#!/usr/bin/env bash
# Start the server

python3 seeds.py
uvicorn src.app.main:app --host 0.0.0.0 --port 8000 --env-file .env
