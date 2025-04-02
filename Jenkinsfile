pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(
                    branches: [[name: '*/develop']],
                    extensions: [],
                    userRemoteConfigs: [[credentialsId: 'github_token', url: 'https://github.com/VikaAvd/jenkins-test-repo']]
                ) 
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install --break-system-packages -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'export PATH=$PATH:/var/jenkins_home/.local/bin && pytest tests/'
            }
        }
        stage('Deploy (CD)') {
            steps {
                withCredentials([string(credentialsId: 'github_token_string', variable: 'GITHUB_TOKEN')]) {
                    sh '''
                    echo "Configuring Git for deployment..."
                    git config --global user.email "jenkins@example.com"
                    git config --global user.name "Jenkins"
                    echo "Fetching and checking out develop branch..."
                    git fetch origin develop
                    git checkout develop
                    echo "Creating/updating main branch from develop..."
                    git checkout -B main
                    echo "Pushing main branch..."
                    git push https://${GITHUB_TOKEN}@github.com/VikaAvd/jenkins-test-repo.git main --force
                    echo "Deployment complete."
                    '''
                }
            }
        }
    }
}
