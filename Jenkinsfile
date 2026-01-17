pipeline {
    agent any

    environment {
        AWS_DEFAULT_REGION = "ap-south-1"
    }

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                docker build -t aws-cost-guard:latest .
                '''
            }
        }

        stage('Run AWS Cost Guard') {
            steps {
                sh '''
                docker rm -f aws-cost-guard || true

                docker run -d \
                  --name aws-cost-guard \
                  -p 8000:8000 \
                  -e AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID \
                  -e AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY \
                  -e AWS_DEFAULT_REGION=$AWS_DEFAULT_REGION \
                  aws-cost-guard:latest
                '''
            }
        }
    }

    post {
        success {
            echo "✅ AWS Cost Guard deployed successfully"
            echo "🌐 Access: http://localhost:8000/status"
        }
        failure {
            echo "❌ Deployment failed"
        }
    }
}
