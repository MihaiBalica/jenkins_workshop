Vagrant.configure("2") do |config|
  config.vm.define "jenkins-master" do |master|
    master.vm.provider :libvirt do |libvirt|
      libvirt.driver = "qemu"
      libvirt.memory = 2048
      libvirt.cpus = 2
    end
    master.vm.box = "generic/ubuntu2004"
    master.vm.hostname = "jenkins-master"
    master.vm.network "private_network", ip: "192.168.122.10"
    master.vm.provision "shell", inline: <<-SHELL
      sudo apt update && sudo apt install -y openjdk-11-jdk wget
      sudo wget -O /usr/share/keyrings/jenkins-keyring.asc https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key
      sudo sh -c 'echo "deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc]" https://pkg.jenkins.io/debian-stable binary/ | sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null'
      sudo apt update && sudo apt install -y jenkins
      sudo systemctl enable jenkins && sudo systemctl start jenkins
    SHELL
  end

  config.vm.define "jenkins-slave" do |slave|
    slave.vm.provider :libvirt do |libvirt|
      libvirt.driver = "qemu"
      libvirt.memory = 2048
      libvirt.cpus = 2
    end
    slave.vm.box = "generic/ubuntu2004"
    slave.vm.hostname = "jenkins-slave"
    slave.vm.network "private_network", ip: "192.168.122.11"
    slave.vm.provision "shell", inline: <<-SHELL
      sudo apt update && sudo apt install -y openjdk-11-jdk
    SHELL
  end
end