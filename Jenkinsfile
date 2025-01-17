pipeline { 
    agent any
    stages {
        stage ('Building and Running Docker Images'){
            steps {
                // Check Docker version to verify access to Docker daemon
                sh 'docker network create jenkins'
                sh 'docker build -t prometheus-agent:v1 -f Dockerfile-Prometheus .'
                sh 'docker run -d --name prometheus-agent --network jenkins -p 9100:9100 prometheus-agent:v1'
                sh 'docker compose up -d'
            }
        }
        stage ('Building'){
            steps {
                // Example Docker command
                sh 'docker ps -a'
            }
        }
        stage ('Testing'){
            steps {
                sh 'echo "Running tests..."'
            }
        }
        stage ('Teardown'){
            steps {
                sh 'docker stop $(docker ps -a -q)'
                sh 'docker rm $(docker ps -a -q)'
                sh 'docker network rm jenkins'
                sh 'docker volume rm $(docker volume ls -q)'
                sh 'docker system prune -f'
            }
        }
    }
}