FROM python@sha256:f5d029fe39146b08200bcc73595795ac19b85997ad0e5001a02c7c32e8769efa

WORKDIR /app

COPY backend/requirements.txt .
RUN pip install -r requirements.txt

COPY backend backend

CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
