from netmiko import ConnectHandler

# 1 create the device object using a dictionary
CSR = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.220',
    'username': 'roger',
    'password': 'cisco'
}

# 2 establish the SSH connection
net_connect = ConnectHandler(**CSR)

# 3 the hostname from the prompt 

hostname = net_connect.send_command('show run | i host')
hostname.split(" ")
hostname,device = hostname.split(" ")
print ("Backing up " + device)

# 4 save backup 
filename = '/home/macallister-crane/Network_scripts/backups/' + device + '.txt'


showrun = net_connect.send_command('show run')
showvlan = net_connect.send_command('show vlan')
showver = net_connect.send_command('show ver')
log_file = open(filename, "a")   # in append mode
log_file.write(showrun)
log_file.write("\n")
log_file.write(showvlan)
log_file.write("\n")
log_file.write(showver)
log_file.write("\n")

# Close the connection
net_connect.disconnect()