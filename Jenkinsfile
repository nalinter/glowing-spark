@NonCPS
def commitinformation(currentbuild){
	def logset = currentbuild.changeSets
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
