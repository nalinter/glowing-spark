def slackNotification(String buildResult,String channelName,String message) {
    if ( buildResult == "SUCCESS" ) {
        slackSend channel: "${channelName}", color: '#059e70', message: "${message}", teamDomain: 'ibm-crmplatforms', tokenCredentialId: '5315744d-e8dc-4d99-8dd2-0f2c7d07e451'
        setGitHubPullRequestStatus state: 'SUCCESS', context: 'AtlasCI-Pipeline', message: "Refer Jenkins build #${env.BUILD_NUMBER} "   
    }
    else if( buildResult == "FAILURE" ) { 
        slackSend channel: "${channelName}", color: '#D33834', message: "${message}", teamDomain: 'ibm-crmplatforms', tokenCredentialId: '5315744d-e8dc-4d99-8dd2-0f2c7d07e451'
        setGitHubPullRequestStatus state: 'FAILURE', context: 'AtlasCI-Pipline', message: "Refer Jenkins build #${env.BUILD_NUMBER} "
    }
    else { 
        slackSend channel: "${channelName}", color: '#A9A9A9', message: "*BUILD ABORTED* \n URL : ${env.BUILD_URL}", teamDomain: 'ibm-crmplatforms', tokenCredentialId: '5315744d-e8dc-4d99-8dd2-0f2c7d07e451'
    }
}
pipeline{
	agent any
		evnironment{
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
			stage("Package Deployment to DEV"){
				when { not {  environment name:'SKIP_DEV', value: 'true' }}
				environment{
					//environment_name = "atlasdev01"
				}
				steps{
                    	//sh "sh ${WORKSPACE}/sugarcrm/custom/devops/shellscript/package_deployment.sh $environment_name ${latestpackage[0]}"
            			}
            	
			}
		}
}
