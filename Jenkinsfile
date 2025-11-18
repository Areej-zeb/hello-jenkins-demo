pipeline {
    agent any

    environment {
        VERSION = '1.0.0'
    }

    tools {
        // This name MUST match the Maven installation name in:
        // Dashboard → Manage Jenkins → Tools → Maven installations
        maven 'MyMaven'
    }

    stages {
        stage('Build') {
            steps {
                echo "Building version: ${env.VERSION}"
                // On Linux/macOS agents:
                sh 'mvn -version'
                // On Windows agents you would use:
                // bat 'mvn -version'
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
