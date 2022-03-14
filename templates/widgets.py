from jinja2 import Environment, FileSystemLoader


def main():
    j2_env = Environment(
        loader=FileSystemLoader("/home/steve/network_automation_workshop/templates")
        lstrip_blocks=True, trim_blocks=True
    )
    template = j2_env.get_template("interfacev2.j2")

    interfaces = [
        {
            "intf_num": "1",
            "mode": "l3",
            "ip_addr": "1.1.1.1/30",
            "descr": "tacocat was here again!",
        },
        {
            "intf_num": "2",
            "mode": "l3",
            "ip_addr": "2.2.2.2/30",
            "descr": "racecar potato",
        },
        {"intf_num": "3", "mode": "l2", "descr": "is it lunch yet??"},
        {"intf_num": "4", "mode": "l3", "ip_addr": "4.4.4.4/30", "descr": "zzzzzzz"},
    ]

    print(template.render(interfaces=interfaces))


if __name__ == "__main__":
    main()
