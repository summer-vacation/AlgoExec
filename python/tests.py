from django.test import TestCase

# Create your tests here.
import requests
import json
import base64


def test_update_remote_filters():
    test_url = "http://gmve-dev.gamematrix.oa.com/inner/edgegw/pre-process/perf-data-sidecar"
    data = {"deviceIds": ["test"]}
    encode_data = base64.b64encode(json.dumps(data).encode('utf-8'))
    print('{"content": "%s"}' % encode_data.decode("utf-8"))
    print('decode data: %s' % base64.b64decode(encode_data).decode())
    res = requests.post(url=test_url, data='{"content": "%s"}' % encode_data.decode("utf-8"))
    print(res.text)


class Solution:
    def minPathSum(self, grid) -> int:
        if grid is None or grid[0] is None:
            return 0
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                elif i == 0:
                    dp[i][j] = grid[i][j] + dp[i][j-1]
                elif j == 0:
                    dp[i][j] = grid[i][j] + dp[i-1][j]
                else:
                    dp[i][j] = min(grid[i][j] + dp[i][j-1], grid[i][j] + dp[i-1][j])
        return dp[i][j]


if __name__ == '__main__':
    # test_update_remote_filters()
    Solution().minPathSum([[1,2,5],[3,2,1]])
