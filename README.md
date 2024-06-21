

Step 3 (from Article)

```bash
python -m gunicorn cloud.asgi:application -k uvicorn.workers.UvicornWorker
```

We shall deploy manually (there's other ways)

https://docs.render.com/deploy-django#manual-deployment
