# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|

    config.vm.define "nxos" do |node| 
        node.vm.box = "nxos/7.0.3.I7.3"

        config.vm.provider "virtualbox" do |vb|
          # Set memory
          vb.memory = "4096"
          # Disconnect serial port to avoid conflict
          vb.customize ['modifyvm', :id, '--uart1', '0x3F8', 4, '--uartmode1', 'disconnected']
          vb.customize ['modifyvm', :id, '--uart2', '0x2F8', 3, '--uartmode2', 'disconnected']
        end

        # Explicity set SSH Port to avoid conflict and for provisioning
        # node.vm.network :forwarded_port, guest: 22, host: 3122, id: 'ssh', auto_correct: true

        # Forward API Ports
        node.vm.network "forwarded_port", guest: 80, host: 8080, id: 'http'  # , auto_correct: true
        node.vm.network "forwarded_port", guest: 443, host: 8081, id: 'https'  # , auto_correct: true
        node.vm.network "forwarded_port", guest: 830, host: 8082, id: 'netconf'  # , auto_correct: true
    end

    # Set provisioner
    config.vm.provision "ansible" do |ansible|
        ansible.playbook = "site.yml"
        ansible.inventory_path = "inventory"
        ansible.raw_arguments = ["--connection=paramiko"]
    end

end
