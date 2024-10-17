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
                to: 'londhekarishma6994@gmail.com'
            )
        }
    }
}
