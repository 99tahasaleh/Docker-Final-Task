# Docker Final Task - BitCoin 

Create a Python Web APP using FLASK that:  
● Presents the Current BitCoin Price (LIVE)  
● Stores the price in a Redis Database  
● Presents the Average Price for the last 10 minutes (LIVE) 

Dockerize the applications by Creating Dockerfile and docker-compose.yml file.

## Redis Database:
### Use cases:

#### Real-time data store
Redis' versatile in-memory data structures let you build data infrastructure for real-time applications requiring low latency and high-throughput.

#### Caching & session storage
Redis' speed makes it ideal for caching database queries, complex computations, API calls, and session state.

#### Streaming & messaging
The stream data type enables high-speed data ingestion, messaging, event sourcing, and notifications.

<img width="932" alt="image" src="https://user-images.githubusercontent.com/73100170/179393390-b8cb727c-8e35-48e4-966c-afaaaea00d4b.png">

## Run Locally

Clone the project

```bash
  git clone https://github.com/MohamadEdris/Docker-Final-Task.git
```

Go to the project directory

```bash
  cd Docker-Final-Task
```

Build

```bash
  docker compose up
```

Run

```bash
  http://localhost:8003/
```

Stop App Run

```bash
  docker compose down
```


## Web App Runing Example

<img width="500" alt="image" src="the web bitcoin price.png">


## Jenkins Pipeline

Used Jenkins to build and publish the application to Docker Hub.
Create a token from Docker to push the image to Docker Hub and set the token in the Jenkins credentials.

<img width="500" alt="image" src="push_dockerhub.png">

<img width="500" alt="image" src="jenkins_succeed.png">


