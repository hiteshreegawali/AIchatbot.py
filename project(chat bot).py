print("WELCOME! TO CHAT BOT")
print("You can ask me basic questions,type bye to end the chat")
responses = {
    "hello":"hii, how can I help you",
    "how are you" : "I am good, thankyou",
    "i am learning python and this is my second project":"That is great keep learning u are going to achieve your goals, focus on yourself",
    "My clg is getting really hectic":"I know right too much learning hrs and continuos class for 3 hr straight is really bad...Dont worry you will get used to it just dont skip classes for 1 sem atleast..",
    "i have applied for hackathon":"Thats really good,remember goal isnt wining its learning...try your best!!I know youll do great. ALL THE BEST",
    "motivate me":"Its just a bad phase... you are capable of every thing you are smart.. Never give up.. with every mistake you are getting better and better"
}

def getresponsebot(userquestions):
    userquestions= userquestions.lower()
    for eachkey in responses:
        if eachkey in userquestions:
            return responses[eachkey]
            
    return "I am not able to tell yet... I'll learn soon"
 
while True:
       userinput = input("please ask ur question")
       reply = getresponsebot(userinput)
       print("Bot response:",reply)
       if "bye" in userinput.lower():
        print("ok bye... feel free to text again")
       if "bye" in userinput.lower():
        break
        


