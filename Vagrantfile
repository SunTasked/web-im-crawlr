Vagrant.require_version ">= 1.6.0"
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
    config.vm.hostname = "scraper"
	
	config.vm.provider "virtualbox"
	
	config.vm.provider "virtualbox" do |v|
	  v.memory = 8196
	  v.cpus = 4
	  v.name = "scraper"
	end

    config.vm.box = "ubuntu/trusty64"


    # Share current folder into the VM
    config.vm.synced_folder ".", "/vagrant"
    
    ## Provisionning with docker from vagrant
    config.vm.provision "shell", path: "install.sh"

end