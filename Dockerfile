FROM python:3-alpine

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY perm_letters.py .

#CMD [ "python", "./perm_letters.py", "-s", "rpiece" ]
ENTRYPOINT [ "/usr/src/app/perm_letters.py" ]
