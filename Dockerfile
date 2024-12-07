FROM python
WORKDIR /home
COPY core/ .
COPY requirements.txt .
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "main.py"]