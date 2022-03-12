from scrapli import Scrapli

import re

content = """
Building configuration... Current configuration : 6969 bytes
!
! Last configuration change at 06:36:23 UTC Thu Mar 10 2022 by admin
!
version 16.12 service timestamps debug datetime msec service timestamps log datetime msec service call-home platform qfp 
utilization monitor load 80 platform punt-keepalive disable-kernel-core platform console serial
!
hostname rtr1
!
boot-start-marker boot-end-marker
!
"""

leaf1 = {
    "host": "leaf1",
    "auth_username": "admin",
    "auth_password": "admin",
    "auth_strict_key": False,
    "platform": "arista_eos",
}


def main():
    result = re.search(r"version (\d{2})\.(\d{2})", content)
    print(result, type(result), dir(result))
    print(result.group())
    print(f"First Group {result.group(1)}")
    print(f"Second Group {result.group(2)}")

    print(f"First Group {result.groups(0)}")
    print(f"Second Group {result.groups(1)}")

    conn = Scrapli(**leaf1)
    conn.open()
    response = conn.send_command(command="show interface management 0")

    mgmt_address_match = re.search(r"internet address is (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/\d{1,2})", string=response.result, flags=re.I)
    uptime_match = re.search(f"^  up (.*)", string=response.result, flags=re.I | re.M)

    print(f"Mgmt address: {mgmt_address_match.group()}")
    print(f"Uptime: {uptime_match.group()}")

    single_pattern_match = re.search(r"internet address is (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/\d{1,2})(?:[\s\S]+)(up .*)", string=response.result, flags=re.I)
    print(f"Mgmt address: {single_pattern_match.groups()[0]}")
    print(f"Uptime: {single_pattern_match.groups()[1]}")

    named_pattern_match = re.search(r"internet address is (?P<mgmt>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/\d{1,2})(?:[\s\S]+)(?P<uptime>up .*)", string=response.result, flags=re.I) 
    print(f"Mgmt address: {named_pattern_match.groupdict()['mgmt']}")
    print(f"Uptime: {named_pattern_match.groupdict()['uptime']}")

    bytes_match =  re.findall(f"\d+ bytes$", string=response.result, flags=re.M)
    print(f"Output bytes: {bytes_match[0]}")
    print(f"Inupt bytes: {bytes_match[1]}")


if __name__ == "__main__":
    main()


