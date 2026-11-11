FROM node:24.22.2-bookworm-slim AS frontend-build
RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates && update-ca-certificates && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM python:3.13.9-slim-bookworm AS backend
RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates && update-ca-certificates && rm -rf /var/lib/apt/lists/*
WORKDIR /app
RUN pip install --no-cache-dir uv==0.9.7
COPY api/pyproject.toml api/uv.lock ./api/
RUN cd api && uv sync --frozen --no-dev
COPY api ./api
COPY data ./data
EXPOSE 8000
CMD ["api/.venv/bin/uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]

