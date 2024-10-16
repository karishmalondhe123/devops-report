pipeline {
    agent any
    stages {
        stage('Install Dependencies') {
            steps {
                script {
                    // Install dependencies
                    sh 'pip install boto3'
                }
            }
        }
        stage('Generate Report') {
            steps {
                script {
                    // Run the script
                    sh 'python3 generate_report.py'
                }
            }
        }
        stage('Send Email') {
            steps {
                mail to: 'londhe.karishma61@example.com',
                     subject: "Weekly EC2 Report",
                     body: "Please find the attached weekly report.",
                     attachmentsPattern: 'weekly_report.csv',
                     mimeType: 'text/csv'
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
