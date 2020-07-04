node {
   def commit_id
   stage('Preparation') {
     checkout scm
     sh "git rev-parse --short HEAD > .git/commit-id"
     commit_id = readFile('.git/commit-id').trim()
   }
   stage('test') {
       sh 'pip install -r requirements.txt'
       sh 'py.test'
   }                                   
   stage('docker build/push') {            
     docker.withRegistry('https://hub.docker.com', 'dockerhub_creds') {
       def app = docker.build("silbabai0110/python-docker-app:${commit_id}", '.').push()
     }                                     
   }                                       
}                                          
