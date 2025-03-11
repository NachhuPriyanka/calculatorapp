#base image as python
FROM python:3.9

#Workdirectory forcontainer (optional)
WORKDIR /app

#copy source code to container
COPY app.py .

#install required dependencies
RUN pip install flask

#command or arguments to run the application
CMD ["python", "app.py"]

