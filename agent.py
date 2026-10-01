
from ollama import chat

from tools import (
    calculate,
    multiply,
    subtract,
    divide,
    calculate_percentage,
    get_current_datetime,
    convert_units,
    get_weather,
    web_search,
)



# MODEL


MODEL = "qwen2.5"



# TOOL REGISTRY


available_tools = {
    "calculate": calculate,
    "multiply": multiply,
    "subtract": subtract,
    "divide": divide,
    "calculate_percentage": calculate_percentage,
    "get_current_datetime": get_current_datetime,
    "convert_units": convert_units,
    "get_weather": get_weather,
    "web_search": web_search,
}



# SYSTEM PROMPT


SYSTEM_PROMPT = (
    "You are a helpful AI assistant. "
    "Use tools when necessary. "
    "For calculations, use calculator tools. "
    "For weather questions, use the weather tool. "
    "For current or web-based information, use web_search. "
    "Do not invent tool results. "
    "Always follow the user's requested format and length. "
    "If the user asks for 2 lines, answer in exactly 2 lines. "
    "Do not copy or repeat raw tool results. "
    "Summarize tool results into a concise final answer."
)



# AGENT FUNCTION


def run_agent(user_input, messages):

    # Add user message to conversation history
   

    messages.append({
        "role": "user",
        "content": user_input,
    })


   
    # AGENT LOOP
   

    max_iterations = 5

    for iteration in range(max_iterations):

    
        # Ask the LLM
       

        response = chat(
            model=MODEL,
            messages=messages,
            tools=list(available_tools.values()),
        )


        
        # Save assistant response
  

        messages.append(response.message)


       
        # Check whether the model requested a tool
        

        if not response.message.tool_calls:

            final_answer = response.message.content

            return final_answer


        
        # Execute requested tools
      

        for tool_call in response.message.tool_calls:

            function_name = tool_call.function.name
            arguments = tool_call.function.arguments


          
            # Debug information in terminal
           

            print("\n" + "=" * 60)
            print("TOOL REQUESTED:", function_name)
            print("ARGUMENTS:", arguments)


          
            # Find the Python function
          

            function_to_call = available_tools.get(
                function_name
            )


           
            # Handle unknown tool
          

            if function_to_call is None:

                error_message = (
                    f"Tool '{function_name}' was not found."
                )

                print("ERROR:", error_message)

                messages.append({
                    "role": "tool",
                    "content": error_message,
                    "tool_name": function_name,
                })

                continue


           
            # Execute the tool safely
           

            try:

                result = function_to_call(
                    **arguments
                )

                print("TOOL RESULT:", result)

                messages.append({
                    "role": "tool",
                    "content": str(result),
                    "tool_name": function_name,
                })


            
            # Handle tool execution errors
            

            except Exception as e:

                error_message = (
                    f"Tool error: {str(e)}"
                )

                print("ERROR:", error_message)

                messages.append({
                    "role": "tool",
                    "content": error_message,
                    "tool_name": function_name,
                })


    
    # MAXIMUM ITERATIONS REACHED
  

    return (
        "I was unable to complete the request "
        "within the allowed tool-call limit."
    )