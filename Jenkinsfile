pipeline{
	agent any
		stages{
			stage("Merge & Label Check"){
				steps{
					script{
						if(env.GITHUB_PR_LABELS && env.GITHUB_PR_LABELS.contains('deploytosbx') && env.GITHUB_PR_LABELS.contains('deploytodev') && env.GITHUB_PR_STATE=="CLOSED"){
							def title = env.GITHUB_PR_TITLE
							def match = ans.findAll(~/(CRMATLAS)(-| )[0-9]+/)
                        				match[0] = match[0].replaceFirst(' ','-')
							def package_name = "module_" + match[0] + "_" + "${GITHUB_PR_NUMBER}" + "_"
							echo "${package_name}"
							def foundFiles = sh(script: "find /var/www/html/prpackages/ -name ${package_name}", returnStdout: true).split()
							echo "${foundFiles}"
							def filenames = foundFiles.sort()
							filenames = filenames.reverse(true)
							echo "${filenames}"
							def latestpackage = filenames[0].findAll(~/(CRMATLAS-)([0-9]+_)([0-9]+_)([0-9]+)/)
							echo "${latestpackage}"
						}
						else{
							echo "${env.GITHUB_PR_STATE}"
							echo "${env.GITHUB_PR_LABELS}"
							
						}
					}
				}
			}
		}
}
