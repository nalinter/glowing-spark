pipeline{
  agent any
  stages{
    stage('parallel'){
	steps{
		script{
			def m = "1234 abc" =~ /^(\d+)/
			echo "${env.GITHUB_PR_LABELS}"
		}
	}
    }
  }
}
