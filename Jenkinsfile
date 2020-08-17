pipeline{
	agent any
		stages{
			stage("Merge & Label Check"){
				steps{
					script{
						sh 'cd /var/www/html/prpackages/'
						sh 'pwd'
						def foundFiles = sh(script: "find . -name module_CRMATLAS-8845'\'*", returnStdout: true).split()
						echo "${foundFiles}"
						def filenames = foundFiles.findAll(~/(CRMATLAS-)([0-9]+_)([0-9]+_)[0-9]+/)
						echo "${filenames}"
					}
				}
			}
		}
	
}
