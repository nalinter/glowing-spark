pipeline{
	agent any
		environment{
			def latestpackage = "${GITHUB_PR_NUMBER}"
		}	
		stages{
			stage("Merge & Label Check"){
				steps{
					script{
						if(env.GITHUB_PR_LABELS && env.GITHUB_PR_LABELS.contains('deploytosbx') && env.GITHUB_PR_LABELS.contains('deploytodev') && env.GITHUB_PR_STATE=="CLOSED"){
							def title = "CRMATLAS-8565"
							def match = title.findAll(~/(CRMATLAS)(-| )[0-9]+/)
                        				match[0] = match[0].replaceFirst(' ','-')
							def package_name = "module_" + match[0] + "_" + "2651" + "_'\'*"
							echo "${package_name}"
							def foundFiles = sh(script: "find /var/www/html/prpackages/ -name ${package_name}", returnStdout: true).split()
							def filenames = foundFiles.sort()
							filenames = filenames.reverse(true)
							echo "Files Found : ${filenames}"
							latestpackage = filenames[0].findAll(~/(CRMATLAS-)([0-9]+_)([0-9]+_)([0-9]+)/)
							echo "Package Deployed to SBX : ${latestpackage[0]}"	
						}
					}
				}
			}
			
		}
}
