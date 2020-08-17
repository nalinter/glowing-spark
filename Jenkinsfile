pipeline{
	agent any
		stages{
			stage("Merge & Label Check"){
				steps{
					script{
						def foundFiles = sh(script: "find . -name /var/www/html/prpackages/module_CRMATLAS-8845'\'*", returnStdout: true).split()
						echo "${foundFiles}"
						def filenames = ans.findAll(~/(CRMATLAS|ATLASINTRN)(-| )([0-9]+|_)+/)
						echo "${filenames}"
					}
				}
			}
		}
	
}
