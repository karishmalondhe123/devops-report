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
                script {
                    // Send email using AWS SES SMTP
                    def mailServer = 'email-smtp.us-west-2.amazonaws.com' // Change to your AWS SES SMTP endpoint
                    def smtpPort = '465' // Use 465 for SSL
                    def smtpUser = 'AKIA3RYC6AKYIMJNFOV6'
                    def smtpPass = 'BLUDSZ+LaCRR1Z/bOchOmMZKpV/HUUVYbcnxbCH8nP6N'

                    def emailBody = "Please find the attached weekly report."

                    sh """
                    echo "${emailBody}" | mailx -s "Weekly EC2 Report" -S smtp="${mailServer}:${smtpPort}" -S smtp-auth=login -S smtp-auth-user="${smtpUser}" -S smtp-auth-password="${smtpPass}" -S ssl-verify=ignore londhe.karishma61@example.com
                    """
                }
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
