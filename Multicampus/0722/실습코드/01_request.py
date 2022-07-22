import requests
r = requests.get('https://api.github.com/user', auth=('user','pass'))
print(r.status_code)

# user,pass 입력안해서 실제로는 401에러남.