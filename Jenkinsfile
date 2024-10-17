pipeline {
    agent any
    stages {
        stage('Run Hello World Script') {
            steps {
                script {
                    // Run the hello-world.py script directly
                    sh 'python3 hello-world.py'
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
