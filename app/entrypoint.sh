#!/bin/bash
gunicorn app.wsgi -b 0.0.0.0:8000