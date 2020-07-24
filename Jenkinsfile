pipeline{
  agent any
  stages{
    stage('parallel'){
	steps{
		githubPRAddLabels errorHandler: statusOnPublisherError('FAILURE'), labelProperty: labels('AtlasCI'), statusVerifier: allowRunOnStatus('SUCCESS')
	}
    }
  }
}
