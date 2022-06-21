### Docker

**Dockerfile**
- python alpine is used due to it works with sh file based on all config of the Dockerfile

<br />

**Docker Compose**

- backend service run a 'wait.sh' file to sync the db with the api. It waits until mysql is ready to then run backend server to be able to connect to db

<br />
---
<br />

### Steps

**INIT Run**
1. Initial run
```console
docker-compose --env-file docker.env up
```

2. Inspect backend service to run migrations to the DB
```console
docker ps
docker exec -it [container] /bin/sh
```

From here the backend service will be able to execute endpoints
All the migrations to the DB are gonna be consistency based on DB ***volume***

<br />
<br />

**POST Run**
```console
docker-compose --env-file docker.env up
```
