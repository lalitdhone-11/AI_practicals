def chatbot():
  print("Welcome to chatbot support")
  print("plz type 'bye'to exit.\n")
  while True:
      user=input("You:").lower()
      if user=="bye":
          print("Chatbot:Thank you have a nice day!!!")
          break
      elif "hello" in user or "hi" in user:
          print("Chatbot:Welcome to chatbot support ,how can i help you?")
      elif "price" in user or "cost" in user:
          print("Chatbot:Our products start from Rs.899")
      elif "order" in user:
          print("Chatbot: you can place order on website")
      elif "refund" in user:
          print("Chatbot:refund is process within 7 days")
      elif "contact" in user:
          print("ChatBot:you can contact us on abc11@gmail.com")
      else:
          print("Chatbot:Sorry,I didn't understand,can you rephrase?") 
chatbot()
