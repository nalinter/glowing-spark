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
  }
}
