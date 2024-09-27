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
To run oru app
```bash
docker run name
```
To open the app in shell mode
```bash
docker run name -it name sh
```
