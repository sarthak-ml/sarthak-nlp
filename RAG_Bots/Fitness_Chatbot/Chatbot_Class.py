class Chatstate():

    __st_user_token__ = "<user_start>\n"
    __end_user_token__ = "<user_ends>\n"
    __st_bot_token__ = "<bot_start>\n"
    __end_bot_token__ = "<bot_ends>\n"


    def __init__(self,model,system=""):
        self.model = model
        self.system = system
        self.history = ["""<system prompt>You are ai designed to help people on their fitness journey your task includes, answering questions
            related to fitness only , You work on the principle of think and reply. Always think if the answer or prompt given by the user even makes sense,
                        if not let the user know the same but in a quirky and funny way
                        
            Important: Questions regarding anything else should be answered with 
            "I am designed to answer questions about your medical journey, let's hop on to that" and other variations of the same sentence

            Your sequence of perfoming task is:
            First you ask name, age, food preference and allergies and always make sure to use this information before answering user next question
            
            Important:
            1. Ask first if the user wants food advice or workout plan
            2. While answering user question about receipe you always provide quantity of the ingredients , number of people it will serve, and calories of each ingreedients
            3. If its workout plan , ask if the user has any injury before suggestion, ask for duration he is willing to give, if it is less than 10 minutes , let him know its too less to curate a plan, 
                while suggesting suggest exercise reps and rounds and calories it will burn.             
            
        </system prompt>"""]

    def add_history_of_user(self,message):
        self.history.append(self.__st_user_token__ + message +self. __end_user_token__)

    def add_history_of_bot(self,message):
        self.history.append(self.__st_bot_token__ + message +self. __end_bot_token__)

    def get_chat_history(self):
        return """ """.join([*self.history])
    
    def get_prompt(self):
        prompt = self.get_chat_history() + self.__st_bot_token__
        if len(self.system)>0:
            return self.system+'\n' + prompt
        else:
            return prompt
        
    def output(self,message):
        self.add_history_of_user(message)
        prompt = self.get_prompt()
        response = self.model.invoke(input = prompt)
        result = response.replace(prompt,"")
        self.add_history_of_bot(result)
        return result





    
