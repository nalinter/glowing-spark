echo $1
echo $2
if [ -d "prpackage_installer" ]; then
	rm -r prpackage_installer
fi
git clone git@github.com:nalinter/prpackage_installer.git
cd prpackage_installer
python3 deploy_uninstall_pkg.py $1 $2
python3 deploy_install_pkg.py $1 $2
