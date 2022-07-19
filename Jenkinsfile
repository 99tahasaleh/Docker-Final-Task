pipeline{

	agent any

	environment {
		DOCKERHUB_CREDENTIALS=credentials('docker')
	}

	stages {


		stage('Build') {

			steps {
				sh 'sudo docker build -t salehtaha/docker-final-task:latest .'
			}
		}
        stage('Login') {

			steps {
				sh ' sudo echo $DOCKERHUB_CREDENTIALS_PSW | sudo docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
			}
		}
		stage('Push') {

			steps {
				sh 'sudo docker push salehtaha/docker-final-task:latest'
			}
		}
	}

	post {
		always {
			sh 'sudo docker logout'
		}
	}

}
