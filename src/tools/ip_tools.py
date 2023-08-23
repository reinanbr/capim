


def get_filename_from_ip(client_ip):
    ip = ip_address(client_ip)
    filename = str(ip).replace('.', '') + '.xlsx'
    return filename

