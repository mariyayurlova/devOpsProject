pipeline {
    agent any

    options {
        buildDiscarder(logRotator(daysToKeepStr: '5', numToKeepStr: '20'))
        disableConcurrentBuilds()
        timestamps()
    }

    environment {
        DB_USER = credentials('user')
        DB_PASS = credentials('password')
    }

    stages {
        stage('Pull code') {
            steps {
                git 'git@github.com:mariyayurlova/devOpsProject.git'
            }
        }
        stage('Run backend') {
            steps {
                script {
                    sh 'python rest_app.py'
                }
            }
        }
        stage('Run frontend') {
            steps {
                script {
                    sh 'python web_app.py'
                }
            }
        }
        stage('Run backend tests') {
            steps {
                script {
                    sh 'python backend_testing.py'
                }
            }
        }
        stage('Run frontend tests') {
            steps {
                script {
                    sh 'python frontend_testing.py'
                }
            }
        }
        stage('Run combined tests') {
            steps {
                script {
                    sh 'python combined_testing.py'
                }
            }
        }
        stage('Clean environment') {
            steps {
                script {
                    sh 'python clean_environment.py'
                }
            }
        }
    }
    post {
        failure {
            mail to: 'mariya.yurlova@gmail.com',
                 subject: "Pipeline failed on ${env.BUILD_TAG}",
                 body: "The Jenkins pipeline failed. Please check the logs for more details."
        }
    }
}