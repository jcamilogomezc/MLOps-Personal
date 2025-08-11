FROM python:3.10-slim
COPY app/ /app/
COPY models/ /app/models/
COPY docker/requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt
EXPOSE 8989
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8989"]