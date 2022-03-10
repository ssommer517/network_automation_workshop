from scrapli import Scrapli


fw1 = {
    "host": "fw1",
    "auth_username": "admin",
    "auth_password": "Admin@123",
    "auth_strict_key": False,
    "ssh_config_file": True,
    "platform": "paloalto_panos"
}


def main():
    conn = Scrapli(**fw1)
    conn.open()

    print(conn.get_prompt())


if __name__ == "__main__":
    main()




