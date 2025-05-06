pipeline {
    agent any

    environment {
        EC2_USER = 'ec2-user'
        EC2_HOST = '3.134.207.118'
        PROJECT_DIR = '/home/ec2-user/myproject' // Adjust the project directory
        REPO_URL = 'https://github.com/Eeirq/ImTrying.git'
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
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
                      cd $PROJECT_DIR
                      git pull origin main
                      source 9Lives/bin/activate  # Activate virtual env (adjust if needed)
                      pip install -r requirements.txt
                      python manage.py migrate
                      nohup python manage.py runserver 0.0.0.0:8000 &
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
