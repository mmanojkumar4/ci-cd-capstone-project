pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Backend Image') {
            steps {
                bat 'docker build -t flask-backend backend'
            }
        }

        stage('Run Backend Tests') {
            steps {
                bat 'docker build -t flask-backend-test --target test backend'
                bat 'docker run --rm flask-backend-test'
            }
        }

        stage('Build Frontend Image') {
            steps {
                bat 'docker build -t flask-frontend frontend'
            }
        }

        stage('Security Scan') {
            steps {
                bat '''
                docker run --rm ^
                  -v /var/run/docker.sock:/var/run/docker.sock ^
                  aquasec/trivy image flask-backend

                docker run --rm ^
                  -v /var/run/docker.sock:/var/run/docker.sock ^
                  aquasec/trivy image flask-frontend
                '''
            }
        }

        stage('Deploy to Staging') {
    steps {
        bat '''
        docker-compose -f docker-compose.staging.yml down
        docker-compose -f docker-compose.staging.yml up -d --build
        '''
    }
}

    }
}
