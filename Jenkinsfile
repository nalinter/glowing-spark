pipeline{
	agent any
		stages{
			stage("Merge & Label Check"){
				steps{
					script{
				
						def foundFiles = sh(script: "find /var/www/html/prpackages/ -name module_CRMATLAS-8845'\'*", returnStdout: true).split()
						echo "${foundFiles}"
						def filenames = foundFiles.findAll(~/(CRMATLAS-)([0-9]+_)([0-9]+_)[0-9]+/)
						echo "${filenames}"
					}
				}
			}
		}
	
}
