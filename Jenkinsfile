pipeline{
	agent any
		stages{
			stage("Merge & Label Check"){
				steps{
					script{
						/*if(env.GITHUB_PR_LABELS.contains('nal-label')&&env.GITHUB_PR_LABELS.contains('bug')&&env.GITHUB_PR_STATE=="CLOSED"){
							echo "${env.GITHUB_R_STATE}"
							echo "${env.GITHUB_PR_LABELS}"
							echo "closed"
						}
						else{
							echo "error"
						}*/
						def files = findFiles(glob: '/var/www/html/prpackages/CRMATLAS-8557_2608_*.zip')
						echo "${files}"
					}
				}
			}
		}
	
}
