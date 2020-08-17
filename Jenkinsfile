pipeline{
	agent any
		stages{
			stage("Merge & Label Check"){
				steps{
					script{
						def foundFiles = sh(script: 'ls', returnStdout: true).split()
						echo "${foundFiles}"
					}
				}
			}
		}
	
}
