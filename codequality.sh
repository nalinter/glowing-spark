export PATH=/usr/local/bin:/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/home/devin/.local/bin:/home/devin/bin
export NODE_PATH=/usr/local/bin/node

echo "ghprbPullId=${GITHUB_PR_NUMBER}"

# Get the SC_PR_UT_Tester workspace
echo "Get the SC_PR_UT_Tester workspace"
workspace=$WORKSPACE
pr_tester_workspace=$WORKSPACE  # when running sugarlint that's Git source management specified

echo "copying mango rules to respective folder"
#cp -r /var/lib/jenkins/workspace/pipeline-testing-CI/customer/tools/vendor $pr_tester_workspace/customer/tools/
sudo cp -r /var/lib/jenkins/workspace/CodeQuality-SugarLint/customer/tools/vendor $pr_tester_workspace/customer/tools/

# Get the commit hashes
echo "Getting the commit hashes"
cd $pr_tester_workspace/sugarcrm;
curr_dir=`pwd`
echo "curr_dir = $curr_dir"
PR_HASH=`git log -n 1 --pretty=format:%H`
echo "PR_HASH=$PR_HASH"
BASE_HASH=`git show $PR_HASH^1 |awk '{print $2}' |head -1`
echo "BASE_HASH=$BASE_HASH"
FEATURE_HASH=`git show $PR_HASH^2 |awk '{print $2}' |head -1`
echo "FEATURE_HASH=$FEATURE_HASH"

#echo "ghprbPullId=$ghprbPullId"  # 09/20/2016


# Run composer install in the sugarcrm dir
#echo "Installing composer in sugracrm directory"
#cd $pr_tester_workspace/sugarcrm; 
#rm -rf composer.json composer.lock
#cp /var/lib/jenkins/workspace/AtlasCI-Pipeline/composer.json /var/lib/jenkins/workspace/AtlasCI-Pipeline/sugarcrm
#composer update

curr_dir=`pwd`
echo "curr_dir = $curr_dir"

# Run "vendor/bin/sugar-lint pull-request commit1 commit2
#cd $pr_tester_workspace/sugarcrm; php /home/devin/sugar-lint/bin/sugar-lint range $BASE_HASH $FEATURE_HASH 
echo "base hash = $BASE_HASH"
echo "feature hash = $FEATURE_HASH"
echo "Starting CodeQuality-Sugarlint"
echo "cd $pr_tester_workspace; /home/devin/sugar-lint/bin/sugar-lint -vvv range $BASE_HASH $FEATURE_HASH -c $pr_tester_workspace/customer/tools/vendor/sugar-lint-rules/mango-rules.php
"
cd $pr_tester_workspace; /home/devin/sugar-lint/bin/sugar-lint -vvv range $BASE_HASH $FEATURE_HASH -c ./customer/tools/vendor/sugar-lint-rules/mango-rules.php
#cd $pr_tester_workspace; /home/devin/sugar-lint/bin/sugar-lint -c ./customer/tools/vendor/sugarcrm/sugar-lint-rules/mango-rules.php
