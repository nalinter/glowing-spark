pipeline{
	agent any
	stages{
		stage('package_test'){
			steps{
				script{
				if(ans=~/(CRMATLAS|ATLASINTRN)(-| )[0-9]+/){
                        		def match = ans.findAll(~/(CRMATLAS|ATLASINTRN)(-| )[0-9]+/)
					echo "${match[0]}"
					}
				}
			}
		}
	}
}
