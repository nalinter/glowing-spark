pipeline{
  agent any
    environment{
      pr_number = "2490"   
      github_url = "https://github.com/ps-dev-ibm-cloud/Mango/pull"
      smoke_test_report = "http://ddywdcdevin01.sl.bluecloud.ibm.com:8080/job/pipeline-testing-CI/PRE-SBX_Report/"
      package_name = "module_" + "2490" + "_modules_1.zip"	
      url = "http://ddywdcdevin01.sl.bluecloud.ibm.com:8080/job/pipeline-testing-CI/174/input"
      envi_url = "http://soc.rtp.raleigh.ibm.com/atlas"
    }
    stages{
        stage('slack-send'){
            steps{
                slackSend channel: 'sbx-aproval', message: "PR-Number: *$pr_number* \n GitHub-PR: $github_url/$pr_number \n PR-Package-Name: *$package_name* \n  Environment: *PRE_SBX* \n URL: $envi_url \n Deployment: *SUCCESSFUL* \n SmokeTest: *SUCCESSFUL* \n Smoke-Test-Report: $smoke_test_report \n Click the below URL to go ahead and deploy package to SBX Environment: \n $url", teamDomain: 'ibm-crmplatforms', tokenCredentialId: '5315744d-e8dc-4d99-8dd2-0f2c7d07e451'
            }
        }
    }
}
