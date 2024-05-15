FROM python:3.11.0
RUN mkdir /fastapi_app
WORKDIR /fastapi_app
COPY requiremenets.txt .
RUN pip install -r requiremenets.txt
COPY . .
RUN python -c "import sqlalchemy; engine = sqlalchemy.create_engine('postgres://postgresuser:8DHPikWhY2IgL5bEVwdXsZ2xS43hnZyY@dpg-cp2bgma1hbls739e6h3g-a.singapore-postgres.render.com/task4_yrwg'); engine.connect()" || true
CMD gunicorn main:app --workers 2 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8001