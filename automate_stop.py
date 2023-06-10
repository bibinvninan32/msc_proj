import subprocess

def execute_docker_compose():
    # Change the directory to the location of your docker-compose.yml file
    compose_directory = '/home/bibin/msc_pro/docker_comp/'
    
    # Command to execute docker-compose
    command = ['docker-compose', '-f', 'docker-compose1.yml', 'down']
    command = ['docker-compose', '-f', 'docker-compose2.yml', 'down']

    
    # Run the command as a subprocess
    subprocess.run(command, cwd=compose_directory, check=True)

# Call the function to execute Docker Compose
execute_docker_compose()
