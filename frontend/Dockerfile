# Stage 1: Build the React app
FROM node:20 AS build

# Set the environment variables we want to access
ARG VITE_BACKEND_URL

# Set the working directory inside the container
WORKDIR /code

# Copy the package.json and package-lock.json (if it exists) into the container
COPY package*.json ./

# Install the dependencies
RUN npm install

# Copy the rest of the application code into the container
COPY . .

# Build the React app for production
RUN npm run build

# Stage 2: Serve the built app using a lightweight web server
FROM nginx:alpine

# Copy the build output to the NGINX html directory
COPY --from=build /code/dist /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# Start NGINX
CMD ["nginx", "-g", "daemon off;"]
