pipeline{
  agent any
  environment{
	  package_name = "never"
	}
  stages{
    stage('parallel'){
	steps{
                script{
                    def ans = env.GITHUB_PR_TITLE
                    if(ans =~/CRMATLAS(-| )[0-9]+/){
                        def match = ans.findAll(~/CRMATLAS(-| )[0-9]+/)
                        match[0] = match[0].replaceFirst(' ','-')
                        package_name = match[0] + "_" + "${GITHUB_PR_NUMBER}" + "_" + "${BUILD_NUMBER}"
                        echo "Package Name: ${package_name}"
                        //sh "sh ${WORKSPACE}/sugarcrm/custom/devops/shellscript/pr-package.sh ${GITHUB_PR_NUMBER} ${package_name}"
                    }
                    else{
                        echo "${GITHUB_PR_NUMBER}: doesn't contain the JIRA Number in the description, add JIRA Number into the description"
                        currentBuild.result = "FAILURE"
			    sh 'exit'
                    }
                }
            }
    }
	    stage('parallel2'){
		    steps{
			    echo "${package_name}"
		    }
	    }
  }
}
