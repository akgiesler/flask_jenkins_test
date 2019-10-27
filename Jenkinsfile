pipeline {
  dir("C:\\dev\\flask_jenkins_test"){sh "echo %cd%"}
  agent { docker { image 'python:3.7.2' } }
  stages {
    stage('build') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }
    stage('test') {
      steps {
        sh 'python little_web_app/tests.py'
      }   
    }
  }
}