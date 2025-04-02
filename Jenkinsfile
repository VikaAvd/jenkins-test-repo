pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/VikaAvd/jenkins-test-repo.git'
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
                sh '''
                echo "Configuring Git for deployment..."
                git config --global user.email "jenkins@example.com"
                git config --global user.name "Jenkins"
                echo "Checking out release branch..."
                git checkout -B release
                echo "Merging develop into release..."
                git merge origin/develop --no-ff -m "Merging develop into release for deployment"
                echo "Pushing release branch..."
                git push origin release --force
                echo "Deployment complete."
                '''
            }
        }
    }
}
