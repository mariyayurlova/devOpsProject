pipeline {
    agent any

    options {
        buildDiscarder(logRotator(daysToKeepStr: '5', numToKeepStr: '20'))
        disableConcurrentBuilds()
        timestamps()
    }

    environment {
        DB_USER = credentials('db-username')
        DB_PASS = credentials('db-password')
    }

    stages {
        stage('Cleanup') {
                steps {
                    script {
                        sh 'fuser -k 5000/tcp || true'
                        sh 'fuser -k 5001/tcp || true'
                    }
                }
        }
        stage('Pull code') {
            steps {
                git branch: 'main', url: 'git@github.com:mariyayurlova/devOpsProject.git'
            }
        }
        stage('Setup Python Environment') {
            steps {
                script {
                    sh 'python3 -m venv venv'
                    sh '. venv/bin/activate && pip install -r requirements.txt'
                }
            }
        }
        stage('Run backend') {
            steps {
                script {
                    sh '. venv/bin/activate && nohup python3 rest_app.py &'
                }
            }
        }
        stage('Run frontend') {
            steps {
                script {
                    sh '. venv/bin/activate && nohup python3 web_app.py &'
                }
            }
        }
        stage('Run backend tests') {
            steps {
                script {
                    sh '. venv/bin/activate && nohup python3 backend_testing.py &'
                }
            }
        }
        stage('Run frontend tests') {
            steps {
                script {
                    sh '. venv/bin/activate && nohup python3 frontend_testing.py &'
                }
            }
        }
        stage('Run combined tests') {
            steps {
                script {
                    sh '. venv/bin/activate && nohup python3 combined_testing.py &'
                }
            }
        }
        stage('Clean environment') {
            steps {
                script {
                    sh '. venv/bin/activate && nohup python3 clean_environment.py &'
                }
            }
        }
    }
}