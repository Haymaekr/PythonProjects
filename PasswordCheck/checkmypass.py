import requests
import hashlib
import sys

def request_api_data(query_char):
	url = 'https://api.pwnedpasswords.com/range/' + query_char
	res = requests.get(url)
	if res.status_code !=200:
		raise RuntimeError(f'Erroe fetchinh: {res.status_code}, check the code or api')
	return res

def get_leaks_count(hash_response, hash_tocheck):
	hash_response = (line.split(':') for line in hash_response.text.splitlines())
	for h,count in hash_response:
		if h == hash_tocheck:
			return count
	return 0

def pwn_api_check(password):

	sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
	first5 , tail = sha1password[:5],sha1password[5:]
	response = request_api_data(first5)
	return get_leaks_count(response, tail)

def main(args):
	for password in args:
		count = pwn_api_check(password)
		if count:
			print(f'''The {password} was found {count} times.
				You should change your password''')
		else:
			print(f"Your password {password} is good. Right on mate!")
	return "FIN"

if __name__ == '__main__':
	sys.exit(main(sys.argv[1:]))