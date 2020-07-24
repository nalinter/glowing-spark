pipeline{
  agent any
  stages{
    stage('parallel'){
	steps{
		githubPRAddLabels errorHandler: statusOnPublisherError('FAILURE'), labelProperty: labels('test_intern_3'), statusVerifier: allowRunOnStatus('SUCCESS')
	}
    }
  }
}
