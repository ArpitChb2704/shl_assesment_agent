#!/bin/bash

python app/services/retriever.py

uvicorn app.main:app --host 0.0.0.0 --port $PORT