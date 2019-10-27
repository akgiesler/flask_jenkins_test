pipeline {
  agent { dockerfile true }
  stages {
    stage('build') {
      steps {
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