FROM python:3.7
ADD finder.py authy.py utils.py requirements.txt /
RUN pip install -r requirements.txt
CMD [ "python", "-u", "finder.py"]
