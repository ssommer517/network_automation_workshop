import pexpect def main(): child = pexpect.spawn("ssh 172.20.20.21 -l admin") print(child, type(child), dir(child)) 
print(child.before) print(child.after) child.expect("Password:") print(child.before) print(child.after) 
child.sendline("admin") child.expect("leaf1") print(child.before) print(child.after) child.sendline("show version") 
child.expect("leaf1") print(child.before) print(child.after) show_version_bytes = child.before show_version = 
show_version_bytes.decode() show_version_clean = show_version.split("show version")[1] print(show_version_clean) 
child.sendline("enable") child.expect("leaf1") child.sendline("terminal length 0") child.expect("leaf1#") 
child.sendline("show run") child.expect("leaf1#") show_run_bytes = child.before show_run = show_run_bytes.decode() 
show_run_clean = show_run.lstrip("show run") print(show_run_clean) if __name__ == "__main__": main()
