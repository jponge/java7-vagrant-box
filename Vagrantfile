# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu-12.10"
  config.vm.box_url = "http://cloud-images.ubuntu.com/quantal/current/quantal-server-cloudimg-vagrant-i386-disk1.box"
  config.vm.network :forwarded_port, guest: 8080, host: 18080
  config.vm.network :forwarded_port, guest: 4848, host: 14848
end
