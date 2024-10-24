from netmiko import ConnectHandler

#1 create the device object using a dictionary
CSR = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.220',
    'username': 'roger',
    'password': 'cisco'
}

# 2 establish the SSH connection
net_connect = ConnectHandler(**CSR)

# 3 send the command and print the output
output = net_connect.send_command('show ip int brief')
print (output)

# 4 close the connection
net_connect.disconnect()