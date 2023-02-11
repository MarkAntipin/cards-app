FROM node:16-alpine as builder

WORKDIR /app
COPY . .
RUN npm ci
RUN npm run build

FROM nginx as production
ENV NODE_ENV production
COPY --from=builder /app/build /app
COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
