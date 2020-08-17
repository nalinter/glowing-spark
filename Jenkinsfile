pipeline{
	agent any
		stages{
			stage("Merge & Label Check"){
				steps{
					script{
						//def foundFiles = sh(script: "find . -name /var/www/html/prpackages/module_CRMATLAS-8845'\'*", returnStdout: true).split()
						def foundFiles = sh(script: "sudo ls -ltr /var/www/html/prpackages/'(CRMATLAS-)([0-9]+_)([0-9]+_)[0-9]+'", returnStdout: true).split()
						echo "${foundFiles}"
						//def filenames = foundFiles.findAll(~/(CRMATLAS-)([0-9]+_)([0-9]+_)[0-9]+/)
						//echo "${filenames}"
					}
				}
			}
		}
	
}
