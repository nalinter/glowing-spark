pipeline{
	agent any
		stages{
			stage("Merge & Label Check"){
				steps{
					script{
						def foundFiles = sh(script: 'ls /var/www/html/prpackages/CRMATLAS-8164', returnStdout: true).split()
						echo "${foundFiles}"
					}
				}
			}
		}
	
}
