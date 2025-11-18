pipeline {
    agent any

    environment {
        VERSION = '1.0.0'
    }

    stages {
        stage('Build') {
            steps {
                echo "Building version: ${env.VERSION}"
            }
        }

        stage('Test') {
            when {
                expression { return true }
            }
            steps {
                echo 'Running tests only if condition is true'
            }
        }

        stage('Deploy') {
            steps {
                echo "Deploying version: ${env.VERSION}"
            }
        }
    }

    post {
        always {
            echo 'The build has completed.'
        }
    }
}
