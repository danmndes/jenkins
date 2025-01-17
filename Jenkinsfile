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
                sh 'echo "Building the application..."'
            }
        }
        stage ('Testing'){
            steps {
                sh 'echo "Running tests..."'
            }
        }
        stage ('Deploying'){
            steps {
                sh 'echo "Deploying application..."'
            }
        }
    }
}