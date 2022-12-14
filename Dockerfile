FROM python:3.10-alpine3.15 as develop-stage
WORKDIR /usr/src/app
COPY package*.json ./
CMD ["export","FLASK_APP=main"]
CMD ["export","FLASK_ENV=development"]
CMD ["export","PORT=80"]

FROM develop-stage as build-stage
CMD ["flask", "run"]

FROM nginx:1.15.7-alpine as production-stage
COPY default.conf /etc/nginx/conf.d/
COPY --from=build-stage /usr/src/app /usr/share/nginx/html/
# To Heroku you can't expose a port

RUN ["ls","/usr/share/nginx/html/"]

CMD sed -i -e 's/$PORT/'"$PORT"'/g' /etc/nginx/conf.d/default.conf && nginx -g 'daemon off;'
