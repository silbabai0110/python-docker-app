node {
   def commit_id
   stage('Preparation') {
     checkout scm
     sh "git rev-parse --short HEAD > .git/commit-id"
     commit_id = readFile('.git/commit-id').trim()
   }
   stage('test') {
     def myTestContainer = docker.image('qnib/pytest')
     myTestContainer.pull()
     myTestContainer.inside {
       sh 'py.test test_python_docker_app.py'
     }
   }                                   
   stage('docker build/push') {            
     docker.withRegistry('https://index.docker.io/v1/', 'dockerhub_creds') {
       def app = docker.build("silbabai0110/python-docker-app:${commit_id}", '.').push()
     }                                     
   }                                       
}                                          
