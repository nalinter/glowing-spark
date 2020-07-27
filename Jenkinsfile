pipeline{
	agent any
	environment{
		pr_number = "4536"
	}
	stages{
		stage('github notification'){
			steps{
				withCredentials([string(credentialsId: 'auth-token-ram', variable: 'token')]) {
    sh 'curl -i -H "Authorization: token ${token}" -X POST "https://api.github.com/repos/ps-dev-ibm-cloud/Mango/issues/${GITHUB_PR_NUMBER}/comments" --data '{"body" : " SugarLint : *SUCCESS* \n UnitTest : *SUCCESS* \n PackageCreation($package_name) : *SUCCESS* \n Pre-SBX Deployment,SmokeTests($pre_sbx_report) : *SUCCESS* \n SBX Deployment,SmokeTests($sbx_report) : *SUCCESS* \n URL : ${env.BUILD_URL} "}''
		}
			}
		}
	}
}
