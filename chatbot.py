print("👷 Welcome to Civil Engineering FAQ Chatbot!")
print("Type 'exit' to quit.\n")

faq = {
    "what is concrete": "Concrete is a mix of cement, sand, aggregates, and water used in construction.",
    "types of foundations": "Shallow and deep foundations like spread footing and pile foundation.",
    "what is a beam": "A beam is a horizontal structural element that resists lateral loads.",
    "types of soil": "Common types include clay, sand, silt, gravel, and loam.",
    "what is structural engineering": "It's the design and analysis of load-bearing structures.",
    "what is load": "Load refers to forces like dead load, live load, and wind load.",
}

while True:
    question = input("You: ").lower()
    if question == "exit":
        print("Bot: Goodbye! 👷‍♂️")
        break
    elif question in faq:
        print("Bot:", faq[question])
    else:
        print("Bot: I don't know that yet. Please try another question.")
