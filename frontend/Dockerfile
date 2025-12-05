FROM node:18-alpine as builder
WORKDIR /app
COPY package.json .
RUN npm install --production
COPY public ./public
COPY src ./src
RUN npm run build

FROM node:18-alpine
WORKDIR /app
COPY --from=builder /app/build /app/build
RUN npm install -g serve
ENV PORT=80
EXPOSE 80
CMD ["serve", "-s", "build", "-l", "80"]
