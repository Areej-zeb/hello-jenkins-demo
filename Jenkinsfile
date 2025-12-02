// Areej Zeb
//22i-1561
//Did lab task


pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Areej-zeb/hello-jenkins-demo.git'
            }
        }

        stage('Build & Test') {
            steps {
                // If Python is installed on the Jenkins machine:
                bat 'python -m pip install --upgrade pip'
                bat 'pip install -r requirements-dev.txt'
                // bat 'pytest'      // if you have tests
            }
        }

        // 🔐 Run SAST analysis with SonarQube
        stage('SonarQube SAST') {
            steps {
                script {
                    // Use the SonarQube server config called 'local-sonarqube'
                    withSonarQubeEnv('local-sonarqube') {
                        def scannerHome = tool 'sonar-scanner-4'
                        // This will read sonar-project.properties in the repo
                        bat "\"${scannerHome}\\bin\\sonar-scanner.bat\""
                    }
                }
            }
        }

        // 🔐 Enforce SonarQube Quality Gate
        stage('Quality Gate') {
    steps {
        timeout(time: 2, unit: 'MINUTES') {
            script {
                def qg = waitForQualityGate abortPipeline: true
                echo "Quality Gate status: ${qg.status}"
            }
        }
    }
}


        stage('Deploy') {
            when {
                branch 'main'
            }
            steps {
                echo "Deploying application (lab step)..."
            }
        }
    }

    post {
        always {
            echo "Pipeline finished."
        }
    }
}
