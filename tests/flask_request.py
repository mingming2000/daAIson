import requests


if __name__ == '__main__':
    data = {'data': "hello, world!"}
    #resp = requests.post("http://192.168.137.87:8082/send", data=data)
    resp = requests.put("http://192.168.137.87:8083/send", data=data)
    print(resp.content)
