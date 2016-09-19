import paramiko

def make_connection(ip_addr, username, password):
    conn = paramiko.SSHClient()
    conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    conn.connect(ip_addr, username = username, password = password)
    return conn

def send_commands(conn):
    stdin, stdout, stderror = conn.exec_command("show version")
    return stdin, stdout, stderror

def input_parameters():
    ip_addr = raw_input("Enter the IP address here: ")
    username = raw_input("Enter username here: ")
    password = raw_input("Enter password here: ")

    return ip_addr, username, password

ip_addr, username, password = input_parameters()

conn = make_connection(ip_addr, username, password)

stdin, stdout, stderror = send_commands(conn)

print stdout.read()
