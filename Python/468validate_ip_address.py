class Solution:
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        if self.check_IPV4(IP):
            return 'IPv4'
        elif self.check_IPV6(IP):
            return 'IPv6'
        else:
            return 'Neither'

    def check_IPV4(self, IP):
        """
        :type IP: str
        :rtype: bool
        """
        groups = IP.split('.')
        # four decimal numbers
        if len(groups) != 4:
            return False
        # no leading zeros
        for num in groups:
            if len(num) > 1 and num[0] == '0':
                return False
        # valid number
        for num in groups:
            if not num.isdigit():
                return False
            num = int(num)
            if num < 0 or num > 255:
                return False
        return True

    def check_IPV6(self, IP):
        """
        :type IP: str
        :rtype: bool
        """
        groups = IP.split(':')
        # 8 hexadecimal numbers
        if len(groups) != 8:
            return False
        # no empty group or extra leading zero
        for num in groups:
            if len(num) == 0 or len(num) > 4:
                return False
        # valid hexadecimal digits
        hexnum = '0123456789abcdefABCDEF'
        for num in groups:
            if not all(d in hexnum for d in num):
                return False
        return True
