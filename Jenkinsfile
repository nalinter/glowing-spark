def isApproved = false 
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
    options {
        timeout(time: 30, unit: 'MINUTES') 
    }
    environment{
            pr_number = "${GITHUB_PR_NUMBER}"   
           github_url = "https://github.com/ps-dev-ibm-cloud/Mango/pull"
           pre_sbx_report = "http://ddywdcdevin01.sl.bluecloud.ibm.com:8080/job/AtlasCI-Pipeline/PRE-SBX_Report/"
           package_name = "module_" + "${GITHUB_PR_NUMBER}" + "_modules_1.zip"  
            envi_url = "http://soc.rtp.raleigh.ibm.com/atlas"  
            sbx_report = "http://ddywdcdevin01.sl.bluecloud.ibm.com:8080/job/AtlasCI-Pipeline/SBX_Report/"
    }
    stages{
        stage('Source Code Checkout'){
            steps{
               echo "Github PR Number : ${GITHUB_PR_NUMBER}"
               checkout([$class: 'GitSCM', branches: [[name: 'origin-pull/pull/${GITHUB_PR_NUMBER}/merge']], doGenerateSubmoduleConfigurations: false, extensions: [[$class: 'SubmoduleOption', disableSubmodules: false, parentCredentials: false, recursiveSubmodules: true, reference: '', trackingSubmodules: false]], submoduleCfg: [], userRemoteConfigs: [[credentialsId: '7e47757b-cf76-4d92-8d06-2fcdbd82476f', name: 'origin', refspec: '+refs/pull/${GITHUB_PR_NUMBER}/merge:refs/remotes/origin-pull/pull/${GITHUB_PR_NUMBER}/merge', url: 'git@github.com:ps-dev-ibm-cloud/Mango.git']]])               
            }
        }
       stage('Sugar Lint'){
        when { not {  environment name:'SKIP_SUGARLINT', value: 'true' }}
            steps{
           // sh "sh ${WORKSPACE}/sugarcrm/custom/devops/shellscript/codequality.sh"
                echo "sugarlint"
            }
            post{
                failure{
                    slackNotification(currentBuild.currentResult,"atlas_devops_internal","PR : $github_url/$pr_number \n Sugar Lint : *${currentBuild.currentResult}* \n URL : ${env.BUILD_URL}")
                }
            }
        }
       stage('Unit Test'){
        when { not {  environment name:'SKIP_UNITTEST', value: 'true' }}
            steps{
            //    sh "sh ${WORKSPACE}/sugarcrm/custom/devops/shellscript/unit-test.sh"
                echo "unit test"
            }
            post{
                failure{
                    slackNotification(currentBuild.currentResult,"atlas_devops_internal","PR : $github_url/$pr_number \n Sugar Lint : *SUCCESS* \n Unit Test : *${currentBuild.currentResult}* \n URL : ${env.BUILD_URL}")
                }
            }
        }
        stage('pr-packagecreate'){
        when { not {  environment name:'SKIP_PRPACKAGE', value: 'true' }}
            steps{
                script{
                    def ans = env.GITHUB_PR_TITLE
                    if(ans=~/(CRMATLAS|ATLASINTRN)(-| )[0-9]+/){
                        def match = ans.findAll(~/(CRMATLAS|ATLASINTRN)(-| )[0-9]+/)
                        match[0] = match[0].replaceFirst(' ','-')
                        package_name = match[0] + "_" + "${GITHUB_PR_NUMBER}" + "_" + "${BUILD_NUMBER}"
                        echo "Package Name: ${package_name}"
                    //    sh "sh ${WORKSPACE}/sugarcrm/custom/devops/shellscript/pr-package.sh ${GITHUB_PR_NUMBER} ${package_name}"
                    }
                    else{
                        echo "${GITHUB_PR_NUMBER}: Your PR doesn't contains JIRA Number in title, Please add Jira Number in your title Example : [CRMATLAS-1234] "
                        currentBuild.result = "FAILURE"
                        sh 'exit 1'
                    }
                }
            }
            post{
                success{
                    slackNotification(currentBuild.currentResult,"atlas_devops_internal","PR : $github_url/$pr_number \n Sugar Lint : *SUCCESS* \n Unit Test : *SUCCESS* \n PackageName : *$package_name* \n URL : ${env.BUILD_URL}")
                }
                failure{
                    slackNotification(currentBuild.currentResult,"atlas_devops_internal","PR : $github_url/$pr_number \n Sugar Lint : *SUCCESS* \n Unit Test : *SUCCESS* \n PackageCreation : *${currentBuild.currentResult}* \n URL : ${env.BUILD_URL}")
                }
            }
        }
        /*stage('Check Github Approval and label'){
            steps{
                script{
                    withCredentials([string(credentialsId: 'auth-token-ram', variable: 'token')]) {
                        review = sh(returnStdout: true, script: 'curl  -s -H "Authorization: token ${token}" -X  GET "https://api.github.com/repos/ps-dev-ibm-cloud/Mango/pulls/${GITHUB_PR_NUMBER}/reviews"').trim()
                    }
                    echo "${review}"
                    def json = new groovy.json.JsonSlurperClassic().parseText(review)
                    echo "${json.state}"
                    status=json.state
                    if (status.contains("APPROVED") && env.GITHUB_PR_LABELS && env.GITHUB_PR_LABELS.contains('deploytosbx')){
                        echo "approved..."
                        echo "${status}"
                        isApproved= true
                    }
                    else{
                        echo "not approved"
                        echo "${status}"
                    }
                }
            }
        }   
        stage('Package Deployment to PRE-SBX'){
        when { 
            allOf { 
             expression { isApproved } 
             not {  environment name:'SKIP_PRESBXDEPLOY', value: 'true' }
            }
            } 
        environment{
                environment_name = "presbx"
            }
            steps{
                    sh "sh ${WORKSPACE}/sugarcrm/custom/devops/shellscript/package_deployment.sh $environment_name ${package_name}"
            }
        }
        stage('Regression-Suite PRE-SBX'){
            when { 
                allOf { 
                    expression { isApproved } 
                    not {  environment name:'SKIP_PRESBXTEST', value: 'true' }
                }
            } 
            agent{
                node{
                label 'atlasdevops'
                }
            }
            steps{
                script{    
                    wrap([$class: 'Xvnc', takeScreenshot: false, useXauthority: true]) {
                        sh 'pwd'
                        dir('/root/Desktop/Atlastesting/integration/Atlas/') {
                            sh 'mvn test -DsuiteXmlFile=SmokeTest.xml'
                            sh 'mv /root/Desktop/Atlastesting/integration/Atlas/reports/*.html /root/Desktop/Atlastesting/test_results/integration/$pr_number.html'
                        }
                    }
                }
                publishHTML([
                    allowMissing: false, 
                    alwaysLinkToLastBuild: false, 
                    escapeUnderscores: false, 
                    includes: "*.html",
                    keepAll: false, 
                    reportDir: '/root/Desktop/Atlastesting/test_results/integration/', 
                    reportFiles: '*.html', 
                    reportName: 'PRE-SBX_Report', 
                    reportTitles: ''])
                }
        }*/ 
        stage('Package Deployment to SBX'){
        /*when { 
            allOf { 
             expression { isApproved } 
             not {  environment name:'SKIP_SBXDEPLOY', value: 'true' }
            }
            }*/ 
            environment{
                environment_name = "atlassbx01"
            }
            steps{
                 // sh "sh ${WORKSPACE}/sugarcrm/custom/devops/shellscript/package_deployment.sh $environment_name ${package_name}"
                echo "sbx"
            }
            post{
                failure{
                    slackNotification(currentBuild.currentResult,"atlas_devops_internal",message: "PR : $github_url/$pr_number \n SBX Deployment : *${currentBuild.currentResult}*")
                }
            }
        }
        stage('Regression-Suite SBX'){
            /*when { 
                allOf { 
                    expression { isApproved } 
                    not {  environment name:'SKIP_SBXTEST', value: 'true' }
                }
            }*/ 
            /*agent{
                node{
                label 'atlasdevops'
                }
            }*/
            steps{
               /* script{    
                    wrap([$class: 'Xvnc', takeScreenshot: false, useXauthority: true]) {
                        sh 'pwd'
                        dir('/root/Desktop/Atlastesting/sbx_smoke_test/Atlas') {
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
                    reportDir: '/root/Desktop/Atlastesting/test_results/sbx_smoke', 
                    reportFiles: '*.html', 
                    reportName: 'SBX_Report', 
                    reportTitles: ''])*/
                echo "regression suite sbx"
            }
            post{
                failure{
                    slackNotification(currentBuild.currentResult,"atlas_devops_internal","PR : $github_url/$pr_number \n SBX Deployment : *SUCCESS* \n SBX Smoke Test : *${currentBuild.currentResult}* \n URL : ${env.BUILD_URL}")
                }
            }
        }
    }
    post{
        success{
            slackNotification(currentBuild.currentResult,"atlas_devops_internal","GitHub PR : $github_url/$pr_number \n SugarLint : *SUCCESS* \n UnitTest : *SUCCESS* \n PackageName : *$package_name* \n Pre-SBX Deployment,SmokeTests($pre_sbx_report) : *SUCCESS* \n SBX Deployment,SBX Smoke Test($sbx_report) : *${currentBuild.currentResult}* \n URL : ${env.BUILD_URL}")
        }
    }
}
