"""

Books updater for 69shu,Comrademao because I've overfilled my bookmarks!


"""

import requests
from bs4 import BeautifulSoup
import argparse
import json
import os
from rich.console import Console
from time import sleep
from googletrans import Translator

translator = Translator()
console = Console()
console.print("\nCN books stat updater\n", style="bold blue")
parser = argparse.ArgumentParser(description="CN books stat updater")
required = parser.add_argument_group('required arguments')
parser.add_argument('--link')
parser.add_argument('--chapter')
parser.add_argument('--check')
args, leftovers = parser.parse_known_args()

if args.link is not None:
	if '69shu' in args.link:
		console.print("You have inputted a 69shu link\n", style='bold red')
		page = requests.get(args.link)
		if page.status_code == 200:
			doesExist = os.path.exists(r'\Users\{yourUsername}\{yourFolder}\cnnovels.json')
			if doesExist == False:
				if args.chapter is not None:
					dict1 = {args.link : args.chapter}
					dictionary = {'69shu' : dict1}
					console.print("Inserting new novel to your personal list")
					with open("cnnovels.json", "w") as jsonFile:
						json.dump(dictionary, jsonFile, indent = 2)
				else:
					dict1 = {args.link : '1'}
					dictionary = {'69shu' : dict1}
					console.print("Inserting new novel to your personal list. Not finding chapter selection...Inputting 1 as chapter")
					with open("cnnovels.json", 'w') as jsonFile:
						json.dump(dictionary, jsonFile, indent = 2)
			else:
				if args.chapter is not None:
					with open("cnnovels.json", 'r') as jsonFile:
						data = json.load(jsonFile)
					if '69shu' in data:
						data['69shu'][args.link] = args.chapter				
						with open("cnnovels.json", 'w') as jsonFile:
							json.dump(data, jsonFile, indent = 2)
					else:
						with open("cnnovels.json", 'r') as jsonFile:
							data = json.load(jsonFile)
						dict1 = {args.link : args.chapter}
						dictionary = {'69shu' : dict1}
						data.update(dictionary)
						console.print("Inserting new novel to your personal list")
						with open("cnnovels.json", "w") as jsonFile:
							json.dump(data, jsonFile, indent = 2)
				else:
					print("It already exists!")
	else:
		console.print("You have inputted a comrademao link\n", style='bold red')
		headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
		page = requests.get(args.link, headers=headers)
		if page.status_code == 200:
			doesExist = os.path.exists(r'\Users\{yourUsername}\{yourFolder}\cnnovels.json')
			if doesExist == False:
				if args.chapter is not None:
					dict1 = {args.link : args.chapter}
					dictionary = {'ComradeMao' : dict1}
					console.print("Inserting new novel to your personal list")
					with open("cnnovels.json", "w") as jsonFile:
						json.dump(dictionary, jsonFile, indent = 2)
				else:
					dict1 = {args.link : '1'}
					dictionary = {'ComradeMao' : dict1}
					console.print("Inserting new novel to your personal list. Not finding chapter selection...Inputting 1 as chapter")
					with open("cnnovels.json", 'w') as jsonFile:
						json.dump(dictionary, jsonFile, indent = 2)
			else:
				if args.chapter is not None:
					with open("cnnovels.json", 'r') as jsonFile:
						data = json.load(jsonFile)
					if 'ComradeMao' in data:
						data['ComradeMao'][args.link] = args.chapter				
						with open("cnnovels.json", 'w') as jsonFile:
							json.dump(data, jsonFile, indent = 2)
					else:
						with open("cnnovels.json", 'r') as jsonFile:
							data = json.load(jsonFile)
						dict1 = {args.link : args.chapter}
						dictionary = {'ComradeMao' : dict1}
						data.update(dictionary)
						console.print("Inserting new novel to your personal list")
						with open("cnnovels.json", "w") as jsonFile:
							json.dump(data, jsonFile, indent = 2)
				else:
					print("It already exists!")
else:
	if args.check is not None:
		headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
		with open("cnnovels.json", 'r') as jsonFile:
			data = json.load(jsonFile)
		for link in data['69shu']:
			chapternum = int(data['69shu'][link])
			url = link.replace("/txt",'').replace('.htm','/')
			page = requests.get(url)
			if page.status_code == 200:
				soup = BeautifulSoup(page.content, 'html.parser')
				a = soup.find('div', class_ = 'mybox')
				b = a.find_all("div")
				c = b[-1].find('ul')
				d = c.find_all('li')
				h3 = a.find('h3')
				div_h3 = h3.find('div', class_='bread')
				a_bread = div_h3.find_all('a')
				title = translator.translate(a_bread[2].text)
				title = title.text
				console.print(title, style='green')
				if len(d) == chapternum:
					console.print("You are on the latest chapter. Come back and check again for new updates!\n")
				else:
					console.print("Current chapter: {}\n".format(chapternum))
					console.print("There are {} chapters you haven't read yet. You can visit the website at {} to read them now!\n".format(len(d) - chapternum, link))
				sleep(2)
		for link in data['ComradeMao']:
			chapternum = int(data['ComradeMao'][link])
			page = requests.get(link, headers=headers)
			if page.status_code == 200:
				soup = BeautifulSoup(page.content, 'html.parser')
				a = soup.find('div', class_ = 'eplister')
				b = a.find("ul")
				c = b.find_all('li')
				div = soup.find('div', class_ = 'infox')
				h1 = div.find('h1')
				title = h1.text
				console.print(title, style='green')
				if len(c) == chapternum:
					console.print("You are on the latest chapter. Come back and check again for new updates!\n")
				else:
					console.print("Current chapter: {}\n".format(chapternum))
					console.print("There are {} chapters you haven't read yet. You can visit the website at {} to read them now!\n".format(len(c) - chapternum, link))
			sleep(2)