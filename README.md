## Deployment
The [`docker-compose.yml`](https://raw.githubusercontent.com/jerbob/clauselocator/main/docker-compose.yml) in this project contains the minimal configuration to deploy this project, independent of source code.

To deploy this project with compose, copy this `docker-compose.yml` and bring up the containers:
```sh
$ wget clauses.jerbob.me/docker-compose.yml

$ docker-compose up -d

$ curl -X POST -s localhost:8000/api/clauses/locate -F 'clause=ipsum' -F 'context=lorem ipsum' | jq
{
  "success": true,
  "results": [
    6,
    10
  ],
  "errors": {}
}
```
By default, the web server will be listening on port `8000`. Set `CLAUSES_LISTEN_PORT` to change this:
```sh
$ export CLAUSES_LISTEN_PORT=8080
$ docker-compose up -d

$ curl -X POST -s localhost:$CLAUSES_LISTEN_PORT/api/clauses/locate -F 'clause=ipsum' -F 'context=lorem ipsum' | jq
{
  "success": true,
  "results": [
    6,
    10
  ],
  "errors": {}
}
```
