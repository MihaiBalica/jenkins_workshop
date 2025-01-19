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

### Add the Jenkins Slave
- Go to Manage Jenkins > Manage Nodes and Clouds > New Node
- Enter a name for the node (e.g., jenkins-slave)
- Select Permanent Agent
- Enter the following information:
	•	Remote root directory: /var/lib/jenkins
	•	Labels: jenkins-slave
	•	Launch method: Launch agent via SSH
	•	Host:
- Connect to the jenkins-slave VM using the following command:
```bash
vagrant ssh jenkins-slave
```
Connect the jenkins-slave VM using the following command:
```bash
vagrant ssh jenkins-slave
java -jar agent.jar -jnlpUrl http://192.168.122.10:8080 -secret <secret> -workDir "/var/lib/jenkins"
```


## Cleanup
```bash
vagrant destroy -f
vagrant box remove generic/ubuntu2004
```