import openai
import os
import json
import requests

#defining the api key
openai.api_key = os.environ.get("OPENAI_API_KEY")


# we will build a gpt function that gets crypto prices from an api and ten we will use the informaiton to build a crypto chatbot


#making the function
coin_checker = [  
    {
        "name": "get_coin_price",
        "description": "Get the price of a coin",
        "parameters": {
            "type": "object",
            "properties": {
                "coin_name": {
                    "type": "string",
                    "description": "the name of the coin to get the price or summery , name shoud be correctly formated : BTCUST , ETHUSDT , we use binance api",
                }
            },

        },
    },
]


#making the messages
messages = [ {"role" : "system", "content" : "you are a helpfull assitant "}]



#making the api call
def get_coin_price(args):

    coin = args["coin_name"]
    url = "https://binance43.p.rapidapi.com/ticker/24hr"
    querystring = {"symbol":f"{coin}"}

    headers = {
	"X-RapidAPI-Key": "YOUR_API_KEY",
	"X-RapidAPI-Host": "binance43.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers,params=querystring)
    #checking if the response is 200
    if response.status_code == 200:
        #returning the result
        return f"here are the results i got :\n\n {response.json()} \n\n if you want to know more about this coin please visit : https://www.binance.com/en/trade/{coin}"


#making the chatbot
while True:
    prompt = input("You: ")
    if prompt == "quit":
        break
    messages.append({"role": "user", "content": prompt})
    response = openai.ChatCompletion.create(
        #the model name shoud be the same as the one here or the gpt4 version
        model="gpt-3.5-turbo-0613",
        messages=messages,
        #adding the function
        functions=coin_checker,
        #setting the function call to auto
        function_call = "auto",
    )
    #checking if the response is a function call
    if response['choices'][0]["finish_reason"] == "function_call":
        function_name_to_use = response['choices'][0]['message']['function_call']['name']
        #checking if the function is the one we want
        if function_name_to_use == "get_coin_price":
            #getting the arguments
            args = json.loads(response['choices'][0]['message']['function_call']['arguments'])
            if args:
                print(args["coin_name"])
                #calling the function
                result_api = get_coin_price(args)
                #adding the result to the messages
                messages.append({"role": "function","name":"get_coin_price" ,"content": result_api})  
                #calling the chatbot again
                function_response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo-0613",
                    messages=messages,

                )
                #getting the callback
                callback = function_response['choices'][0]['message']['content']
                messages.append({"role": "assistant", "content": callback})          
                print("Bot: " + callback)   

    #if the response is not a function call we just get the callback     
    else:            
     callback = response['choices'][0]['message']['content']
     messages.append({"role": "assistant", "content": callback})
     print("Bot: " + callback)



#drop your ideas and lets build something cool