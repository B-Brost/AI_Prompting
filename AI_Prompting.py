import openai as OpenAI
def analyze_input_with_delimiters(client: OpenAI, user_input: str) -> str:
    """
    ChatCompletion(id='chatcmpl-9GGDzq2EgQfE6EgXcAQpP4olCdyPs', choices=[Choice(finish_reason='stop', index=0, logprobs=None, 
    message=ChatCompletionMessage(content='The sentiment of the above inputs is positive. The phrase "I am happy" 
    indicates a feeling of joy and contentment.', role='assistant', function_call=None, tool_calls=None))], created=1713662643,
    model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint='fp_c2295e73ad', usage=CompletionUsage(completion_tokens=25, prompt_tokens=45, total_tokens=70))
    """
    # Define the delimiters
    delimiters = ['***', '$$$', '%%%']
    # Initialize an empty string for the prompt
    prompt = ""
    # Loop through the delimiters and add the user input to the prompt with each delimiter
    for delimiter in delimiters:
        prompt += f"{delimiter}{user_input}{delimiter} "
    # Add the analysis task to the prompt
    prompt += "Analyze the sentiment of the above inputs."
    # Get the LLM response
    completion = client.chat.completions.create(
        model = 'gpt-3.5-turbo',
        messages = [
            {'role' : 'system', 'content' : 'You are a helpful assistant.'},
            {'role' : 'user', 'content' : prompt}
        ],
        temperature=0
    )
    return completion

def generate_story(client: OpenAI, title: str) -> str:
    """
    The Last Day of Summer
    On the last day of summer, the townspeople gathered around the lighthouse for a farewell celebration. They lit bonfires on the beach, sang songs of summers past, and shared stories of days gone by. As the stars twinkled overhead and the waves crashed against the shore, a sense of unity and nostalgia filled the air.
    As the clock struck midnight, signaling the official end of summer, a hush fell over the crowd. The lighthouse beacon shone brightly, casting its warm light over the town, a reminder that even in the darkest of times, there was always hope.
    And so, as the last day of summer came to a close, the residents of Seaview stood together, embracing the changing seasons and looking forward to the memories that the next summer would bring. The lighthouse stood as a silent guardian, a beacon of light and hope in the darkness, guiding the way to a new beginning.
    """
    # Define the prompt
    prompt = f"Write a short story based on the title: '{title}'."

    # Get the LLM response
    completion = client.chat.completions.create(
        model = 'gpt-3.5-turbo',
        messages = [
            {'role' : 'system', 'content' : 'You are a creative writer.'},
            {'role' : 'user', 'content' : prompt}
        ],
        temperature=0.6,
        max_tokens=500
    )
    return completion.choices[0].message.content

def generate_haiku(client: OpenAI, theme: str) -> str:
    """
    Blossoms gently sway,
    Nature's canvas comes alive,
    Spring's beauty in play.
    """
    # Define the prompt
    prompt = f"Compose a haiku about the theme: '{theme}'."

    # Get the LLM response
    completion = client.chat.completions.create(
        model = 'gpt-3.5-turbo',
        messages = [
            {'role' : 'system', 'content' : 'You are a poetic assistant.'},
            {'role' : 'user', 'content' : prompt}
        ],
        temperature=0.6,
        max_tokens=200
    )
    return completion.choices[0].message.content

def check_input_and_respond(client: OpenAI, user_input: str) -> str:
    """
    Yes, it is going to rain today.
    """
    # Define the prompt
    prompt = f"If the input is a question, answer it. If the input is a statement, confirm it. Input: '{user_input}'."

    # Get the LLM response
    completion = client.chat.completions.create(
        model = 'gpt-3.5-turbo',
        messages = [
            {'role' : 'system', 'content' : 'You are a helpful assistant.'},
            {'role' : 'user', 'content' : prompt}
        ],
        temperature=0.6,
        max_tokens=200
    )
    return completion.choices[0].message.content

def check_input_type(client: OpenAI, user_input: str) -> str:
    """
    The input '2+2' is a mathematical expression. Solving it, we get:

    2 + 2 = 4

Therefore, the result of the expression '2+2' is 4.
    """
    # Define the prompt
    prompt = f"If the input is a mathematical expression, solve it. If the input is a text string, summarize it. Input: '{user_input}'."

    # Get the LLM response
    completion = client.chat.completions.create(
        model = 'gpt-3.5-turbo',
        messages = [
            {'role' : 'system', 'content' : 'You are a helpful assistant.'},
            {'role' : 'user', 'content' : prompt}
        ],
        temperature=0.6,
        max_tokens=200
    )
    return completion.choices[0].message.content

def generate_color_description(client: OpenAI, color: str) -> str:
    """
    4.Green is the color of nature and represents growth, harmony, freshness, and fertility. It is also associated with balance, health, 
    renewal, and prosperity. Green is often seen as a calming and relaxing color that symbolizes peace and stability.
    """
    # Define the prompt
    prompt = f"""
    1. Color: "Red"
    Description: "Red is the color of fire and blood, so it is associated with energy, war, danger, strength, power, determination as well as passion, desire, and love."

    2. Color: "Blue"
    Description: "Blue is the color of the sky and sea. It is often associated with depth and stability. It symbolizes trust, loyalty, wisdom, confidence, intelligence, faith, truth, and heaven."

    3. Color: "{color}"
    Description:
    """

    # Generate the completion
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    # Extract the generated description from the response
    description = response.choices[0].message.content.strip()

    return description

def generate_flower_description(client: OpenAI, flower: str) -> str:
    """
    4. Flower: "Cosmo"
    Description: "A cosmo, with its delicate petals in a variety of vibrant colors, dances gracefully in the summer breeze, 
    spreading joy and energy wherever it goes. A symbol of happiness, spontaneity, and celebration."    
    """
    
    # Define the prompt
    prompt = f"""
    1. Flower: "Peony"
    Description: “A peony, in royal robes and sweet perfume, sways softly under the sun’s warm light, a symbol of love pure and bright.”

    2. Flower: "Lily"
    Description: "“A lily, in pristine white and subtle fragrance, stands tall under the moon’s gentle glow, a symbol of purity serene and elegant.”
    
    3. Flower: "Rose"
    Description: "A rose, in vibrant hues and intoxicating scent, blooms bravely amidst the thorns, a symbol of passion intense and enduring."
    
    4. FLower: "{flower}"
    Description:
    """

    # Generate the completion
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    # Extract the generated description from the response
    description = response.choices[0].message.content.strip()

    return description

def main():
    # Initialize the OpenAI client
    client = OpenAI

    # Set the OpenAI API key, or set API environment
    client.api_key = 'insert API Key'


    # Call the analyze_input_with_delimiters function
    user_input = "I am happy."
    print(analyze_input_with_delimiters(client, user_input))
    print("\n")
    # Call the generate_story function
    title = "The Last Day of Summer"
    print(generate_story(client, title))
    print("\n")
    # Call the generate_haiku function
    theme = "The Beauty of Spring"
    print(generate_haiku(client, theme))
    print("\n")
    # Call the check_input_and_respond function
    response = check_input_and_respond(client, "Is it going to rain today?")
    print(response)
    print("\n")
    # Call the check_input_type function
    response = check_input_type(client, "2+2")
    print(response)
    print("\n")
    # Call the generate_color_description function
    description = generate_color_description(client, "Green")
    print(description)
    print("\n")
    # Call the generate_flower_description function
    description = generate_flower_description(client, "Cosmo")
    print(description)

# Call the main function
if __name__ == "__main__":
    main()






