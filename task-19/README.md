## Steps use the playbook for creating K8S cluster

* Use `ansible-playbook -vv ec2.yml` to create instances.
* Then, change the `remote user` to `ec2-user`.
  ```
  [defaults]
    inventory = inventory
    host_key_checking= false
    command_warnings= false
    #remote_user= ec2-user
    private_key_file= ec2.pem
    roles_path= K8SMaster :K8SSlave 
  ```
* Then, run `ansible-playbook -vv k8scluster.yml` to setup the K8S cluster on the AWS EC2 instances.
