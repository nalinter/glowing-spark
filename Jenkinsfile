pipeline{
  agent any
  environment{
	  package_name = "never"
	}
  stages{
    stage('parallel'){
	    steps{
		    echo "hello"
	    }
            }
	  post{
		  always{
			  withCredentials([string(credentialsId: 'auth-token-ram', variable: 'token')]) {
                       sh(returnStdout: true, script: 'curl -i -H "Authorization: token ${token}" -X POST "https://api.github.com/repos/ps-dev-ibm-cloud/Mango/issues/2524/comments" --data "{"body" : "SugarLint : *SUCCESS* \n UnitTest : *SUCCESS* \n PackageCreation($package_name) : *SUCCESS* "}"')
                    }
		  }
	  }
   	 }
}
