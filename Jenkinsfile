pipeline{
	agent any
	environment{
		pr_number = "4536"
	}
	stages{
		stage('github notification'){
			steps{
				echo "hello"
			}
			post{
				always{
					script{
						withCredentials([string(credentialsId: 'auth-token-ram', variable: 'token')]) {
    				sh 'curl -i -H "Authorization: token ${token}" -X POST "https://api.github.com/repos/ps-dev-ibm-cloud/Mango/issues/2524/comments" --data '{"body" : " sample message , please ignore SugarLint - *SUCCESS* \n UnitTest - *SUCCESS* \n PackageCreation(CRM) - *SUCCESS* \n Pre-SBX Deployment,SmokeTests(Report) - *SUCCESS* \n SBX Deployment,SmokeTests(report) - *SUCCESS* \n URL : ${env.BUILD_URL} "}''
				}
					}
				}
			}
		}
	}
}
