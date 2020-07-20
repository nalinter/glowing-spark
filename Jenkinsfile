pipeline{
  agent any
environment{
           pr_number = "2456"   
	    //   github_url = "https://github.com/ps-dev-ibm-cloud/Mango/pull"
	     //  smoke_test_report = "http://ddywdcdevin01.sl.bluecloud.ibm.com:8080/job/AtlasCI-Pipeline/PRE-SBX_Report/"
	      // unit_test_status="SUCCESS"
	   // package_name = "module_" + "${GITHUB_PR_NUMBER}" + "_modules_1.zip"  
          // envi_url = "http://soc.rtp.raleigh.ibm.com/atlas"  
           sbx_report = "http://ddywdcdevin01.sl.bluecloud.ibm.com:8080/job/AtlasCI-Pipeline/SBX_Report/"
    }
  stages{
    stage('Regression-Suite SBX'){
        when { not {  environment name:'SKIP_SBXTEST', value: 'true' }}
        agent{
                node{
                label 'atlasdevops'
                }
            }
            steps{
                  script{    
                     wrap([$class: 'Xvnc', takeScreenshot: false, useXauthority: true]) {
                      sh 'pwd'
                        dir('/root/Desktop/Atlastesting/sbx_smoke_test/Atlas/') {
                            sh 'mvn test -DsuiteXmlFile=SmokeTestSbx.xml'
                sh 'mv /root/Desktop/Atlastesting/sbx_smoke_test/Atlas/reports/*.html /root/Desktop/Atlastesting/test_results/sbx_smoke/$pr_number.html'
                            }
                    }
                }
                publishHTML([
                    allowMissing: false, 
                    alwaysLinkToLastBuild: false, 
                    escapeUnderscores: false, 
                    includes: "*.html",
                    keepAll: false, 
                    reportDir: '/root/Desktop/Atlastesting/test_results/sbx_smoke/', 
                    reportFiles: '*.html', 
                    reportName: 'SBX_Report', 
                    reportTitles: ''])
            }
            post{
                success{
                slackSend channel: 'atlas-sbx-deployment-approval', color: '#059e70',message: "GitHub-PR: *$pr_number* \n Package Deployment to SBX : *${currentBuild.currentResult}* \n Smoke Test(Report:$sbx_report) : *SUCCESS*", teamDomain: 'ibm-crmplatforms',tokenCredentialId: '5315744d-e8dc-4d99-8dd2-0f2c7d07e451'
                }
                failure{
                slackSend channel: 'atlas-sbx-deployment-approval', color: '#d33834',message: "GitHub-PR: *$pr_number* \n Package Deployment to SBX : *${currentBuild.currentResult}* \n Smoke Test(Report:$sbx_report) : *FAILURE*", teamDomain: 'ibm-crmplatforms',tokenCredentialId: '5315744d-e8dc-4d99-8dd2-0f2c7d07e451'
                }
            }
    }
  }
}
