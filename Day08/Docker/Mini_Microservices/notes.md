# Mini Microservices Lab

## Objective
Build a simple microservices application using Docker Compose.

## Components
- API: Flask + psycopg2
- Database: PostgreSQL
- Network: Docker Bridge Network (`micro-net`)
- Volume: `db-data` for persistent database storage

## What I Learned
- Use Docker Compose to run multiple services.
- Connect containers through a custom Docker network.
- Access PostgreSQL from another container using the service name (`db`).
- Store database data with Docker Volumes.
- Initialize the database and query data through the API.

## Workflow
1. Build and start the services with Docker Compose.
2. Create the `users` table and insert sample data.
3. Send requests to `/users`.
4. Flask connects to PostgreSQL and returns the query result.

## Result
- API and PostgreSQL communicate successfully.
- Data persists with Docker Volume.
- Services communicate through the Docker network without using IP addresses.

## Commands
```bash
docker-compose up -d

docker exec -it <db-container> psql -U postgres -d users

curl localhost:5000/users
```

## Troubleshooting
- Check container status:
  ```bash
  docker ps
  ```

- View logs:
  ```bash
  docker logs <container>
  ```

- Inspect network:
  ```bash
  docker network inspect micro-net
  ```

- Check volumes:
  ```bash
  docker volume ls
  ```