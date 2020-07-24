pipeline{
  agent any
  stages{
    stage('parallel'){
	steps{
		echo "hello"
	}
	    post{
		    success{
			    		githubPRAddLabels errorHandler: statusOnPublisherError('FAILURE'), labelProperty: labels('AtlasCI'), statusVerifier: allowRunOnStatus('SUCCESS')

		    }
	    }
    }
  }
}
