import requests
from pprint import pprint
from datetime import datetime
import os
import smtplib, ssl

class Server:
	def __init__(self,url):
		self.__url = url
	
	def get(self,id):
		if id == None:
			response = requests.get(self.__url)
		else:
			response = requests.get(f"{self.__url}/{id}")
		data = response.json()
		pprint(data)
		self.log("get")

	def post(self,new_data):
		response = requests.post(self.__url,data = new_data)
		data = response.json()
		pprint(data)
		self.log("post")

	def put(self,id,new_data):
		response = requests.put(f"{self.__url}/{id}",data = new_data)
		data = response.json()
		pprint(data)
		self.log("put")

	def delete(self,id):
		requests.delete(f"{self.__url}/{id}")
		pprint("ID " + str(self.id) + " is deteted")

	def log(self,method):
		path = f"{os.getcwd()}./Day12/nthanh/log.txt"
		date = datetime.now().strftime("%H:%M:%S %d/%m/%Y")
		log_msg = f"{method} - {date}"

		with open(path, 'a') as f_log:
			f_log.write(log_msg)


class Gmail(Server):
	def __init__(self):
		super().__init__(url)
	
	def congratulation(self, name, email):
		pass

if __name__ == "__main__":
	url = "https://60e484a35bcbca001749ea92.mockapi.io/human"
	id = None
	server = Server(url)
	# server.get(id)

	new_data = {
	"name": "Thanh",
	"age": 25,
	"email": "emailthanhnguyen19@gmail.com",
	"successful": "True",
	}
	server.post(new_data)

	