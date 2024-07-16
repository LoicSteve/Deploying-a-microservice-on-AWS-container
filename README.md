# functional-from-zero
live training

[![Python application test with Github Actions](https://github.com/LoicSteve/functions-from-zero/actions/workflows/main.yml/badge.svg)](https://github.com/LoicSteve/functions-from-zero/actions/workflows/main.yml)


### To call Microservice
something like this

```bash
curl -X 'POST' \
  'http://0.0.0.0:8080/wiki' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Microsoft"
}'
```

### Build container

`docker build .`
`docker image ls`

### Run container

something like this
`docker run -p 127.0.0.1:8080:8080 271e244e08b6 `

### Invoke POST request

run `invoke.sh`