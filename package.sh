echo "PRNumber : $1"
echo "Package Name : $2"
cd /home/devin/PackageCreation/atlasdocker/data/app/sugar/installer/packager
#sh createPackageFromPRNew.sh $ghprbPullId $ghprbPullId
echo "Running Script for creating Package"
sh createPackageFromPRNew.sh $1 $2
cd releases
ls
echo "copying package to prpackages folder"
cp /home/devin/PackageCreation/atlasdocker/data/app/sugar/installer/packager/releases/* /var/www/html/prpackages/
