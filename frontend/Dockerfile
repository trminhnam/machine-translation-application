FROM node:16.15.1-slim AS frontend
WORKDIR /app
COPY . .
RUN ls -a
RUN npm install
RUN npm run build
RUN npm install pm2 --location=global
EXPOSE ${PORT}
ENV TRANSLATE_HOST=http://127.0.0.1:8334
ENV TRANSLATE_PATH=/translation_api
CMD ["pm2-runtime", "build/index.js"]
