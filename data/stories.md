## Generated Story -7882715103327446561
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - utter_ask_budget
* restaurant_search{"price": "Rs.300 to 700"}
    - slot{"price": "300 to 700"}
    - ActionSearchRestaurants
    - slot{"location": "Delhi"}
* restaurant_search
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email
    - slot{"emailid": "arjunsingh89baghel@gmail.com"}
    - send_email
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## Generated Story -3898277359004523010
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Mumbai"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Mumbai"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "300 to 700"}
    - slot{"price": "300 to 700"}
    - ActionSearchRestaurants
    - slot{"location": "Mumbai"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email
    - slot{"emailid": "arjunsingh89baghel@gmail.com"}
    - send_email
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## Generated Story 7048052416262072766
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Mumbai", "price": "more than 700"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Mumbai"}
    - slot{"price": "more than 700"}
    - validate_location
    - slot{"loc_avl": "1"}
    - ActionSearchRestaurants
    - slot{"location": "Mumbai"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "more than 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email
    - slot{"emailid": "arjunsingh89baghel@gmail.com"}
    - send_email
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## Generated Story -3898277359004523011
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "300 to 700"}
    - slot{"price": "300 to 700"}
    - ActionSearchRestaurants
    - slot{"location": "Jaipur"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email
    - slot{"emailid": "arjunsingh89baghel@gmail.com"}
    - send_email
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## Generated Story 7895360618332411983
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - utter_ask_budget
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - ActionSearchRestaurants
    - slot{"location": "Mumbai"}
    - slot{"cuisine": "Chinese"}
    - slot{"price": "more than 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email
    - slot{"emailid": "arjunsingh89baghel@gmail.com"}
    - send_email
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
	
############################# STORIES WITH ALL VALID PARAMS AND SEND MAIL NOT CHOESN ############################ 

## Generated Story -6062178547877207050
* greet
    - utter_greet
* restaurant_search{"location": "Lucknow"}
    - slot{"location": "Lucknow"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_budget
* restaurant_search{"price": "300 to 700"}
    - slot{"price": "300 to 700"}
    - ActionSearchRestaurants
    - slot{"location": "Lucknow"}
    - slot{"cuisine": "Mexican"}
    - slot{"price": "300 to 700"}
    - utter_ask_sendmail
* deny
    - utter_no_email_sent
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## Generated Story -3898277359004523010
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Mumbai"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Mumbai"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "300 to 700"}
    - slot{"price": "300 to 700"}
    - ActionSearchRestaurants
    - slot{"location": "Mumbai"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "300 to 700"}
    - utter_ask_sendmail
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## Generated Story -7048052416262072766
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Mumbai", "price": "more than 700"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Mumbai"}
    - slot{"price": "more than 700"}
    - validate_location
    - slot{"loc_avl": "1"}
    - ActionSearchRestaurants
    - slot{"location": "Mumbai"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "more than 700"}
    - utter_ask_sendmail
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## Generated Story -7895360618332411983
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - utter_ask_budget
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - ActionSearchRestaurants
    - slot{"location": "Mumbai"}
    - slot{"cuisine": "Chinese"}
    - slot{"price": "more than 700"}
    - utter_ask_sendmail
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
	
########################## STORIES WITH INVALID LOCATION ##########################################	
	
## Generated Story -4032620909897627882
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "mirzapur"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "mirzapur"}
    - validate_location
    - slot{"loc_avl": "0"}
    - utter_do_not_operate
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## Generated Story 596563140856362927
* greet
    - utter_greet
* restaurant_search{"location": "wasseypur"}
    - slot{"location": "wasseypur"}
    - validate_location
    - slot{"loc_avl": "0"}
    - utter_do_not_operate
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## Generated Story -4666364952305038038
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "wasseypur"}
    - slot{"location": "wasseypur"}
    - validate_location
    - slot{"loc_avl": "0"}
    - utter_do_not_operate
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

############################ STORIES WITH INVALID CUISINE ENTERED #############################

## Generated Story -4851377152726938344
* greet
    - utter_greet
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_budget
* restaurant_search{"price": "300 to 700"}
    - slot{"price": "300 to 700"}
    - ActionSearchRestaurants
    - slot{"location": "Delhi"}
    - slot{"cuisine": "italian"}
    - slot{"price": "300 to 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email
    - slot{"emailid": "arjunsingh89baghel@gmail.com"}
    - send_email
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## Generated Story -625261534328078868
* greet
    - utter_greet
* restaurant_search{"cuisine": "moroccan", "location": "Mumbai"}
    - slot{"cuisine": "moroccan"}
    - slot{"location": "Mumbai"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - ActionSearchRestaurants
    - slot{"location": "Mumbai"}
    - slot{"cuisine": "Mexican"}
    - slot{"price": "more than 700"}
    - utter_ask_sendmail
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## Generated Story 7895360618332411983
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - utter_ask_budget
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - ActionSearchRestaurants
    - slot{"location": "Mumbai"}
    - slot{"cuisine": "Chinese"}
    - slot{"price": "more than 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email
    - slot{"emailid": "arjunsingh89baghel@gmail.com"}
    - send_email
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
	
################################## STORIES WITH INVALID PRICE #############################
	
## Generated Story 2894257700257618989
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Kochi", "price": "200 to 600"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Kochi"}
    - slot{"price": "200 to 600"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "300 to 700"}
    - slot{"price": "300 to 700"}
    - ActionSearchRestaurants
    - slot{"location": "Kochi"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "300 to 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email
    - slot{"emailid": "arjunsingh89baghel@gmail.com"}
    - send_email
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## Generated Story -1273872810590943832
* greet
    - utter_greet
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
* restaurant_search{"price": "less than 500"}
    - slot{"price": "less than 500"}
    - ActionSearchRestaurants
    - slot{"location": "chennai"}
    - slot{"cuisine": "North Indian"}
    - slot{"price": "less than 300"}
    - utter_ask_sendmail
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## Generated Story -3898277359004523010
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Mumbai"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Mumbai"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "less than 500"}
    - slot{"price": "less than 500"}
    - utter_ask_budget
    - ActionSearchRestaurants
    - slot{"location": "Mumbai"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "300 to 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email
    - slot{"emailid": "arjunsingh89baghel@gmail.com"}
    - send_email
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

	
#######################

## Generated Story -6662270146725728901
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - ActionSearchRestaurants
    - slot{"location": "Mumbai"}
    - slot{"cuisine": "Chinese"}
    - slot{"price": "more than 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email
    - slot{"emailid": "arjunsingh89baghel@gmail.com"}
    - send_email
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
	
## Generated Story -6662270146725728901
* greet
    - utter_greet
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_location
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - ActionSearchRestaurants
    - slot{"location": "Mumbai"}
    - slot{"cuisine": "Chinese"}
    - slot{"price": "more than 700"}
    - utter_ask_sendmail
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## Generated Story 4702155743682014719
* greet
    - utter_greet
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - ActionSearchRestaurants
    - slot{"location": "Mumbai"}
    - slot{"cuisine": "Mexican"}
    - slot{"price": "more than 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email
    - slot{"emailid": "arjunsingh89baghel@gmail.com"}
    - send_email
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart


## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - validate_location
    - slot{"loc_avl": "1"}
* restaurant_search{"cuisine": "indian"}
    - slot{"cuisine": "indian"}
* restaurant_search
    - utter_ask_budget
* restaurant_search
    - ActionSearchRestaurants
    - ActionSearchRestaurants
* restaurant_search{"location": "Between Rs.300"}
    - slot{"location": "Between Rs.300"}

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian", "location": "Delhi", "price": "Rs.700"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "Delhi"}
    - slot{"price": "Rs.700"}
    - validate_location
    - ActionSearchRestaurants
    - utter_ask_sendmail
* email
    - utter_goodbye
    - action_slot_reset

## interactive_story_2
* restaurant_search{"cuisine": "Indian"}
    - slot{"cuisine": "Indian"}
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - validate_location
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_budget
* restaurant_search{"price": "700"}
    - slot{"price": "700"}
    - ActionSearchRestaurants
* email
    - utter_do_not_operate

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_budget
* restaurant_search{"price": "700"}
    - slot{"price": "700"}
    - ActionSearchRestaurants
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "arjunsingh89baghel@gmail.com"}
    - slot{"emailid": "arjunsingh89baghel@gmail.com"}
    - send_email
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
* greet

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian", "location": "pune"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "pune"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "700"}
    - slot{"price": "700"}
    - ActionSearchRestaurants
    - utter_ask_sendmail
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_default

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_budget
* restaurant_search{"price": "Rs.700"}
    - slot{"price": "Rs.700"}
    - ActionSearchRestaurants

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_budget
* restaurant_search{"price": "700"}
    - slot{"price": "700"}
    - ActionSearchRestaurants

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Delhi"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "700"}
    - slot{"price": "700"}
    - ActionSearchRestaurants
    - slot{"location": "Delhi"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "arjunsingh89baghel@gmail.com"}
    - slot{"emailid": "arjunsingh89baghel@gmail.com"}
    - send_email

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "jaipur"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "jaipur"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Rs.700"}
    - slot{"price": "Rs.700"}
    - ActionSearchRestaurants
    - slot{"location": "jaipur"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "arjunsingh89baghel@gmail.com"}
    - slot{"emailid": "arjunsingh89baghel@gmail.com"}
    - send_email
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
* goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "bijapur"}
    - slot{"location": "bijapur"}
    - validate_location
    - slot{"loc_avl": "0"}
    - utter_do_not_operate
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
* greet
    - utter_greet
* restaurant_search{"location": "kochi"}
    - slot{"location": "kochi"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_budget
* restaurant_search{"price": "Rs.700"}
    - slot{"price": "Rs.700"}
    - ActionSearchRestaurants
    - slot{"location": "kochi"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "arjunsingh89baghel@gmail.com"}
    - slot{"emailid": "arjunsingh89baghel@gmail.com"}
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
* restaurant_search{"cuisine": "south indian", "location": "udaipur"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "udaipur"}
    - utter_ask_budget
* restaurant_search{"price": "Rs.300"}
    - slot{"price": "Rs.300"}
    - validate_location
    - slot{"loc_avl": "0"}
    - utter_do_not_operate
    - utter_ask_location
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}

## interactive_story_2
* greet
    - utter_greet
* restaurant_search{"cuisine": "south indian", "location": "Delhi"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "Delhi"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "700"}
    - slot{"price": "700"}
    - ActionSearchRestaurants
    - slot{"location": "Delhi"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "arjunsingh89baghel@gmail.com"}
    - slot{"emailid": "arjunsingh89baghel@gmail.com"}
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
* greet
* restaurant_search

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_location
* restaurant_search{"location": "kota"}
    - slot{"location": "kota"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "700"}
    - slot{"price": "700"}
    - ActionSearchRestaurants
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "arjunsingh89baghel@gmail.com"}
    - slot{"emailid": "arjunsingh89baghel@gmail.com"}
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Delhi"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "700"}
    - slot{"price": "700"}
    - ActionSearchRestaurants
    - slot{"location": "Delhi"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "arjunsingh89baghel@gmail.com"}
    - slot{"emailid": "arjunsingh89baghel@gmail.com"}
    - send_email
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_location
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Rs.700"}
    - slot{"price": "Rs.700"}
    - ActionSearchRestaurants
    - slot{"location": "Delhi"}
    - utter_ask_sendmail
* email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart


* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Delhi", "price": "Rs.700"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Delhi"}
    - slot{"price": "Rs.700"}
    - validate_location
    - slot{"loc_avl": "1"}
    - ActionSearchRestaurants
    - slot{"location": "Delhi"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "arjunsingh89baghel@gmail.com"}
    - slot{"emailid": "arjunsingh89baghel@gmail.com"}
    - send_email
    - reset_slots
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_1
* restaurant_search{"cuisine": "chinese", "location": "Delhi", "price": "Rs.700"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Delhi"}
    - slot{"price": "Rs.700"}
    - validate_location
    - slot{"loc_avl": "1"}
    - ActionSearchRestaurants
    - slot{"location": "Delhi"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "arjunsingh89baghel@gmail.com"}
    - slot{"emailid": "arjunsingh89baghel@gmail.com"}
    - send_email
    - reset_slots
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
