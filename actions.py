# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/



from typing import Dict, Text, Any, List, Union, Optional

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction



class ActionFormInterested(FormAction):
    def name(self) -> Text:
        """Unique identifier of the form"""

        return "ent_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["interested"]


    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
               
            "interested": [
                self.from_entity(entity="interested"),
                self.from_intent(intent="affirm", value=True),
                self.from_intent(intent="deny", value=False),
            ],         
            
        }  

    def interested_answer(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate if intrested or not."""

        if value == False:
            dispatcher.utter_message(text="ok good bye")
            return {"interested": value}

        elif value == True:
            dispatcher.utter_message(template="utter_iqama")
            # validation failed, set slot to None
            return {"interested": value}
        else:
            dispatcher.utter_message(text="kindly answer if you are intrested or not ")
            return {"interested":None}
    

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
        interested= tracker.get_slot('interested')   
        
        if interested == True:
            dispatcher.utter_message(template="utter_iqama")
           
        elif interested== False:
            dispatcher.utter_message(template="utter_goodbye")
            # return [SlotSet("interested", None)]
        else:
            dispatcher.utter_message(template="utter_intrestedAnswer")    
            #return [SlotSet("services", None)]
        # dispatcher.utter_message(text="done")
        return []

class ActionFormIqama(FormAction):
    def name(self) -> Text:
        """Unique identifier of the form"""

        return "ent_form_iqama"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["interested","iqama"]


    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "iqama": [
                self.from_entity(entity="iqama"),
                self.from_intent(intent="affirm", value=True),
                self.from_intent(intent="deny", value=False),
            ],    
                     
            
        }  

    
    def iqama_answer(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate if intrested or not."""

        if value == False:
            # dispatcher.utter_message(text="ok good bye")
            return {"interested": value}

        elif value == True:
            # dispatcher.utter_message(template="utter_iqama")
            # validation failed, set slot to None
            return {"interested": value}
        else:
            dispatcher.utter_message(text="kindly answer if you have iqama or not ")
            return {"interested":None}

    

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
        iqama= tracker.get_slot('iqama')   
        
        if iqama == True:
            dispatcher.utter_message(template="utter_eduLevel")
        if iqama == False:
            dispatcher.utter_message(template="utter_eduLevel")    
        elif iqama == None:
            dispatcher.utter_message(template="utter_iqamaAnswer")    
            #return [SlotSet("services", None)]
        # dispatcher.utter_message(text="done")
        
        return []


class ActionFormEduLeve(FormAction):
    def name(self) -> Text:
        """Unique identifier of the form"""

        return "ent_form_levelEducation"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["interested","iqama","edulevel"]


    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "edulevel":[self.from_entity(entity="edulevel"), self.from_text()] ,
                     
        
        }  

    
    def edulevel_answer(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate if intrested or not."""
        
        if value == None:
            dispatcher.utter_message(template="utter_employed_reask")
            return {"edulevel": None}

        else:
            dispatcher.utter_message(template="utter_employed")
            return {"edulevel":value}

    

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
        edulevel= tracker.get_slot('edulevel')   
        
        
        if edulevel==None:
            dispatcher.utter_message(template="utter_edulevel_reask")
           
        else:
            dispatcher.utter_message(template="utter_employed")
            # return [SlotSet("interested", None)]
        
        
        return []        

class ActionFormEmployed(FormAction):
    def name(self) -> Text:
        """Unique identifier of the form"""

        return "ent_form_employed"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["employed"]


    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "employed": [
                self.from_entity(entity="employed"),
                self.from_intent(intent="affirm", value=True),
                self.from_intent(intent="deny", value=False),
            ],    
                     
            
        }  

    
    def emplyed_answer(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate if intrested or not."""

        if value == False:
            # dispatcher.utter_message(text="ok good bye")
            return {"employed": value}

        elif value == True:
            # dispatcher.utter_message(template="utter_iqama")
            # validation failed, set slot to None
            return {"employed": value}
        else:
            dispatcher.utter_message(template="utter_employed_reask")
            return {"employed":None}

    

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
        employed= tracker.get_slot('employed')   
        
        if employed == True:
            dispatcher.utter_message(template="utter_position")
        if employed == False:
            dispatcher.utter_message(template="utter_position")    
        elif employed == None:
            dispatcher.utter_message(template="utter_employed_reask")    
            #return [SlotSet("services", None)]
        # dispatcher.utter_message(text="done")
        
        return []

class ActionFormposition(FormAction):
    def name(self) -> Text:
        """Unique identifier of the form"""

        return "ent_form_position"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["position"]


    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "position":[self.from_entity(entity="position"), self.from_text()] ,
                     
        
        }  

    
    def position_answer(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
      

        if value == None:
            dispatcher.utter_message(template="utter_position_reask")
            return {"position": None}

        else:
            dispatcher.utter_message(template="utter_employed")
            return {"position":value}

    

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
        position= tracker.get_slot('position')   
        
        if position==None:
            dispatcher.utter_message(template="utter_position_reask")
           
        else:
            dispatcher.utter_message(template="utter_experience")
            # return [SlotSet("interested", None)]
        
        
        return []          

class ActionFormExperience(FormAction):
    def name(self) -> Text:
        """Unique identifier of the form"""

        return "ent_form_experience"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["experience"]


    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "experience":[self.from_entity(entity="experience"), self.from_text()] ,
                     
        
        }  

    
    def experience_answer(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
      

        if value == None:
            dispatcher.utter_message(template="utter_experience_reask")
            return {"experience": None}

        else:
            dispatcher.utter_message(template="utter_certifications")
            return {"experience":value}

    

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
        experience= tracker.get_slot('experience')   
        
        if experience==None:
            dispatcher.utter_message(template="utter_experience_reask")
           
        else:
            dispatcher.utter_message(template="utter_certifications")
            # return [SlotSet("interested", None)]
        
        
        return []         

class ActionFormExperience(FormAction):
    def name(self) -> Text:
        """Unique identifier of the form"""

        return "ent_form_certifications"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["certifications"]


    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "certifications":[self.from_entity(entity="certifications"), self.from_text()] ,
                     
        
        }  

    
    def certifications_answer(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
      

        if value == None:
            dispatcher.utter_message(template="utter_certifications_reask")
            return {"certifications": None}

        else:
            dispatcher.utter_message(template="utter_englishRate")
            return {"certifications":value}

    

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
        certifications= tracker.get_slot('certifications')   
        
        if certifications==None:
            dispatcher.utter_message(template="utter_certifications_reask")
           
        else:
            dispatcher.utter_message(template="utter_englishRate")
            # return [SlotSet("interested", None)]
        
        
        return []            


class ActionFormEnglishRate(FormAction):
    def name(self) -> Text:
        """Unique identifier of the form"""

        return "ent_form_englishrate"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["englishRate"]


    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "englishRate":[self.from_entity(entity="englishRate"), self.from_text()] ,
                     
        
        }  

    
    def englishRate_answer(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
      

        if value == None:
            dispatcher.utter_message(template="utter_englishRate_reask")
            return {"englishRate": None}

        else:
            dispatcher.utter_message(template="utter_available")
            return {"englishRate":value}

    

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
        englishRate= tracker.get_slot('englishRate')   
        
        if englishRate==None:
            dispatcher.utter_message(template="utter_englishRate_reask")
           
        else:
            dispatcher.utter_message(template="utter_available")
            # return [SlotSet("interested", None)]
        
        
        return []            


class ActionFormEnglishRate(FormAction):
    def name(self) -> Text:
        """Unique identifier of the form"""

        return "ent_form_available"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["available"]


    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "available":[self.from_entity(entity="available"), self.from_text()] ,
                     
        
        }  

    
    def available_answer(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
      

        if value == None:
            dispatcher.utter_message(template="utter_available_reask")
            return {"available": None}

        else:
            dispatcher.utter_message(template="utter_endcall")
            return {"available":value}

    

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
        available= tracker.get_slot('available')   
        
        if available==None:
            dispatcher.utter_message(template="utter_englishRate_reask")
           
        else:
            dispatcher.utter_message(template="utter_endcall")
            # return [SlotSet("interested", None)]
        
        
        return []         