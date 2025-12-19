# Hackathon-Task-List-Dockerized-Inference-Environment
Containerize a model + API so it runs anywhere reproducibly
Dockerized Inference Environment
FastAPI Dockerized Inference Service

A simple FastAPI application containerized using Docker and Docker Compose, deployed locally and on AWS EC2.
This project demonstrates how to build, run, and expose an API service in a reproducible environment.
eatures

FastAPI REST API

Swagger UI (/docs)

Dockerized application

Docker Compose support

Ready for AWS EC2 deployment
Project Structure
fastapi-docker/
│
├── app/
│   ├── __init__.py
│   └── main.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
Requirements

Docker

Docker Compose

Python 3.9+ (only for local testing)

AWS EC2 (for cloud deployment)
Deploy on AWS EC2
1️⃣ Launch EC2

AMI: Ubuntu 22.04

Open ports: 22, 8000

Instance type: t2.micro

2️⃣ Install Docker on EC2
sudo apt update
sudo apt install -y docker.io docker-compose
sudo systemctl start docker
sudo usermod -aG docker ubuntu
exit

Copy project to EC2
scp -i <key>.pem -r fastapi-docker ubuntu@<EC2-PUBLIC-IP>:/home/ubuntu/

4️⃣ Run the app
cd fastapi-docker
docker compose up --build -d

Access API
http://3.94.98.226:8000/docs

Common Issues & Resolutions
no configuration file provided: not found

Cause: Running Docker Compose from wrong directory
✅ Fix:
Run command where docker-compose.yml exists

scp: No such file or directory

Cause: Wrong local path
✅ Fix:
Use full path or navigate to correct folder:


