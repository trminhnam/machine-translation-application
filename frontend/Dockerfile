FROM node:16.15.1-slim AS frontend
WORKDIR /app
COPY . .
RUN npm install
RUN npm run build
RUN npm install pm2 --location=global
EXPOSE ${PORT}
CMD ["pm2-runtime", "build/index.js"]
