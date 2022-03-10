from scrapli import Scrapli


rtr1 = {
    "host": "rtr1",
    "auth_username": "admin",
    "auth_password": "admin",
    "auth_strict_key": False,
    "ssh_config_file": True,
    "platform": "cisco_iosxe"
}


def main():
    conn = Scrapli(**rtr1)
    conn.open()

    print(conn.get_prompt())

    responses = conn.send_configs(configs=["interface loopback0", "description tacocat"])
    print(responses)

    print(conn.get_prompt())

    response = conn.send_command(command="show run interface loopback0")
    print(response.result)


if __name__ == "__main__":
    main()




