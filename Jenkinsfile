pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
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
                echo 'Deploying....'
            }
        }
    }

    post {
        always {
            echo 'The build has completed.'
        }
    }
}
