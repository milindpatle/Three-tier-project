# Frontend Dockerfile
FROM node:18-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
# Pass backend URL at build time
ARG BACKEND_URL
RUN REACT_APP_API_URL=$BACKEND_URL npm run build

FROM nginx:alpine
# Copy custom nginx config
COPY nginx.conf /etc/nginx/nginx.conf
# Copy built files
COPY --from=builder /app/build /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]