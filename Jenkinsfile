def isApproved = false 
def slackNotification(String buildResult,String channelName,String message) {
    if ( buildResult == "SUCCESS" ) {
        slackSend channel: "${channelName}", color: '#059e70', message: "${message}", teamDomain: 'ibm-crmplatforms', tokenCredentialId: '5315744d-e8dc-4d99-8dd2-0f2c7d07e451'
      //  setGitHubPullRequestStatus state: 'SUCCESS', context: 'AtlasCI-Pipeline', message: "Refer Jenkins build #${env.BUILD_NUMBER} "
        
    }
    else if( buildResult == "FAILURE" ) { 
        slackSend channel: "${channelName}", color: '#D33834', message: "${message}", teamDomain: 'ibm-crmplatforms', tokenCredentialId: '5315744d-e8dc-4d99-8dd2-0f2c7d07e451'
       // setGitHubPullRequestStatus state: 'FAILURE', context: 'AtlasCI-Pipline', message: "Refer Jenkins build #${env.BUILD_NUMBER} "
    }
    else { 
        slackSend channel: "${channelName}", color: '#A9A9A9', message: "*BUILD ABORTED* \n URL : ${env.BUILD_URL}", teamDomain: 'ibm-crmplatforms', tokenCredentialId: '5315744d-e8dc-4d99-8dd2-0f2c7d07e451'
    }
}
pipeline{
    agent any
    options {
        timeout(time: 30, unit: 'MINUTES') 
    }
    stages{
        stage('Source Code Checkout'){
            steps{
               echo "Github PR Number : ${GITHUB_PR_NUMBER}"
               slackNotification(currentBuild.currentResult,"#atlas_devops_internal","Hello Jenkins from bangalore :joy (test message)")

               //checkout([$class: 'GitSCM', branches: [[name: 'origin-pull/pull/${GITHUB_PR_NUMBER}/merge']], doGenerateSubmoduleConfigurations: false, extensions: [[$class: 'SubmoduleOption', disableSubmodules: false, parentCredentials: false, recursiveSubmodules: true, reference: '', trackingSubmodules: false]], submoduleCfg: [], userRemoteConfigs: [[credentialsId: '7e47757b-cf76-4d92-8d06-2fcdbd82476f', name: 'origin', refspec: '+refs/pull/${GITHUB_PR_NUMBER}/merge:refs/remotes/origin-pull/pull/${GITHUB_PR_NUMBER}/merge', url: 'git@github.com:ps-dev-ibm-cloud/Mango.git']]])               
            }
        }
       
        }
}
