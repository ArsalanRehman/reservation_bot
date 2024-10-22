### build command

`docker build -t reservation-bot .`

### Run command

`docker run --rm  reservation-bot`

### Run command with bind mount

`docker run --rm -v /home/arslan/python_course/tenis/:/app  reservation-bot`

### Debug using this command

`docker run -it --entrypoint /bin/bash reservation-bot`
