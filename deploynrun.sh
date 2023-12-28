docker build --pull --rm -f "Dockerfile" -t bybittest:latest "."
docker container run bybittest:latest python /app/main.py