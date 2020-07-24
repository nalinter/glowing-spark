pipeline{
  agent any
  stages{
    stage('parallel'){
	steps{
		script{
			def ans = env.GITHUB_PR_TITLE
			if(ans =~ /CRMATLAS(-| )[0-9]+/)
			{
				def res = ans.findAll(~/CRMATLAS(-| )[0-9]+/).replaceAll(( ),'-')
				package_name = res[0] + "_" + "${GITHUB_PR_NUMBER}" + "_" + "${BUILD_NUMBER}"
				echo "${package_name}"
			}
			else{
				echo "description doesn't have JIRA number Please change add JIRA number into description"
				currentBuild.result = "FAILURE"
			}
		}
	}
    }
  }
}
