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
		review = sh(returnStdout: true, script: 'curl  -s -H "Authorization: token ${token}" -X  GET "https://api.github.com/repos/ps-dev-ibm-cloud/Mango/pulls/${GITHUB_PR_NUMBER}"').trim()
	}
	def json = new groovy.json.JsonSlurperClassic().parseText(review)
	echo "${json.title}"
        def title = json.title
         def name = title.substring(1,9)
		   if(name != "CRMATLAS"){
			   echo "Please ensure that ur description starts with "CRMATLAS" "
		   }
		   else{
			   def name1 = title.substring(1,14)
			   package_name = "soc_" + "${name1}" + "_" + "${GITHUB_PR_NUMBER}" + "_" + "${env.BUILD_NUMBER}"
			   echo "${env.package_name}"
		   }
        
	     }
	}
    }
  }
}
