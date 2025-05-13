from ai import call_gpt

def main():
    name = input("Enter your name: ")
    topic = input("Enter a topic: ")
    prompt = f"Write a thoughtful haiku for someone named {name}. The haiku should be inspired by the topic '{topic}' and follow the traditional 5-7-5 syllable format. Use vivid, simple imagery and evoke a quiet or reflective feeling."
    response = call_gpt(prompt) 
    print("Creating your haiku...")
    print("\n")
    print(response)
    pass


if __name__ == "__main__":
    main()