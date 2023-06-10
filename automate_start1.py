import subprocess

def execute_docker_compose():
    # Change the directory to the location of your docker-compose.yml file
    compose_directory = '/home/bibin/msc_pro/docker_comp/'
    # Command to execute docker-compose
    command = ['docker-compose', '-f', 'docker-compose1.yml', 'up', '-d']
    # Run the command as a subprocess
    subprocess.run(command, cwd=compose_directory, check=True)

def execute_virtual_interfaces():
    # Specify the path to your bash script
    script_path = '/home/bibin/msc_pro/docker_comp/interfaces1.sh'
    # Execute the bash script
    subprocess.run(['bash', script_path], check=True)

def execute_get_namespace_red():
    command = f"docker inspect ubuntu_red | grep SandboxKey"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    output = result.stdout.strip()
    start_index = output.find('"/') + 2
    end_index = output.find('"', start_index)
    # Extract the namespace path
    namespace_path = output[start_index:end_index]
    namespace_path = '/'+ namespace_path
    print(namespace_path)
    veth_commd = ['sudo', 'ip', 'link', 'set', 'veth-r-cont', 'netns', namespace_path]
    subprocess.run(veth_commd, check=True)


def execute_get_namespace_blue():
    command = f"docker inspect ubuntu_blue | grep SandboxKey"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    output = result.stdout.strip()
    start_index = output.find('"/') + 2
    end_index = output.find('"', start_index)
    # Extract the namespace path
    namespace_path = output[start_index:end_index]
    namespace_path = '/'+ namespace_path
    print(namespace_path)
    veth_commd = ['sudo', 'ip', 'link', 'set', 'veth-b-cont', 'netns', namespace_path]
    subprocess.run(veth_commd, check=True)

def execute_get_namespace_ovs1():
    command = f"docker inspect ubun_cont_ovs1 | grep SandboxKey"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    output = result.stdout.strip()
    start_index = output.find('"/') + 2
    end_index = output.find('"', start_index)
    # Extract the namespace path
    namespace_path = output[start_index:end_index]
    namespace_path = '/'+ namespace_path
    print(namespace_path)
    veth_commd = ['sudo', 'ip', 'link', 'set', 'veth-r-ovs', 'netns', namespace_path]
    subprocess.run(veth_commd, check=True)
    veth_commd = ['sudo', 'ip', 'link', 'set', 'veth-b-ovs', 'netns', namespace_path]
    subprocess.run(veth_commd, check=True)

def execute_ip_addr():
    command_red = f"docker exec ubuntu_red ifconfig veth-r-cont 192.168.10.200/24"
    result = subprocess.run(command_red, shell=True, text=True)

    command_blue = f"docker exec ubuntu_blue ifconfig veth-b-cont 192.168.10.220/24"
    result = subprocess.run(command_blue, shell=True, text=True)

    command_ovs11 = f"docker exec ubuntu_red ifconfig veth-r-cont up"
    command_ovs12 = f"docker exec ubuntu_blue ifconfig veth-b-cont up"
    command_ovs13 = f"docker exec ubun_cont_ovs1 /usr/share/openvswitch/scripts/ovs-ctl start"
    command_ovs14 = f"docker exec ubun_cont_ovs1 ovs-vsctl add-br br0"
    command_ovs15 = f"docker exec ubun_cont_ovs1 ifconfig br0 up"
    command_ovs16 = f"docker exec ubun_cont_ovs1 ifconfig veth-r-ovs up"
    command_ovs17 = f"docker exec ubun_cont_ovs1 ifconfig veth-b-ovs up"
    command_ovs18 = f"docker exec ubun_cont_ovs1 ovs-vsctl add-port br0 veth-r-ovs"
    command_ovs19 = f"docker exec ubun_cont_ovs1 ovs-vsctl add-port br0 veth-b-ovs"
    result11 = subprocess.run(command_ovs11, shell=True, text=True)
    result12 = subprocess.run(command_ovs12, shell=True, text=True)
    result13 = subprocess.run(command_ovs13, shell=True, text=True)
    result14 = subprocess.run(command_ovs14, shell=True, text=True)
    result15 = subprocess.run(command_ovs15, shell=True, text=True)
    result16 = subprocess.run(command_ovs16, shell=True, text=True)
    result17 = subprocess.run(command_ovs17, shell=True, text=True)
    result18 = subprocess.run(command_ovs18, shell=True, text=True)
    result19 = subprocess.run(command_ovs19, shell=True, text=True)

# Call the function to execute Docker Compose
execute_docker_compose()
execute_virtual_interfaces()
execute_get_namespace_red()
execute_get_namespace_blue()
execute_get_namespace_ovs1()
execute_ip_addr()
