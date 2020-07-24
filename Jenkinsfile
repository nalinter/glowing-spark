pipeline{
  agent any
  stages{
    stage('parallel'){
	steps{
		script{
			def ans = env.GITHUB_PR_TITLE
			if(ans =~ /CRMATLAS(-| )[0-9]+/)
			{
				echo "Description contains JIRA number"
				def match_pattern = ans.findAll()
				echo "${match_pattern}"
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
