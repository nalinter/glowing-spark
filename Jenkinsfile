pipeline{
  agent any
  stages{
    stage('parallel'){
	parallel{
		stage('parallel-1'){
			steps{
				echo "parallel-1"
			}
		}
		stage('parallel-2){
		      steps{
			      echo "parallel-2"
		      }
		      }
	    }
    }
  }
}
