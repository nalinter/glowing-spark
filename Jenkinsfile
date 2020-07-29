pipeline{
	agent any
	stages{
		stage('package_test'){
			steps{
				script{
					def ans = env.GITHUB_PR_TITLE
				if(ans=~/(CRMATLAS|ATLASINTRN)(-| )[0-9]+/){
                        		def match = ans.findAll(~/(CRMATLAS|ATLASINTRN)(-| )[0-9]+/)
					echo "${match[0]}"
					match[0] = match[0].replaceFirst(' ','-')
                        package_name = match[0] + "_" + "${GITHUB_PR_NUMBER}" + "_" + "${BUILD_NUMBER}"
                        echo "Package Name: ${package_name}"
					}
				}
			}
		}
	}
}
