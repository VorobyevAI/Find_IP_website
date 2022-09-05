import socket

def get_ip():
    ###Finds the Ip address of the website by the name of the domain name.###

    hostname = input('Enter the domain name: ')
    try:
        return f" Hostname: {hostname}, \n IP address: {socket.gethostbyname(hostname)}"

    except socket.gaierror as error:
        return f" An error has occurred!\n Error: {error}"


def main():
    print(get_ip())


if __name__ == "__main__":
    main()