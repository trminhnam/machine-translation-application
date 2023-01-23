FROM node:16.15.1-slim AS frontend

WORKDIR /app

COPY . /app/

RUN npm install
RUN npm run build && sleep 5
RUN npm install pm2 --location=global

EXPOSE ${PORT}

CMD ["pm2-runtime", "build/index.js"]
