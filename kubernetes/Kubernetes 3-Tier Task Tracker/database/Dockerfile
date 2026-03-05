FROM mongo:latest

# Advanced: Add a script that runs only on the first startup
# Any .sh or .js files put in this folder are executed automatically
COPY ./init-db.js /docker-entrypoint-initdb.d/

# Set environment variables for security (Best Practice)
ENV MONGO_INITDB_DATABASE=task_db

EXPOSE 27017
