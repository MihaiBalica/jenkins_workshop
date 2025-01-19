Vagrant.configure("2") do |config|
  config.vm.define "jenkins-master" do |master|
    master.vm.provider :libvirt do |libvirt|
      libvirt.driver = "qemu"
      libvirt.memory = 2048
      libvirt.cpus = 3
    end
    master.vm.box = "generic/ubuntu2404"
    master.vm.hostname = "jenkins-master"
    master.vm.network "private_network", ip: "192.168.122.10"
    master.vm.provision "shell", inline: <<-SHELL
      sudo apt update && sudo apt install -y docker.io
      sudo usermod -aG docker vagrant
    SHELL
    master.vm.provision "shell", inline: <<-SHELL
      docker run -d \
        --name jenkins-master \
        -u root \
        -p 8080:8080 -p 50000:50000 \
        -v jenkins_home:/var/jenkins_home \
        -v /var/run/docker.sock:/var/run/docker.sock \
        jenkins/jenkins:lts
    SHELL
  end

  config.vm.define "jenkins-slave" do |slave|
    slave.vm.provider :libvirt do |libvirt|
      libvirt.driver = "qemu"
      libvirt.memory = 2048
      libvirt.cpus = 3
    end
    slave.vm.box = "generic/ubuntu2404"
    slave.vm.hostname = "jenkins-slave"
    slave.vm.network "private_network", ip: "192.168.122.11"
    slave.vm.provision "shell", inline: <<-SHELL
      sudo apt update && sudo apt install -y docker.io
      sudo usermod -aG docker vagrant
    SHELL
  end
end