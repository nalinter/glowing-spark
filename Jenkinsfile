def slackNotification(String buildResult,String message) {
    if ( buildResult == "SUCCESS" ) {
	    slackSend channel: '#atlas_devops_internal', color: '#059e70', message: "${message}", teamDomain: 'ibm-crmplatforms', tokenCredentialId: '5315744d-e8dc-4d99-8dd2-0f2c7d07e451'
       // setGitHubPullRequestStatus state: 'SUCCESS', context: 'AtlasCI-Pipeline', message: "Refer Jenkins build #${env.BUILD_NUMBER} "
       }
    }
    
pipeline{
	agent any
	stages{
		stage('package_test'){
			steps{
				slackNotification("SUCCESS","Sample testing message \n ${env.BUILD_URL}")
			}
		}
	}
}
