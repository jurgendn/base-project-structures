# /bin/bash

# Start the first process
# With uvicorn worker:
# uvicorn fileName:application -h hostAddress -p port
# If there are any testing (pytest)
pytest tests/
uvicorn app:app -h 0.0.0.0 -p 8888