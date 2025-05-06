pipeline {
    agent any

    environment {
        DOCKER_HUB_USERNAME = 'eelysa'
        DOCKER_IMAGE        = 'mydjangoapp'
        DOCKER_TAG          = 'v1.0.1'
        CONTAINER_NAME      = 'django_container'
        HOST_PORT           = '8002'    // host port on EC2
        CONTAINER_PORT      = '8000'    // port inside container
        EC2_USER            = 'ec2-user'
        EC2_HOST            = '3.134.207.118'
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t $DOCKER_HUB_USERNAME/$DOCKER_IMAGE:$DOCKER_TAG ."
            }
        }

        stage('Login to Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'docker-credentials',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASSWORD'
                )]) {
                    sh "echo $DOCKER_PASSWORD | docker login -u $DOCKER_USER --password-stdin"
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                sh "docker push $DOCKER_HUB_USERNAME/$DOCKER_IMAGE:$DOCKER_TAG"
            }
        }

        stage('Deploy to EC2') {
            steps {
                withCredentials([sshUserPrivateKey(
                    credentialsId: 'ec2-ssh-key',
                    keyFileVariable: 'SSH_KEY'
                )]) {
                    sh """
                    ssh -o StrictHostKeyChecking=no -i $SSH_KEY $EC2_USER@$EC2_HOST '
                      docker pull $DOCKER_HUB_USERNAME/$DOCKER_IMAGE:$DOCKER_TAG
                      docker stop $CONTAINER_NAME || true
                      docker rm   $CONTAINER_NAME || true
                      docker run -d \
                        --name $CONTAINER_NAME \
                        -p $HOST_PORT:$CONTAINER_PORT \
                        $DOCKER_HUB_USERNAME/$DOCKER_IMAGE:$DOCKER_TAG
                    '
                    """
                }
            }
        }
    }

    post {
        success { echo '✅ Deployment successful!' }
        failure { echo '❌ Deployment failed!' }
    }
}
