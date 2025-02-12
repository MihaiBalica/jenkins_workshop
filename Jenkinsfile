pipeline {
    // Use a specific node by label (e.g., 'python') if you've assigned one to your agent.
    // Otherwise, "agent any" will use any available node.
    agent { label 'python' }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out the project...'
            }
        }
        stage('Install Dependencies') {
            steps {
                echo 'Installing Python dependencies...'
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                echo 'Running tests...'
                sh 'pytest --junitxml=results.xml'
            }
            post {
                always {
                    // Publish the test results in Jenkins.
                    junit 'results.xml'
                }
            }
        }
    }
    post {
        always {
            // Clean up workspace after every build.
            cleanWs()
        }
    }
}