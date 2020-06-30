pipeline{
  agent any
    environment{
      pr_number = "2490"   
	   	github_url = "https://github.com/ps-dev-ibm-cloud/Mango/pull"
	   	smoke_test_report = "http://ddywdcdevin01.sl.bluecloud.ibm.com:8080/job/pipeline-testing-CI/PRE-SBX_Report/"
    }
    stages{
        stage('slack-send'){
            steps{
                slackSend channel: 'sbx-aproval', color: '#A9A9A9', message: "Environment: *PRE_SBX* \n PR-NUMBER: *$pr_number* \n GitHub-PR: $github_url/$pr_number \n PR-Package-Name: *module_'$pr_number'_modules_1.zip* \n Deployment-Pre-SBX: *SUCCESSFUL* \n SmokeTest: *SUCCESSFUL* \n Smoke-Test-Report: $smoke_test_report \n Click the below URL to go ahead and deploy package to SBX Environment: \n hello", teamDomain: 'ibm-crmplatforms', tokenCredentialId: '5315744d-e8dc-4d99-8dd2-0f2c7d07e451'
            }
        }
    }
}
