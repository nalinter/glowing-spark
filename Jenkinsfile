pipeline{
	agent any
		stages{
			stage("Merge & Label Check"){
				steps{
					if(env.GITHUB_PR_LABELS.contains('nal-label')&&env.GITHUB_PR_STATE=="CLOSED"){
						echo "closed"
					}
					else{
						echo "error"
					}
				}
			}
		}
	
}
