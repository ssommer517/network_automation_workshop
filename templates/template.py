from jinja2 import Environment, FileSystemLoader


def main():
    j2_env = Environment(loader=FileSystemLoader("/home/steve/network_automation_workshop/templates"))
    template = j2_env.get_template("interface.j2")


if __name__ == "__main__":
   main()

