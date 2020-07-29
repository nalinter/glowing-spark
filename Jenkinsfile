pipeline{
	agent any
	stages{
		stage('package_test'){
			steps{
				githubPRAddLabels labelProperty: labels('hello'), statusVerifier: buildStatus('SUCCESS'), errorHandler: buildStatus('FAILURE')
			}
		}
	}
}
