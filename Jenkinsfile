pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo "Building Project"
            }
        }
    }
    post {
        success {
            emailext(
                subject: 'Test Email',
                body: 'Email sent from Jenkins',
                to: 'londhe.karishma61@gmail.com'
            )
        }
    }
}
