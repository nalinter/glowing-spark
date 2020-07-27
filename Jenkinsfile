pipeline{
	agent any
	environment{
		pr_number = "4536"
	}
	stages{
		stage('Regression-Suite SBX'){
            agent{
                node{
                label 'atlasdevops'
                }
            }
            steps{
                script{    
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
                    reportTitles: ''])
            }
        }
	}
}
