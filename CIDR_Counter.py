# 导入ipaddress模块，用于处理IP地址和子网
import ipaddress

# 定义一个函数，根据输入的CIDR格式的IP地址返回所需的信息
def get_ip_info(cidr):
    # 尝试将输入转换为ipaddress对象，如果失败则抛出异常
    try:
        ip = ipaddress.ip_network(cidr)
    except ValueError as e:
        print("无效的IP地址或CIDR格式:", e)
        return
    
    # 获取主机可用的起始和结束IP地址，转换为十进制字符串
    start_ip = str(ip[1])
    end_ip = str(ip[-2])

    # 获取主机可用的IP地址数量
    num_hosts = ip.num_addresses - 2

    # 获取十进制子网掩码，转换为十进制字符串
    netmask = str(ip.netmask)

    # 获取网络号和广播地址或多播地址，转换为十进制字符串
    network = str(ip.network_address)
    
    # 判断IP版本，如果是4则输出广播地址，如果是6则输出多播地址
    if ip.version == 4:
        broadcast_or_multicast = "广播"
        address = str(ip.broadcast_address)
    elif ip.version == 6:
        broadcast_or_multicast = "多播"
        address = str(ip.network_address + 1) # 多播地址通常是网络号加1
    
    # 打印结果
    print("主机可用的起始IP地址:", start_ip)
    print("主机可用的结束IP地址:", end_ip)
    print("主机可用的IP地址数量:", num_hosts)
    print("十进制子网掩码:", netmask)
    print("网络号:", network)

    # 根据IP版本输出不同的结果
    if ip.version == 4:
        print(broadcast_or_multicast + "地址:", address)
    elif ip.version == 6:
        print(broadcast_or_multicast + "组:", address)

# 测试函数
cidr = input('请输入CIDR格式的IP地址（例如192.168.1.0/24或2001:db8::/32）：')
get_ip_info(cidr)
