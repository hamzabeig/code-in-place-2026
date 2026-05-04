from ai import call_gpt

def main():
    name= input("Enter you name: ")
    topic = input("Enter a topic: ")
    
    response = call_gpt(f"""A haiku is a type of very ,
                        short poem.It has three lines. 
                        The first line has 5 syllables, 
                        the second has 7 syllables, 
                        and the third has 5 syllables again. 
                        Haiku usually describe a moment in nature
                        or a feeling, using clear, simple images. 
                        Even though it is brief, a good haiku often
                        gives the reader a quiet, thoughtful feeling.
                        write a haiku and use {name} as actor with
                        theme as {topic}
                        """) 
    
    print (response)

if __name__ == "__main__":
    main()
