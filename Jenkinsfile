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
                git branch: 'main', url: 'git@github.com:mariyayurlova/devOpsProject.git'
            }
        }
        stage('Run backend') {
            steps {
                script {
                    sh 'nohup python rest_app.py &'
                }
            }
        }
        stage('Run frontend') {
            steps {
                script {
                    sh 'nohup python web_app.py &'
                }
            }
        }
        stage('Run backend tests') {
            steps {
                script {
                    sh 'nohup python backend_testing.py &'
                }
            }
        }
        stage('Run frontend tests') {
            steps {
                script {
                    sh 'nohup python frontend_testing.py &'
                }
            }
        }
        stage('Run combined tests') {
            steps {
                script {
                    sh 'nohup python combined_testing.py &'
                }
            }
        }
        stage('Clean environment') {
            steps {
                script {
                    sh 'nohup python clean_environment.py &'
                }
            }
        }
    }
}