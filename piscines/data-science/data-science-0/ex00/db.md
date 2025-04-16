# Docker Compose
```yml
services:
  db:
    image: postgres
    restart: always
    environment:
      POSTGRES_USER: aruzafa-
      POSTGRES_DB: piscineds
      POSTGRES_PASSWORD: mysecretpassword
    ports:
      - 5432:5432
```

# Commands
To start container: `docker compose up`
To stop container: `docker compose down`
To stop container and delete volume: `docker compose down --volumes`
To enter inside docker container: `docker exec -it aruzafa--db-1 sh`
To enter inside DB: `psql -Uaruzafa- -dpiscineds -hlocalhost -W`
