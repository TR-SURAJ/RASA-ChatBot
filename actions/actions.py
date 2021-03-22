# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from datetime import date
import pandas as pd
import sqlite3


class ActionShowHotelDetails(Action):

    def name(self) -> Text:
        return "show_hotel_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        conn = sqlite3.connect("hoteldata.sqlite")
        query = "SELECT name,address,rating,url FROM hoteldata where city=\"Bangalore\" and img!=\"\" and facility!=\"\" order by rating DESC LIMIT 5"
        df = pd.read_sql(query,conn)
        content = 'Below are the Options:\n\n\n'

        if df.shape[0]>0:
            values = list(df.values)
    


            for data in values:
                hotelName = data[0]
                address = data[1]
                rating = data[2]
                Link = data[3]
                content = content +"Hotel Name: "+hotelName+"\nAddress: "+address+"\nRating: "+rating+"\nBook Now: "+Link+"\n\n"
    
        else:
            content:"No Hotels Found"


        dispatcher.utter_message(text=content)

        return []




class ActionShowTicketDetails(Action):

    def name(self) -> Text:
        return "show_ticket_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
       

        dispatcher.utter_message(template="utter_ticket_details")

        return []



class ActionShowEventDetails(Action):

    def name(self) -> Text:
        return "show_event_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
       

        dispatcher.utter_message(template="utter_event_details")

        return []
