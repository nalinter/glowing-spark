pipeline{
  agent any
  stages{
    stage('parallel'){
	parallel{
		stage('parallel-1'){
			steps{
				sh 'sh codequality.sh'
			}
		}
		stage('parallel-2'){
		      steps{
			      echo "parallel-2"
		      }
		      }
	    }
    }
  }
}
