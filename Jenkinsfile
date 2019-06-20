pipeline {
    agent any
    triggers {
        pollSCM '*/5 * * * *'
    }
    stages {
        stage('Checkout') {
            steps {
                git "https://github.com/khjomaa/world_of_games.git"
            }
        }
        stage("Build") {
            steps {
                sh 'docker-compose build'
            }
        }
        stage("Run") {
            steps {
                sh 'docker-compose up -d'
            }
        }
        stage("Test") {
            steps {
                sh 'docker exec wog python tests/e2e.py'
            }
        }
        stage("Finalize") {
            steps {
                withCredentials([usernamePassword(credentialsId: 'DockerHub', passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_ID')]) {
                    sh 'docker login -u $DOCKER_ID -p $DOCKER_PASSWORD'
                    sh 'docker push khjomaa/world_of_games:latest'
                }
                sh 'docker-compose down;docker rmi $(docker images -q)'
            }
        }
    }
}