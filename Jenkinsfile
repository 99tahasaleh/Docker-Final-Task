pipeline{

	agent any

	environment {
		DOCKERHUB_CREDENTIALS=credentials('docker')
	}

	stages {


	}

	post {
		always {
			sh 'sudo docker logout'
		}
	}

}
