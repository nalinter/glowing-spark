pipeline{
  agent any
  stages{
    stage('parallel'){
	steps{
		script{
			def m = "1234 abc" =~ /^(\d+)/
			def ans = env.GITHUB_PR_LABELS.contains("deploytosbx")
			echo "${ans}"
		}
	}
    }
  }
}
