# jenkins
personal project to set a dind jenkins server and run some observability

### build jenkins with command

```
docker run --name jenkins-blueocean --restart=on-failure --detach \             
  --network jenkins --env DOCKER_HOST=tcp://docker:2376 \
  --env DOCKER_CERT_PATH=/certs/client --env DOCKER_TLS_VERIFY=1 \
  --publish 8080:8080 --publish 50000:50000 \
  --volume jenkins-data:/var/jenkins_home \
  --volume jenkins-docker-certs:/certs/client:ro \
  jenkins:v1
````

to run locally docker agents, use this guy to mediate between docker host and jenkins container.

```
docker run -d --restart=always -p 127.0.0.1:2376:2375 --network jenkins -v /var/run/docker.sock:/var/run/docker.sock alpine/socat tcp-listen:2375,fork,reuseaddr unix-connect:/var/run/docker.sock
```

after running the detached container, do a 
```
docker inspect <id_of_container> | grep IPAddress
````

get the address and the port 2375 that we just exposed from our alpine container and use it configure the docker cloud

more explanation: https://stackoverflow.com/questions/47709208/how-to-find-docker-host-uri-to-be-used-in-jenkins-docker-plugin

for agent docker image, we can use jenkins/agent:latest-jdk17 just for testing purposes

max instances to 2, to not overload our resources for the moment