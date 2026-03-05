# --- Stage 1: Build ---
FROM node:18-alpine AS build-stage
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# --- Stage 2: Production ---
FROM nginx:stable-alpine
# Copy the build output to Nginx's html folder
COPY --from=build-stage /app/build /usr/share/nginx/html
# Copy a custom nginx config if you have one (for routing)
# COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
