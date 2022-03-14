from jinja2 import Environment, FileSystemLoader

from scrapli import Scrapli

from scrapli_cfg import ScrapliCfg


def main():
    j2_env = Environment(
        loader=FileSystemLoader("/home/steve/network_automation_workshop/config_management"),
        lstrip_blocks=True, trim_blocks=True,
    )
    template = j2_env.get_template("eos.j2")

    device_data = {
        "leaf1": {
            "hostname": "leaf1",
            "v4_mgmt": "172.20.20.21/24",
            "v6_mgmt": "2001:172:20:20::21/64",
        },
        "leaf2": {
            "hostname": "leaf2",
            "v4_mgmt": "172.20.20.22/24",
            "v6_mgmt": "2001:172:20:20::22/64",
        },
        "spine1": {
            "hostname": "spine1",
            "v4_mgmt": "172.20.20.11/24",
            "v6_mgmt": "2001:172:20:20::11/64",
        }
    }

    login_banner = """
banner login
Way betterer login banner
**KEEP OUT!!!**


EOF"""

    rendered_configs = {}
    for host, template_data in device_data.items():
        rendered_configs[host] = template.render(**template_data)

    common_connection_data = {
        "auth_strict_key": False,
        "auth_username": "admin",
        "auth_password": "admin",
        "platform": "arista_eos"
    }

    for host in device_data:
        conn = Scrapli(host=host, **common_connection_data)
        conn.open()

        cfg_conn = ScrapliCfg(conn=conn)
        cfg_conn.prepare()

        cfg_conn.load_config(rendered_configs[host], replace=True)
        diff_result = cfg_conn.diff_config()

        print(diff_result.device_diff)

        cfg_conn.abort_config()
        cfg_conn.cleanup()
        conn.close()

if __name__ == "__main__":
    main()

