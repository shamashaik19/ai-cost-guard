pipeline {
    agent any

    environment {
        AWS_DEFAULT_REGION = "ap-south-1"
        IMAGE_NAME = "aws-cost-guard"
        CONTAINER_NAME = "aws-cost-guard"
    }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'master',
                    url: 'https://github.com/shamashaik19/ai-cost-guard.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                docker build -t $IMAGE_NAME:latest .
                '''
            }
        }

        stage('Run AWS Cost Guard') {
            steps {
                withCredentials([
                    [
                        $class: 'AmazonWebServicesCredentialsBinding',
                        credentialsId: 'aws-creds'
                    ]
                ]) {
                    sh '''
                    docker rm -f $CONTAINER_NAME || true

                    docker run -d \
                      --name $CONTAINER_NAME \
                      -p 8000:8000 \
                      -e AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID \
                      -e AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY \
                      -e AWS_DEFAULT_REGION=$AWS_DEFAULT_REGION \
                      $IMAGE_NAME:latest
                    '''
                }
            }
        }
    }

    post {
        success {
            echo "✅ AWS Cost Guard deployed successfully"
            echo "🌐 http://localhost:8000/status"
        }
        failure {
            echo "❌ Pipeline failed"
        }
    }
}
