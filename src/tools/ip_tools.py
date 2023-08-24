from ipaddress import ip_address


def get_filename_from_ip(client_ip,type_file:str='.xlsx'):
    ip = ip_address(client_ip)
    filename = str(ip).replace('.', '') + type_file
    return filename

