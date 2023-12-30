from setuptools import setup
import getpass, os

import tests

def install_require():
    if getpass.getuser() == "root":
        c = input("Do you want to install Silence VPN? (y/n): ")
        if c == "y":
            print("Installing Silence VPN...")
            os.system("pip install -r requirements.txt")
            os.system("python src/main.py")
        else:
            print("Aborting installation...")

    if getpass.getuser() == "root":
        c = input("Install OpenVPN? (y/n): ")
        if c == "y":
            print("Installing OpenVPN...")
            os.system("./openvpn-install.sh")
        else:
            print("Aborting installation...")

def test_db():
    print("Testing Silence VPN...")
    print("Testing connection to database...")
    if tests.DatabaseConnectionTest().main():
        print("Connection to database failed.")
    else:
        print("Connection to database successed.")


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="Silence VPN",
    version="0.0.1",
    author="TryWarz",
    author_email="trywarz.contact@gmail.com",
    description="Silence VPN is a VPN written in Python.",
)

if __name__ == "__main__":
    install_require()
    test_db()