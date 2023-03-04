# Write by New Bing
# 导入ipaddress模块
import ipaddress

# 定义一个函数，接受一个CIDR格式的地址作为参数
def parse_cidr(cidr):
    # 用ipaddress模块创建一个IPNetwork对象，根据地址的类型自动判断是IPv4还是IPv6
    try:
        net = ipaddress.ip_network(cidr)
    except ValueError:
        print('输入有误！请重新检查！')
        print('你的输入：', cidr)
        exit(1)
    # 输出起始和终止可用十进制格式IP地址
    print(f"起始可用IP地址：{net[1]}")
    if isinstance(net, ipaddress.IPv4Network):
        print(f"终止可用IP地址：{net[-2]}")
    else:
        print(f"终止可用IP地址：{net[-1]}")
    # 输出可用地址数量
    if isinstance(net, ipaddress.IPv4Network):
        print(f"可用地址数量：{net.num_addresses - 2}")
    else:
        print(f"可用地址数量：{net.num_addresses - 1}")
    # 输出十进制格式子网掩码
    print(f"子网掩码：{net.netmask}")
    # 输出十进制格式网络号和广播地址（如果是IPv6，则没有广播地址）
    print(f"网络号：{net.network_address}")
    if isinstance(net, ipaddress.IPv4Network):
        print(f"广播地址：{net.broadcast_address}")
    else:
        print("广播地址：检测到IPv6，无广播地址。")

# 测试一下
cidr = input('请输入CIDR格式的IP地址（例如192.168.1.0/24或2001:db8::/32）：')
parse_cidr(cidr)
