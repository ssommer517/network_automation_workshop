from scrapli import Scrapli
from scrapli_cfg import ScrapliCfg

def main():
    dev = {
        "host": "spine1",
        "auth_username": "admin",
        "auth_password": "admin",
        "auth_strict_key": False,
        "platform": "arista_eos"
    }

    conn = Scrapli(**dev)
    conn.open()

    cfg_conn = ScrapliCfg(conn=conn)
    print(type(cfg_conn), dir(cfg_conn))

    cfg_conn.prepare()

    get_result = cfg_conn.get_config()
    print(type(get_result), dir(get_result))

    print(get_result.result)

    with open("spine1.config", "r") as f:
        spine1_cfg = f.read()

    loadcfg = cfg_conn.load_config(spine1_cfg)
    print(type(loadcfg), dir(loadcfg))

    diff_result = cfg_conn.diff_config()
    print(type(diff_result), dir(diff_result))
    print(diff_result.device_diff)
    print(diff_result.side_by_side_diff)
    print(diff_result.unified_diff)

    #cfg_conn.abort_config()
    cfg_conn.commit_config()
    cfg_conn.cleanup()


if __name__ == "__main__":
    main()

