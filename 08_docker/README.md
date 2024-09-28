# Docker

Docker is an open-source platform that automates the deployment, scaling, and management of applications using containerization. Containers are lightweight, standalone, and executable software packages that include everything needed to run an application—code, runtime, system tools, libraries, and settings.

Docker enables developers to package applications with all their dependencies into a standardized unit called a container. These containers can run consistently across various environments, from development to production, ensuring that the software behaves the same regardless of where it's deployed.

First we can download an ubuntu docker image
```bash
docker pull ubuntu
```
To see the docker images
```bash
docker images
```
After creating a Dockerfile inside our app we can build a docker image by
```bash
docker build -t name .
```
To run the app
```bash
docker run name
```
To open the app in shell mode
```bash
docker run name -it name sh
```
To map the container port to our machine's port
```bash
docker run -p 5173:5173 name
```
To see the running containers
```bash
docker ps
```
To see all the containers
```bash
docker ps -a
```
To stop a running container
```bash
docker stop container_id
```
To remove all inactive containers
```bash
docker container prune
```
To remove a specific container
```bash
docker rm container_id
```
To remove an image
```bash
docker rmi image_id
```
To reflect our local code changes inside the container
```bash
docker run -p 5173:5173 -v "$(pwd):/app" -v /app/node_modules name
```

We can automate the image building steps using Docker Compose. First we can create a docker compose file using
```bash
docker init
```
This will create docker file and compose files after editing these files we can run the app by
```bash
docker compose up
```
