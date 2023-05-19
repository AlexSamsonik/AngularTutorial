FROM node:20

WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install
RUN npm install -g @angular/cli

COPY . .

RUN npm run build --prod

CMD ["ng", "serve", "--host", "0.0.0.0", "--port", "4200"]
