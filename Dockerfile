FROM python:3.10

ADD step1/requirements.txt .
RUN pip install -r requirements.txt
RUN pip install gunicorn

EXPOSE 8080

COPY model/iris_hp_model.joblib model/
COPY iris_app.py .


CMD ["gunicorn", "iris_app:app", "-k", "uvicorn.workers.UvicornWorker", "-b", "0.0.0.0:8080"]




