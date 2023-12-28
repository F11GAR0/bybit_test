## Example to withdraw for Rudolf

#### Config
Create *config.py* and place in this:
```py
BYBIT_API_KEY="Place your api key here"
BYBIT_API_SECRET="Place your api secret here"
```

#### Build docker if need
```sh
docker build --pull --rm -f "Dockerfile" -t bybittest:latest "."
```
#### Run with docker
```sh
docker container run bybittest:latest python /app/main.py
```
#### Run vanila
```sh
python main.py
```