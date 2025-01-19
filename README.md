# jenkins_workshop



## Vagrant
### Vagrant Installation
1. Download Vagrant from [Vagrant Downloads](https://www.vagrantup.com/downloads.html)

Steps to install Vagrant on Ubuntu:
```bash
wget -O - https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list
sudo apt update && sudo apt install vagrant

#install qemu-kvm just in case it is not installed
sudo apt update && sudo apt install -y qemu-kvm libvirt-daemon-system libvirt-clients
```

### Vagrant libvirt plugin
```bash
vagrant plugin install vagrant-libvirt
```

### Start the VMs
```bash
vagrant up --provider=libvirt
```
This command will:
	•	Create two VMs (jenkins-master and jenkins-slave).
	•	Install the necessary software (Java and Jenkins) using the provisioning scripts.
	•	Set up private networking for communication between the VMs.

### Check the VMs
```bash
vagrant status
```

### SSH into the VMs
```bash
vagrant ssh jenkins-master
ip addr show
```

### Access Jenkins
Open a browser and go to http://192.168.122.10:8080/ to access Jenkins on the master node.

- Unlock Jenkins using the password found in the file /var/lib/jenkins/secrets/initialAdminPassword on the master node.

- Install the suggested plugins.
- Create an admin user.
- Set the Jenkins URL to http://192.168.122.10:8080

#### Configure Jenkins
- install plugins
  - Pipeline
  - allure
  - ssh agent
  - junit

### Add the Jenkins Slave in Docker container
```shell
docker run -d \
  --name jenkins-agent \
  -e JENKINS_URL=http://<MASTER_IP>:8080 \
  -e JENKINS_SECRET=<AGENT_SECRET> \
  -e JENKINS_AGENT_NAME=agent1 \
  jenkins/inbound-agent
```



## Cleanup
```bash
vagrant destroy -f
vagrant box remove generic/ubuntu2004
```