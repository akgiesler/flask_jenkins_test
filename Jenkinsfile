pipeline {
  agent { docker { image 'python:3.7.2' } }
  environment{ PATH = 'C:\\Program Files\\Docker Toolbox;C:\\Program Files\\Python38\\Scripts\\;C:\\Program Files\\Python38\\;C:\\WINDOWS\\system32\\;C:\\Program Files\\Git\\cmd'}
  stages {
    stage('build') {
      steps {
        dir("C:\\dev\\flask_jenkins_test")
        sh "echo starting..."
        sh "echo %cd%"
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