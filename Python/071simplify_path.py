class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """

        result = []
        path_list = path.split('/')

        for s in path_list:
            if not s or s == '.':
                continue
            elif s == '..':
                if result:
                    result.pop()
            else:
                result.append(s)

        return '/' + '/'.join(result)
