from jkdk import Jkdk
import os
# import argparse

# parser = argparse.ArgumentParser(description='填入学号和密码')
# parser.add_argument('-c', '--credit', required=True, help='学号')
# parser.add_argument('-p', '--password', required=True, help='密码')

# outputs = parser.parse_args()
# print(f'credit={outputs.credit}, password={outputs.password}')

username = os.environ.get('username')
password = os.environ.get('password')
key = os.environ.get('key')
province = os.environ.get('province')
city = os.environ.get('city')
position = os.environ.get('position')
city = province+city


print(f'username={username}')
print(f'password={password}')
print(f'SCKEY={key}')
print(f'province={province}')
print(f'city={city}')
print(f'position={position}')

if key == '':
    key = None
m = Jkdk(username, password, key, province=province,
         city=city, position=position)
m.jkdk()


username1 = os.environ.get('username1')
password1 = os.environ.get('password1')
key1 = os.environ.get('key1')
province1 = os.environ.get('province1')
city1 = os.environ.get('city1')
position1 = os.environ.get('position1')
city1 = province1+city1


print(f'username={username1}')
print(f'password={password1}')
print(f'SCKEY={key1}')
print(f'province={province1}')
print(f'city={city1}')
print(f'position={position1}')

if key1 == '':
    key1 = None
m1 = Jkdk(username1, password1, key1, province=province1,
         city=city1, position=position1)
m1.jkdk()


