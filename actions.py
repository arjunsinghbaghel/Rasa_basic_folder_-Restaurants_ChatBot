from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

# from rasa_core.actions.action import Action
#from rasa_core_sdk import Action
#from rasa_core_sdk.forms import ( BooleanFormField, EntityFormField, FormAction, FreeTextFormField )
#from rasa_core_sdk.events import SlotSet
# from rasa_core.events import SlotSet
import zomatopy
import json
import smtplib
from email.message import EmailMessage

from rasa_sdk import Action
from rasa_sdk.events import SlotSet

zomato_config={ "user_key":"35a1d24cad5c2653361da4c1e0daf8da"}
result_of_last_query = ""

class ActionSearchRestaurants(Action):
	def name(self):
		return 'ActionSearchRestaurants'

	def findRestaurantBasedOnBudget(self, userbudget, allRestaurants):
		rangeMin = 0
		rangeMax = 100000
		
		prc = userbudget

		if prc == "Less than Rs.300":
			rangeMax = 300
		elif prc == "Between Rs.300 and 700" or prc == "700":
			rangeMin = 300
			rangeMax = 700
		elif prc == "More than Rs.700" or prc == "Rs.700":
			rangeMin = 700
		else:
			# default budget 
			rangeMin = 300
			rangeMax = 699

		index = 0
		count = 0
		response = ""
		global result_of_last_query
		result_of_last_query = ""

		for restaurant in allRestaurants:
			++count
			res = "[" + restaurant['restaurant']['user_rating']['aggregate_rating'] + "/5] " + restaurant['restaurant']['name'] + " in " + restaurant['restaurant']['location']['address']

			# price_range = str(restaurant['restaurant']['price_range'])
			avg_c_2 = restaurant['restaurant']['average_cost_for_two']

			# if price_range == "1":
			
			if avg_c_2 <= rangeMax and avg_c_2 >= rangeMin:
				
				# mapbybudget["1"].append(restaurant)
				# if userbudget == price_range:
				
				res = restaurant['restaurant']['currency'] + str(restaurant['restaurant']['average_cost_for_two']) + " " + res + "\n"
				if(index < 5):
					response = response + res

				if(index < 10):
					result_of_last_query = result_of_last_query + res
				index = index + 1

		# modifying the search results
		# if the no. of result fall short, appending the results of other price range
		if index == 0:
			response = "Oops! no restaurant found for this query. " + " search results = " + str(count)
		elif index < 5:
			# we can add restaurants from the higher range but for now i am appending an extra message 
			response = response + "\n \nFor more results please search in higher budget range...\n \n"
		elif index < 10:
			result_of_last_query = result_of_last_query + "\n \nFor more results please search in higher budget range...\n \n"

		return response

	def run(self, dispatcher, tracker, domain):
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		budget = tracker.get_slot('price')
		
		zomato = zomatopy.initialize_app(zomato_config)
		location_detail=zomato.get_location(loc, 1)

		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		
		cuisines_dict={
		'american':1,
		'mexican':73,
		'italian':55,
		'thai':95,
		'chinese':25,
		'north indian':50,
		'cafe':30,
		'bakery':5,
		'biryani':7,
		'south indian':85
		}

		results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 50)

		d = json.loads(results)
		response=""

		if d['results_found'] == 0:
			response= "Sorry, we didn't find any results for this query."
		else:
			# dispatcher.utter_message(str(d))
			response = self.findRestaurantBasedOnBudget(budget, d['restaurants'])

		dispatcher.utter_message(str(response))
		return [SlotSet('location',loc)]


t1_t2_cities = ["Ahmedabad","Bangalore","Chennai","Delhi","Hyderabad","Kolkata","Mumbai","Pune",
"Agra","Ajmer","Aligarh","Allahabad","Amravati","Amritsar","Asansol","Aurangabad",
"Bareilly","Belgaum","Bhavnagar","Bhiwandi","Bhopal","Bhubaneswar",
"Bikaner","Bokaro Steel City","Chandigarh","Coimbatore","Cuttack","Dehradun",
"Dhanbad","Durg-Bhilai Nagar","Durgapur","Erode","Faridabad","Firozabad","Ghaziabad",
"Gorakhpur","Gulbarga","Guntur","Gurgaon","Guwahati",
"Gwalior","Hubli-Dharwad","Indore","Jabalpur","Jaipur","Jalandhar","Jammu","Jamnagar","Jamshedpur","Jhansi","Jodhpur",
"Kannur","Kanpur","Kakinada","Kochi","Kottayam","Kolhapur","Kollam","Kota","Kozhikode","Kurnool","Lucknow","Ludhiana",
"Madurai","Malappuram","Mathura","Goa","Mangalore","Meerut",
"Moradabad","Mysore","Nagpur","Nanded","Nashik","Nellore","Noida","Palakkad","Patna","Pondicherry","Raipur","Rajkot",
"Rajahmundry","Ranchi","Rourkela","Salem","Sangli","Siliguri",
"Solapur","Srinagar","Sultanpur","Surat","Thiruvananthapuram","Thrissur","Tiruchirappalli","Tirunelveli","Tiruppur",
"Ujjain","Vijayapura","Vadodara","Varanasi",
"Vasai-Virar City","Vijayawada","Visakhapatnam","Warangal"]

t1_t2_cities_list = [x.lower() for x in t1_t2_cities]

# Check if the location exists. using zomato api.if found then save it, else utter not found.
class ActionValidateLocation(Action):
	def name(self):
		return 'validate_location'

	def run(self, dispatcher, tracker, domain):
		loc = tracker.get_slot('location')
		city = str(loc)
		# dispatcher.utter_message(city)

		if city.lower() in t1_t2_cities_list:
			return [SlotSet('loc_avl',"1")]
		else:
			zomato = zomatopy.initialize_app(zomato_config)

			try:
				results = zomato.get_city_ID(city)
				return [SlotSet('loc_avl',"1")]
			except:
				# results = "Sorry, didn’t find any such location. Can you please tell again?" + "-----" + city
				# dispatcher.utter_message(city)
				return [SlotSet('loc_avl',"0")]


# Send email the list of 10 restaurants
class ActionSendEmail(Action):
	def name(self):
		return 'send_email'

	def run(self, dispatcher, tracker, domain):
		to_addr = tracker.get_slot('emailid')
		
		# for slack handling
		#if len(to_addr.split("|")) == 2:
		#	to_addr = to_addr.split("|")[1]

		import smtplib,ssl
		context = ssl.create_default_context()
		s = smtplib.SMTP('smtp.gmail.com', 587)
		s.ehlo()
		s.starttls(context=context)
		s.ehlo()
		s.login("restaurantchatbotp@gmail.com", "programmer@work")
		message = "The details of all the restaurants you inquried \n \n"
		global result_of_last_query
		message = message + result_of_last_query
		try:
			s.sendmail("restaurantchatbotp@gmail.com", str(to_addr), message)
                        #s.send_message(message, "restaurantchatbotp@gmail.com", str(to_addr))
			s.quit()
		except Exception as e:
                        print(e)
                        dispatcher.utter_message(to_addr)

		result_of_last_query = ""
		return [AllSlotsReset()]

#from rasa_core_sdk.events import AllSlotsReset
#from rasa_core_sdk.events import Restarted

from rasa_sdk.events import AllSlotsReset
from rasa_sdk.events import Restarted

class ActionRestarted(Action): 	
	def name(self):
		return 'action_restart'
	def run(self, dispatcher, tracker, domain):
		return[Restarted()] 

class ActionSlotReset(Action): 
	def name(self): 
		return 'action_slot_reset' 
	def run(self, dispatcher, tracker, domain): 
		return[AllSlotsReset()]
