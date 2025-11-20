pipeline {
    agent any

    tools {
        // Ensure sonar-scanner tool is available by this name
        // (must match the name from Manage Jenkins → Tools)
        // This block might already exist in your Jenkinsfile
        // example:
        // python 'Python-3'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Areej-zeb/hello-jenkins-demo.git'
            }
        }

        // You probably already have something similar:
        stage('Build & Unit Tests') {
            steps {
                sh 'python -m pip install --upgrade pip'
                sh 'pip install -r requirements-dev.txt'
                // run your tests or existing static checks here
                // e.g. pytest, flake8, bandit, etc.
            }
        }

        // 🔐 NEW STAGE: SAST with SonarQube
        stage('SonarQube SAST') {
            steps {
                script {
                    // Use Jenkins SonarQube server config
                    withSonarQubeEnv('local-sonarqube') {
                        def scannerHome = tool 'sonar-scanner-4'
                        sh """
                          ${scannerHome}/bin/sonar-scanner \
                            -Dsonar.projectKey=hello-jenkins-demo \
                            -Dsonar.projectName=hello-jenkins-demo
                          """
                    }
                }
            }
        }

        // 🔐 NEW STAGE: Quality Gate – block deployment on bad security
        stage('Quality Gate') {
            steps {
                timeout(time: 2, unit: 'MINUTES') {
                    def qg = waitForQualityGate abortPipeline: true
                    echo "Quality Gate status: ${qg.status}"
                }
            }
        }

        // Whatever you already had for deploy, keep it after Quality Gate
        stage('Deploy') {
            when {
                branch 'main'
            }
            steps {
                // your existing deploy steps
                echo "Deploying application..."
            }
        }
    }

    post {
        always {
            echo "Pipeline run finished"
        }
    }
}
