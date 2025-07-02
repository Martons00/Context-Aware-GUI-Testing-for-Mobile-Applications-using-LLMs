### utils_llama.py in Droidbot repository
# Branch LLama_Integration
# This code is part of the Droidbot project, which integrates Llama 3.1
#https://github.com/Martons00/droidbot/tree/LLama_Integration

def ask_llama(self,view, maxl=200, temp=0.7, full_view_representation=None):
    rappresentation = ""
    for line in full_view_representation.split('\n'):
        type = line.split('<')[1].split(' ')[0]
        line = line.split('>')[1].split('<')[0]
        if len(line) > 0:
            rappresentation += f"<{type}>" + line + "</" + type + ">\n"
    full_view_representation = rappresentation
    # Generate a brief description of the current element based on available attributes
    view_text = self.__safe_dict_get(view, 'text', default='').strip()
    content_description = self.__safe_dict_get(view, 'content_description', default='').strip()
    view_class = self.__safe_dict_get(view, 'class', default='').split('.')[-1]

    # Build a readable summary for the current view
    view_details = (
        f"Current Element:\n"
        f"  - Class: {view_class}\n"
        f"  - Text: {view_text if view_text else 'N/A'}\n"
        f"  - Description: {content_description if content_description else 'N/A'}\n"
    )

    # Construct a structured prompt that incorporates both the global UI representation 
    # and the details of the active view
    prompt = (
            f"<s>[INST] <<SYS>>"
            "You are an assistant that generates only a realistic, context-appropriate text input for a UI element. "
            "Respond with a single word of plain text, no explanations, no formatting, no extra symbols."
            "<</SYS>>\n\n"
            "### Few-Shot Examples:\n\n"
            "Example 1:\n"
            "[UI Representation]\n"
            "<input id=0 text='Email address' bound_box=10,50,310,100>Enter email</input>\n"
            "Output:\n"
            "john.doe@example.com\n\n"
            "Example 2:\n"
            "[UI Representation]\n"
            "<input id=1 text='Search bar' bound_box=20,100,300,150>Search products...</input>\n"
            "<button id=2 text='Search' bound_box=320,100,620,150></button>\n"
            "Output:\n"
            "wireless headphones\n\n"
            "UI Snapshot:\n"
            f"{full_view_representation}\n\n"
            "Focused Element Details:\n"
            f"{view_details}\n\n"
            "Now, based on the UI Snapshot and Focused Element Details, provide only the appropriate text for the focused element."
            "[/INST]\n"
            "OUTPUT: "
        )

    
    print("Prompt sent to Llama:")
    print(prompt)
    
    response = ask_llama_local(prompt=prompt, temp=temp)
    response = response.split('OUTPUT:')[1].strip().replace('\n', ' ')
    if len(response) > 15:
        response = response[:15]
    if response:
        print("Response received:")
        print(response)
        print("Response text:")
        print(response.strip())
    else:
        print("Error: No response received from Llama.")
        return None
    # Decode and return the response
    return response.strip()

def ask_choice_llama(self,view, maxl=200, temp=0.7, full_view_representation=None,possible_actions=None):
    rappresentation = ""
    for line in full_view_representation.split('\n'):
        if '<' in line and '>' in line:
            try:
                type = line.split('<')[1].split(' ')[0]
                content = line.split('>')[1].split('<')[0]
                if len(content) > 0:
                    rappresentation += f"<{type}>{content}</{type}>\n"
            except Exception as e:
                print(f"WARNING: errore nel parsing della riga: {line} -- {e}")
        else:
            # se vuoi ignorare le righe senza tag, lascia pure vuoto
            continue

    full_view_representation = rappresentation
    # Generate a brief description of the current element based on available attributes
    view_text = self.__safe_dict_get(view, 'text', default='').strip()
    content_description = self.__safe_dict_get(view, 'content_description', default='').strip()
    view_class = self.__safe_dict_get(view, 'class', default='').split('.')[-1]

    # Build a readable summary for the current view
    view_details = (
        f"Current Element:\n"
        f"  - Class: {view_class}\n"
        f"  - Text: {view_text if view_text else 'N/A'}\n"
        f"  - Description: {content_description if content_description else 'N/A'}\n"
    )
    
    # If no possible actions are provided, return None
    # Se non ci sono azioni possibili, restituisci None
    view_possible_actions = None
    if possible_actions:
        view_possible_actions = ""
        for idx, action in enumerate(possible_actions):
            if isinstance(action, dict):
                event_type = action.get('event_type', 'N/A')
                view = action.get('view', {})
            else:
                event_type = getattr(action, 'event_type', 'N/A')
                view = getattr(action, 'view', {})
            content_desc = view.get('content_description', 'N/A')
            resource_id = view.get('resource_id', 'N/A')
            class_name = view.get('class', 'N/A')
            bounds = view.get('bounds', 'N/A')
            view_possible_actions += f"{idx}: event_type={event_type}, desc='{content_desc}', resource_id={resource_id}, class={class_name}, bounds={bounds}\n"

    # Ora puoi stampare la stringa sintetica se vuoi
    print(view_possible_actions)
    if possible_actions:
        view_history_actions = ""
        for idx, action in enumerate(last_actions):
            if isinstance(action, dict):
                event_type = action.get('event_type', 'N/A')
                view = action.get('view', {})
            else:
                event_type = getattr(action, 'event_type', 'N/A')
                view = getattr(action, 'view', {})
            content_desc = view.get('content_description', 'N/A')
            resource_id = view.get('resource_id', 'N/A')
            class_name = view.get('class', 'N/A')
            bounds = view.get('bounds', 'N/A')
            view_history_actions += f"{idx}: event_type={event_type}, desc='{content_desc}', resource_id={resource_id}, class={class_name}, bounds={bounds}\n"



    # Construct a structured prompt that incorporates both the global UI representation
    # and the details of the active view
    prompt = (
            f"<s>[INST] <<SYS>>"
            "You are an assistant that generates only a realistic, context-appropriate text input for a UI element. "
            "Respond with a single action to take, no explanations, no formatting, no extra symbols."
            "<</SYS>>\n\n"
            "### Few-Shot Examples:\n\n"
            "Example 1:\n"
            "[UI Representation]\n"
            "<input id=0 text='Email address' bound_box=10,50,310,100>Enter email</input>\n"
            "Possible Actions:\n"
            "0: event_type=touch, desc='Show Calendar List and Settings drawer', resource_id=None, class=android.widget.ImageButton, bounds=[[11, 147], [165, 301]]"
            "1: event_type=touch, desc='July', resource_id=com.google.android.calendar:id/date_picker_button, class=android.widget.LinearLayout, bounds=[[166, 147], [650, 301]]"
            "2: event_type=touch, desc='Search', resource_id=com.google.android.calendar:id/action_search, class=android.widget.Button, bounds=[[661, 158], [793, 290]]"
            "3: event_type=touch, desc='Jump to Today', resource_id=com.google.android.calendar:id/action_today, class=android.widget.Button, bounds=[[793, 158], [925, 290]]"                
            "Output:\n"
            "1"
            
            "UI Snapshot:\n"
            f"{full_view_representation}\n\n"
            "Focused Element Details:\n"
            f"{view_details}\n\n"
            "Possible Actions:\n"
            f"{view_possible_actions}\n"
            "History of Actions:\n"
            f"{view_history_actions}\n"
            "Now, based on the UI Snapshot, Focused Element Details, possible actions and History of Actions, provide only the appropriate index action."
            "[/INST]\n"
            "OUTPUT: "
        )

    
    print("Prompt sent to Llama:")
    print(prompt)
    response = ask_llama_local(prompt=prompt, temp=temp)

    # Estrai solo la parte dopo 'OUTPUT:'
    try:
        response = response.split('OUTPUT:')[1].strip()
    except IndexError:
        print("Error: 'OUTPUT:' not found in Llama response.")
        return None

    # Rimuovi newline e spazi ridondanti
    response = response.replace('\n', ' ').strip()

    # Prendi solo i primi 2 caratteri se la risposta è troppo lunga
    if len(response) > 15:
        response = response[:2].strip()

    if response:
        print("Response received:")
        print(response)
    else:
        print("Error: No response received from Llama.")
        return None

    # Prova a estrarre un intero dalla risposta (es. "1.", " 2 ", "3\n" -> 1, 2, 3)
    import re
    match = re.search(r'\d+', response)
    if match:
        idx = int(match.group())
        if 0 <= idx < len(possible_actions):
            last_actions.append(possible_actions[idx])
            if len(last_actions) > 10:
                last_actions.pop(0)
            return idx
        else:
            print(f"Error: Response index {idx} out of range for possible actions.")
            return None
    else:
        print(f"Error: Response '{response}' is not a valid index.")
        return None


def ask_llama_API(self,view, maxl=200, temp=0.7, full_view_representation=None):

    # Generate a brief description of the current element based on available attributes
    view_text = self.__safe_dict_get(view, 'text', default='').strip()
    content_description = self.__safe_dict_get(view, 'content_description', default='').strip()
    view_class = self.__safe_dict_get(view, 'class', default='').split('.')[-1]
    allowed_actions = view.get('allowed_actions', [])

    # Build a readable summary for the current view
    view_details = (
        f"Current Element:\n"
        f"  - Class: {view_class}\n"
        f"  - Text: {view_text if view_text else 'N/A'}\n"
        f"  - Description: {content_description if content_description else 'N/A'}\n"
        f"  - Allowed Actions: {', '.join(allowed_actions) if allowed_actions else 'N/A'}\n"
    )

    # Construct a structured prompt that incorporates both the global UI representation 
    # and the details of the active view
    prompt = (
        f"""<s>[INST] <<SYS>>
    You are a helpful assistant designed to generate context-aware text inputs for UI elements. 
    Analyze the interface structure, element properties, and existing content to suggest realistic values.
    <</SYS>>

    ### Task Description:
    1. Given the current UI state and a focus element (marked as editable):
    2. Suggest a text input that matches the element's context.
    3. The output MUST be few words, without any additional explanations or formatting or simbols.
    4. The output MUST be a single line of text.
    5. The output MUST be different from previus texts.
    5. Follow these guidelines:
    - Use actual data formats (emails, names, numbers) when detectable
    - Mirror the style of existing content when applicable
    - Prioritize content descriptions over placeholder texts
    - Keep inputs minimal but meaningful

    ### Few-Shot Examples:

    Example 1:
    [UI Representation]
    <input id=0 text='Email address' bound_box=10,50,310,100>Enter email</input>

    Output:
    john.doe@example.com

    Example 2: 
    [UI Representation]
    <input id=1 text='Search bar' bound_box=20,100,300,150>Search products...</input>
    <button id=2 text='Search' bound_box=320,100,620,150></button>

    Output:
    wireless headphones

    ### Current Interface:
    {full_view_representation}

    ### Focus Element Details:
    {view_details}

    ### Instruction:
    Based on the above context, suggest appropriate text for the focus element. 
    Provide only the raw text input without explanations, simbols or formatting, JUST TEXT. [/INST]
    
    OUTPUT:
    """
    )
    
    print("Prompt sent to Llama:")
    print(prompt)

    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": "Bearer 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",
            "Content-Type": "application/json",
        },
        data=json.dumps({
            "model": "meta-llama/llama-3.1-8b-instruct:free",
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
        })
    )

    if response.ok:
        print("Response received:")
        print(response.json())  # Print the JSON response
        print("Response text:")
        print(response.json().get('choices')[0].get('message').get('content').strip())
        
    else:
        print(f"Error: {response.status_code}")
        print(response.text)

    # Decode and return the response
    return response.json().get('choices')[0].get('message').get('content').strip()


import requests
import json

response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": "Bearer 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",
        "Content-Type": "application/json",
    },
    data=json.dumps({
        "model": "meta-llama/llama-3.1-8b-instruct:free",
        "messages": [
            {
                "role": "user",
                "content": "What is the meaning of life?"
            }
        ],
    })
)

if response.ok:
    print("Response received:")
    print(response.json())  # Print the JSON response
else:
    print(f"Error: {response.status_code}")
    print(response.text)

