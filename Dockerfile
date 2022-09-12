FROM python:3.10-alpine3.15
EXPOSE 5000
ADD . /app
CMD ["export","FLASK_APP=main"]
CMD ["export","FLASK_ENV=development"]
CMD ["flask", "run"]
