pipeline{
  agent any
  stages{
    stage("sample"){
      steps{
	 echo "sample"
      }
      post{
                success{
                slackSend channel: 'atlas-sbx-deployment-approval', color: '#059e70',message: "GitHub-PR: *$pr_number* \n Package Deployment to SBX : *${currentBuild.currentResult}* \n Smoke Test(Report:$sbx_report) : *Success*", teamDomain: 'ibm-crmplatforms',tokenCredentialId: '5315744d-e8dc-4d99-8dd2-0f2c7d07e451'
                }
                failure{
                slackSend channel: 'atlas-sbx-deployment-approval', color: '#d33834',message: "GitHub-PR: *$pr_number* \n Package Deployment to SBX : *${currentBuild.currentResult}* \n Smoke Test(Report:$sbx_report) : *Failure*", teamDomain: 'ibm-crmplatforms',tokenCredentialId: '5315744d-e8dc-4d99-8dd2-0f2c7d07e451'
                }
       }
    }
  }
}
