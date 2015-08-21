# rollbar-celery-example

A small example showing how to use Rollbar to catch and report exceptions from Celery workers

## How to use

1. Install redis-server

2. Install package requirements

  ```
  pip install -r requirements.txt
  ```

3. Run the worker:

  ```
  celery -A tasks worker --loglevel=info
```

4. Run `send_job.py`:

  ```
  python send_job.py
  ```

