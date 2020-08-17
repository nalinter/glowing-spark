pipeline{
	agent any
		stages{
			stage("Merge & Label Check"){
				steps{
					script{
						dir('/var/www/html/prpackages/'){
						def foundFiles = sh(script: "find . -name module_CRMATLAS-8845'\'*", returnStdout: true).split()
						echo "${foundFiles}"
						}
					}
				}
			}
		}
	
}
