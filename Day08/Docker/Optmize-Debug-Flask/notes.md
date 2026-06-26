## Docker Resource Limits & Health Check Lab

### Objective
Learn how to optimize and debug a Dockerized Flask application using resource limits and Docker Health Check.

### What I Did
- Built a simple Flask application with Docker.
- Added a `HEALTHCHECK` instruction to monitor application status.
- Limited container resources using:
  - Memory: `128MB`
  - CPU: `0.2`
- Generated continuous requests with `curl` to simulate application load.
- Monitored resource usage using `docker stats`.

### Debug
- Verified container health with:
  ```bash
  docker inspect flask-app --format='{{.State.Health.Status}}'
  ```
- Checked application logs:
  ```bash
  docker logs flask-app
  ```
- Tested the Health Check by removing the `curl` command and observing the container status.

### Result
- Successfully monitored CPU and memory usage.
- Verified Docker Health Check functionality.
- Practiced debugging unhealthy containers using `docker inspect`, `docker stats`, and `docker logs`.