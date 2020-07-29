pipeline{
	agent any
	stages{
		stage('package_test'){
			steps{
		githubPRAddLabels errorHandler: statusOnPublisherError('FAILURE'), labelProperty: labels('devops'), statusVerifier: allowRunOnStatus('SUCCESS')
			}
		}
	}
}
