pipeline {
    agent {
        docker {
            image 'python:3.12'
        }
    }
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/VikaAvd/jenkins-test-repo.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'pytest tests/'
            }
        }
    }
}


