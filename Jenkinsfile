pipeline{
  agent any
  stages{
    stage('parallel'){
	steps{
		script{
			def ans = env.GITHUB_PR_TITLE
			echo "${ans}"
			if(ans =~ /CRMATLAS(-| )[0-9]+/){
				echo "yes"
			}
		}
	}
    }
  }
}
