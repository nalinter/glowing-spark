pipeline{
  agent any
  stages{
    stage("sample"){
      steps{
        echo "sample-stage"
      }
      post{
        always{
          echo "post stage"
        }
      }
    }
    stage("sample-2"){
      steps{
        echo "sample2"
      }
    }
  }
}
