FROM node:20-alpine

COPY . /app
WORKDIR /app

RUN yarn

RUN echo $(cat /dev/urandom | tr -dc 'a-z' | fold -w 99 | head -n 1) > /app/src/jwt.key

CMD ["yarn", "start"]
