pipeline {
    agent any
    environment {
        // Bind the GitHub token to an environment variable for secure usage
        GITHUB_TOKEN = credentials('github_token_string')
    }
    stages {
        stage('Checkout Develop') {
            steps {
                checkout scmGit(
                    branches: [[name: '*/develop']],
                    extensions: [],
                    userRemoteConfigs: [[credentialsId: 'github_token', url: 'https://github.com/VikaAvd/jenkins-test-repo']]
                ) 
            }
        }
        stage('Fetch Remote Main') {
            steps {
                script {
                    echo "Fetching remote main branch..."
                    sh 'git fetch origin main'
                }
            }
        }
        stage('Check for Remote Differences') {
            steps {
                script {
                    // Log commits on develop that are not in remote main for troubleshooting
                    echo "Commits in develop that are not in remote main (origin/main):"
                    sh 'git log origin/main..develop --oneline || true'
                    
                    // Check for differences between remote main and develop.
                    // Note: git diff --quiet returns 0 if no differences, non-zero if differences are found.
                    def diffStatus = sh(script: 'git diff --quiet origin/main develop', returnStatus: true)
                    
                    if (diffStatus != 0) {
                        echo "Differences detected: changes exist in develop that are not in origin/main."
                        env.CHANGES_DETECTED = "true"
                    } else {
                        echo "No differences detected between develop and remote main."
                        env.CHANGES_DETECTED = "false"
                    }
                }
            }
        }
        stage('Deploy (Merge Develop into Main)') {
            steps {
                script {
                    sh '''
                    echo "Configuring Git..."
                    git config --global user.email "jenkins@example.com"
                    git config --global user.name "Jenkins"
                    echo "Checking out main branch..."
                    git checkout -B main
                    echo "Merging develop into main..."
                    git merge origin/develop --no-ff -m "Merging develop into main for deployment"
                    echo "Pushing main branch..."
                    git push https://${GITHUB_TOKEN}@github.com/VikaAvd/jenkins-test-repo.git main --force
                    echo "Deployment complete."
                    '''
                }
            }
        }
        stage('Skip Deployment if No Changes') {
            when {
                expression { env.CHANGES_DETECTED == "false" }
            }
            steps {
                echo "Skipping deployment because no remote differences were found between develop and main."
            }
        }
    }
}