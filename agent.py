from google.genai import types

from llm import client, MODEL

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


# --------------------------------------------------
# TOOL REGISTRY
# --------------------------------------------------

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


# --------------------------------------------------
# TOOL DECLARATIONS
# --------------------------------------------------

tool_declarations = [
    {
        "name": "calculate",
        "description": "Add two numbers together.",
        "parameters": {
            "type": "object",
            "properties": {
                "a": {"type": "integer"},
                "b": {"type": "integer"},
            },
            "required": ["a", "b"],
        },
    },
    {
        "name": "multiply",
        "description": "Multiply two numbers.",
        "parameters": {
            "type": "object",
            "properties": {
                "a": {"type": "integer"},
                "b": {"type": "integer"},
            },
            "required": ["a", "b"],
        },
    },
    {
        "name": "subtract",
        "description": "Subtract b from a.",
        "parameters": {
            "type": "object",
            "properties": {
                "a": {"type": "integer"},
                "b": {"type": "integer"},
            },
            "required": ["a", "b"],
        },
    },
    {
        "name": "divide",
        "description": "Divide a by b.",
        "parameters": {
            "type": "object",
            "properties": {
                "a": {"type": "number"},
                "b": {"type": "number"},
            },
            "required": ["a", "b"],
        },
    },
    {
        "name": "calculate_percentage",
        "description": "Calculate a percentage of a value.",
        "parameters": {
            "type": "object",
            "properties": {
                "value": {"type": "number"},
                "percentage": {"type": "number"},
            },
            "required": ["value", "percentage"],
        },
    },
    {
        "name": "get_current_datetime",
        "description": "Get the current date and time.",
        "parameters": {
            "type": "object",
            "properties": {},
        },
    },
    {
        "name": "convert_units",
        "description": "Convert between supported units.",
        "parameters": {
            "type": "object",
            "properties": {
                "value": {"type": "number"},
                "from_unit": {"type": "string"},
                "to_unit": {"type": "string"},
            },
            "required": ["value", "from_unit", "to_unit"],
        },
    },
    {
        "name": "get_weather",
        "description": "Get current weather for a city.",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {"type": "string"},
            },
            "required": ["city"],
        },
    },
    {
        "name": "web_search",
        "description": "Search the web for current information.",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {"type": "string"},
            },
            "required": ["query"],
        },
    },
]


gemini_tools = types.Tool(
    function_declarations=tool_declarations
)


# --------------------------------------------------
# SYSTEM INSTRUCTION
# --------------------------------------------------

SYSTEM_PROMPT = """
You are a helpful AI assistant.

Use tools when necessary.

For calculations, use calculator tools.

For weather questions, use the weather tool.

For current or web-based information, use web_search.

Do not invent tool results.

Always follow the user's requested format and length.

If the user asks for 2 lines, answer in exactly 2 lines.

Do not copy or repeat raw tool results.

Summarize tool results into a concise final answer.
"""


# --------------------------------------------------
# AGENT
# --------------------------------------------------

def run_agent(user_input, messages):

    # Add the new user message to application history
    messages.append({
        "role": "user",
        "content": user_input,
    })

    # Convert our simple chat history into Gemini format
    contents = []

    for message in messages:

        role = message["role"]
        content = message["content"]

        if not content:
            continue

        if role == "user":
            contents.append(
                types.Content(
                    role="user",
                    parts=[types.Part(text=content)],
                )
            )

        elif role == "assistant":
            contents.append(
                types.Content(
                    role="model",
                    parts=[types.Part(text=content)],
                )
            )

    max_iterations = 5

    for _ in range(max_iterations):

        response = client.models.generate_content(
            model=MODEL,
            contents=contents,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT,
                tools=[gemini_tools],
            ),
        )

        # Add Gemini's response to the conversation
        contents.append(response.candidates[0].content)

        # ------------------------------------------
        # No tool requested
        # ------------------------------------------

        if not response.function_calls:

            final_answer = response.text

            messages.append({
                "role": "assistant",
                "content": final_answer,
            })

            return final_answer

        # ------------------------------------------
        # Tool requested
        # ------------------------------------------

        for function_call in response.function_calls:

            function_name = function_call.name
            arguments = dict(function_call.args)

            print("\n" + "=" * 60)
            print("TOOL REQUESTED:", function_name)
            print("ARGUMENTS:", arguments)

            function_to_call = available_tools.get(function_name)

            # --------------------------------------
            # Tool does not exist
            # --------------------------------------

            if function_to_call is None:

                result = {
                    "error": f"Tool '{function_name}' was not found."
                }

            else:

                try:

                    result = function_to_call(**arguments)

                    print("TOOL RESULT:", result)

                except Exception as e:

                    result = {
                        "error": str(e)
                    }

                    print("TOOL ERROR:", e)

                  # --------------------------------------
            # Send tool result back to Gemini
            # --------------------------------------

            function_response = types.Part(
                function_response=types.FunctionResponse(
                    name=function_name,
                    response={"result": result},
                    id=function_call.id,
                )
            )

            contents.append(
                types.Content(
                    role="user",
                    parts=[function_response],
                )
            )

    return "I was unable to complete the request within the allowed tool-call limit."