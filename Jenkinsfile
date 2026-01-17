pipeline {
    agent any

    environment {
        AWS_DEFAULT_REGION = 'ap-south-1'
    }

    stages {

        stage('Checkout Code') {
            steps {
                git credentialsId: 'github-creds',
                    url: 'https://github.com/shamashaik19/ai-cost-guard.git',
                    branch: 'master'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t aws-cost-guard:latest .'
            }
        }

        stage('Run AWS Cost Guard') {
            steps {
                withCredentials([
                    [$class: 'AmazonWebServicesCredentialsBinding',
                     credentialsId: 'aws-creds']
                ]) {
                    sh '''
                    docker rm -f aws-cost-guard || true
                    docker run -d \
                      -p 8000:8000 \
                      -e AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID \
                      -e AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY \
                      -e AWS_DEFAULT_REGION=$AWS_DEFAULT_REGION \
                      --name aws-cost-guard \
                      aws-cost-guard:latest
                    '''
                }
            }
        }
    }

    post {
        success {
            echo '✅ AWS Cost Guard deployed successfully!'
        }
        failure {
            echo '❌ Deployment failed. Check logs.'
        }
    }
}
