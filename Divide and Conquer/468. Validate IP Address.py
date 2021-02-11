class Solution:
    def validIPAddress(self, IP: str) -> str:
        ipv4 = r'([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'
        pattern_ipv4 = re.compile(r'^('+ipv4+r'\.){3}'+ipv4+r'$')
        ipv6 = r'[0-9a-fA-F]{1,4}'
        pattern_ipv6 = re.compile(r'^('+ipv6+r'\:){7}'+ipv6+r'$')

        if '.' in IP:
            return "IPv4" if pattern_ipv4.match(IP) else "Neither"
        else:
            return "IPv6" if pattern_ipv6.match(IP) else "Neither"

执行用时：36 ms, 在所有 Python3 提交中击败了80.04%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了26.43%的用户

