from jinja2 import Environment, FileSystemLoader


def main():
    j2_env = Environment(
        loader=FileSystemLoader("/home/steve/network_automation_workshop/http")
    )
    template = j2_env.get_template("acl.j2")

    acl_lines = [
        " deny ip 0.0.0.0 0.255.255.255 any",
        " deny ip 10.0.0.0 0.255.255.255 any",
        " deny ip 100.64.0.0 0.63.255.255 any",
        " deny ip 127.0.0.0 0.255.255.255 any",
        " deny ip 169.254.0.0 0.0.255.255 any",
        " deny ip 172.16.0.0 0.15.255.255 any",
        " deny ip 192.0.0.0 0.0.0.255 any",
        " deny ip 192.0.2.0 0.0.0.255 any",
        " deny ip 192.168.0.0 0.0.255.255 any",
        " deny ip 198.18.0.0 0.1.255.255 any",
        " deny ip 198.51.100.0 0.0.0.255 any",
        " deny ip 203.0.113.0 0.0.0.255 any",
        " deny ip 224.0.0.0 15.255.255.255 any",
        " deny ip 240.0.0.0 15.255.255.255 any"
    ]

    print(template.render(acl_lines=acl_lines))


    template_v2 = j2_env.get_template("aclv2.j2")

    acl_lines_v2 = [
        {"action": " deny", "protocol": "ip", "source": "0.0.0.0 0.255.255.255", "dest": "any"},
        {"action": " deny", "protocol": "ip", "source": "10.0.0.0 0.255.255.255", "dest": "any"},
        {"action": " deny", "protocol": "ip", "source": "100.64.0.0 0.63.255.255", "dest": "any"},
        {"action": " deny", "protocol": "ip", "source": "127.0.0.0 0.255.255.255", "dest": "any"},
        {"action": " deny", "protocol": "ip", "source": "169.254.0.0 0.0.255.255", "dest": "any"},
        {"action": " deny", "protocol": "ip", "source": "172.16.0.0 0.15.255.255", "dest": "any"},
        {"action": " deny", "protocol": "ip", "source": "192.0.0.0 0.0.0.255", "dest": "any"},
        {"action": " deny", "protocol": "ip", "source": "192.0.2.0 0.0.0.255", "dest": "any"},
        {"action": " deny", "protocol": "ip", "source": "192.168.0.0 0.0.255.255", "dest": "any"},
        {"action": " deny", "protocol": "ip", "source": "198.18.0.0 0.1.255.255", "dest": "any"},
        {"action": " deny", "protocol": "ip", "source": "198.51.100.0 0.0.0.255", "dest": "any"},
        {"action": " deny", "protocol": "ip", "source": "203.0.113.0 0.0.0.255", "dest": "any"},
        {"action": " deny", "protocol": "ip", "source": "224.0.0.0 15.255.255.255", "dest": "any"},
        {"action": " deny", "protocol": "ip", "source": "240.0.0.0 15.255.255.255", "dest": "any"},
    ]

    print(template_v2.render(acl_lines=acl_lines_v2))


if __name__ == "__main__":
    main()
