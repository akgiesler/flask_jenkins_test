pipeline {
  agent { dockerfile {
          filename 'Dockerfile'
          }
        }
  stages {
    stage('build') {
      steps {
        bat "echo starting..."
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