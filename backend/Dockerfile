FROM python:3.11-slim

WORKDIR /app

# Се презема готовата 'uv' бинарна датотека од официјалниот имиџ на Astral
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Се копира pyproject.toml (и uv.lock доколку постои)
COPY pyproject.toml uv.lock* ./

# Се инсталираат сите депенденси дефинирани во pyproject.toml директно во контејнерот
RUN uv pip install --system -r pyproject.toml

# Се копира останатиот дел од кодот на апликацијата
COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]