pipeline{
	agent any
	stages{
		stage('package_test'){
			steps{
				sh 'python3 pkg_install.py presbx 2559'
			}
		}
	}
}
