pipeline{
	agent any
		stages{
			stage("Get Latest Package Uploaded to SBX"){
				steps{
					script{
						def val = "module_CRMATLAS-6759_2607_'\'*"
						def foundFiles = sh(script: "find /var/www/html/prpackages/ -name ${val}", returnStdout: true).split()
						echo "${foundFiles}"
						def filenames = foundFiles.sort()
						filenames = filenames.reverse(true)
						echo "${filenames}"
						def matchvalue = filenames[0].findAll(~/(${val})([0-9]+)/)
						echo "${matchvalue}"
					}
				}
			}
		}
	
}
