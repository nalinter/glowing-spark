@NonCPS
def commitinformation(currentbuild){
	def logset = build.changeSets
	echo ${logset}
}



pipeline{
  agent any
  stages{
    stage("sample"){
      steps{
        commitinformation(currentBuild)
      }
    }
  }
}
