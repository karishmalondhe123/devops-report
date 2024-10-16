pipeline {
    agent any
    stages {
        stage('Install Venv') {
            steps {
                script {
                    // Install python3-venv
                    sh 'sudo apt-get update && sudo apt-get install -y python3-venv'
                }
            }
        }
        stage('Install Dependencies') {
            steps {
                script {
                    // Create a virtual environment
                    sh 'python3 -m venv venv'
                    // Install dependencies in the virtual environment
                    sh './venv/bin/pip install boto3'
                }
            }
        }
        stage('Generate Report') {
            steps {
                script {
                    // Run the script within the virtual environment
                    sh './venv/bin/python hello-world.py'
                }
            }
        }
        stage('Send Email') {
            steps {
                mail to: 'londhe.karishma61@example.com',
                     subject: "Weekly EC2 Report",
                     body: "Please find the attached weekly report."
                     // attachments: 'weekly_report.csv',
                     // mimeType: 'text/csv'
            }
        }
    }
    triggers {
        cron('0 8 * * 1')  // Every Monday at 8 AM
    }
    parameters {
        booleanParam(name: 'MANUAL_BUILD', defaultValue: false, description: 'Trigger the build manually')
    }
}
