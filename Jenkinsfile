pipeline{
  agent any
  stages{
    stage('parallel'){
	steps{
		script{
			def ans = env.GITHUB_PR_TITLE
			if(ans =~ /CRMATLAS(-| )[0-9]+/)
			{
				def pattern = ~/CRMATLAS(-| )[0-9]+/
				def pattern_match = pattern.matcher(ans).matches()
				echo "${pattern_match}"
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
