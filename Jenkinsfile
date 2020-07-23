pipeline{
  agent any
  environment{
	  package_name = "soc_"
	}
  stages{
    stage('parallel'){
	steps{
	   script{
		    withCredentials([string(credentialsId: 'auth-token-ram', variable: 'token')]) {
		review = sh(returnStdout: true, script: 'curl  -s -H "Authorization: token ${token}" -X  GET "https://api.github.com/repos/ps-dev-ibm-cloud/Mango/pulls/2557"').trim()
	}
	def json = new groovy.json.JsonSlurperClassic().parseText(review)
	echo "${json.title}"
        def title = json.title
         def name = title.subString(1,14)
         echo "${json.name}"
        
	     }
	}
    }
  }
}
