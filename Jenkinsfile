pipeline{
  agent any
  stages{
    stage('parallel'){
	steps{
		def m = "1234 abc" =~ /^(\d+)/
		if(m.find()){
			def ans = m.group()
			echo "${ans}"
		}
	}
    }
  }
}
