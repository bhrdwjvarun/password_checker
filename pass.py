import requests
import sys
import hashlib


def checker(hashes):
		for h,count in hashes:
			if h==tail:
				return count
		return 0

for str in sys.argv[1:] :
	result = hashlib.sha1(str.encode()).hexdigest().upper()
	head = result[:5]
	tail = result[5:]
	url = 'https://api.pwnedpasswords.com/range/' + head
	res = requests.get(url)
	hashes = (line.split(':') for line in res.text.splitlines())
	abc = checker(hashes)
	if abc:
		print(f'\nyour password \"{str}\" has been found {abc} times, you might want to change your password\n')
	else:
		print(f'\ncarry on with your password \"{str}\" \n')