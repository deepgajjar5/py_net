import paramiko

def make_connection(ip_addr, username, password):
    conn = paramiko.SSHClient()
    conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    conn.connect(ip_addr, username = username, password = password)
    return conn

def send_commands(conn):
    conn1 = conn.invoke_shell()
    conn1.send("configure terminal\n")
    conn1.send("configure terminal\n")
    conn1.send("logging buffered 19945\n")
    conn1.send("show run\n")
    conn1.recv(100000)

def input_parameters():
    ip_addr = raw_input("Enter the IP address here: ")
    username = raw_input("Enter username here: ")
    password = raw_input("Enter password here: ")

    return ip_addr, username, password

ip_addr, username, password = input_parameters()

conn = make_connection(ip_addr, username, password)

send_commands(conn)

