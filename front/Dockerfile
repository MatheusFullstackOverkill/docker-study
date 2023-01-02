FROM node:17-alpine

WORKDIR /app

COPY package.json .

RUN npm install

COPY . .

RUN npm run build

FROM nginx:stable

COPY nginx.conf /etc/nginx/sites-enabled/default
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=0 /app/out /out
EXPOSE 80