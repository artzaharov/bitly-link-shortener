import requests


LONG_LINKS_FILE = 'longlinks.txt'
SHORT_LINKS_FILE = 'shortlinks.txt'


def get_short_links():
	headers = {
		'Authorization': 'Bearer XXXXXXX',  # Вместо XXXXXXX вставить свой API Key с сервиса bitly.com
		'Content-Type': 'application/json',
	}

	try:
		with open(LONG_LINKS_FILE) as file:
			links = file.readlines()
	except Exception as ex:
		print(ex)
		return ''

	result = []
	for link in links:
		link = link.strip()
		data = '{"long_url": "' + link + '", "domain": "bit.ly"}'

		try:
			response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, data=data)
			result.append(response.json().get('link') + '\n')
			print(f'Ready: {link}')
		except Exception as ex:
			print(ex)
			continue

	return result


def main():
	result = get_short_links()
	if result:
		with open(SHORT_LINKS_FILE, 'w') as file:
			file.writelines(result)


if __name__ == '__main__':
	main()
