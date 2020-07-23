import java.util.regex.Matcher;
import java.util.regex.Pattern;
pipeline{
  agent any
  stages{
    stage('parallel'){
	steps{
		script{
			def ans = env.GITHUB_PR_TITLE
			echo "${ans}"
			Pattern pat = Pattern.compile("/CRMATLAS(^| )([0-9]+)/");
			Matcher mat = pat.matcher(ans)
			if(mat.find()){
			    def exp = mat.group()
				echo "${exp}"
			}
		}
	}
    }
  }
}
