pipeline {
  agent { docker { image 'python:3.7.2' } }
  stages {
    stage('build') {
      steps {
        dir("C:\\dev\\flask_jenkins_test")
        bat "echo %cd%"
        bat 'pip install -r requirements.txt'
      }
    }
    stage('test') {
      steps {
        bat 'python little_web_app/tests.py'
      }   
    }
  }
}