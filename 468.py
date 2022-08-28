class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if '.' in queryIP and ':' in queryIP:
            return 'Neither'
        if '.' in queryIP:
            fields = queryIP.split('.')
            if len(fields) != 4:
                return 'Neither'
            for field in fields:
                if not 1 <= len(field) <= 3:
                    return 'Neither'
                if field[0] == '0':
                    if len(field) > 1:
                        return 'Neither'
                else:
                    if not field.isdigit() or not 0 <= int(field) <= 255:
                        return 'Neither'
            return 'IPv4'
        else:
            fields = queryIP.split(':')
            chars = set('0123456789abcdefABCDEF')
            if len(fields) != 8:
                return 'Neither'
            for field in fields:
                if not 1 <= len(field) <= 4:
                    return 'Neither'
                for c in field:
                    if c not in chars:
                        return 'Neither'
            return 'IPv6'
