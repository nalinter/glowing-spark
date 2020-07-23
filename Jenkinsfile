pipeline{
  agent any
  stages{
    stage('parallel'){
	steps{
		script{
			def ans = env.GITHUB_PR_TITLE
			echo "${ans}"
			def regex = (ans=~'/CRMATLAS(-| )(\d+)/')
		}
	}
    }
  }
}
