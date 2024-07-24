import random
import string
import firebase_admin
from firebase_admin import credentials, db, firestore
from firebase_functions import https_fn, database_fn
import google.generativeai as genai
# from firebase_admin import credentials, db

# Initialize Firebase Admin SDK
cred = credentials.Certificate("path/to/serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://sabic-d4934-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

# https://astrobot-ffa09-default-rtdb.firebaseio.com/

# Initialize Google Generative AI
genai.configure(api_key="AIzaSyB1TrkVDp_xNrtT20v0rksuJUnqjESmWi4")

# Load Gemini Pro model
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def generate_gemini_response(conversation_history, system_prompt):
    # Prepare system message
    system_message = {
        "role": "system",
        "content": f"{system_prompt}"
    }
    messages = [system_message]
    
    # Add user messages from conversation history
    for conversation in conversation_history:
        messages.append({
            "role": "user",
            "content": conversation,
        })

    # Generate response
    response = chat.send_message(messages[-1]['content'], stream=False)
    return response.text

# Cloud Function to handle HTTP requests
@https_fn.on_request()
def converse(req: https_fn.Request) -> https_fn.Response:
    if req.method != "POST":
        return https_fn.Response("Method not allowed", status=405)

    data = req.get_json()
    query = data.get("query")
    conversation_id = data.get("conversation_id")

    if not query:
        return https_fn.Response({"success": False}, status=400)

    if not conversation_id:
        conversation_id = ''.join(random.choices(string.ascii_letters + string.digits, k=16))

    ref = db.reference(f'conversations/{conversation_id}')
    conversation = ref.get()
    
    if not conversation:
        ref.set({"0": query})
        response_id = "1"
    else:
        query_id = str(len(conversation))
        response_id = str(len(conversation) + 1)
        ref.child(query_id).set(query)

    db.reference(f'requests/{conversation_id}/{response_id}').set({
        "query": query,
        "timestamp": firestore.SERVER_TIMESTAMP
    })

    return https_fn.Response({"success": True, "data": {"conversation_id": conversation_id, "response_id": response_id}})

@database_fn.on_create(ref="/requests/{conversation_id}/{response_id}")
def xRtdbTriggerNewChatCompletionRequest(event):
    snapshot = event.data
    context = event.context
    conversation_id = context.params['conversation_id']
    response_id = context.params['response_id']

    system_prompt="";

    ref = db.reference(f'conversations/{conversation_id}')
    conversation_history = list(ref.get().values())
    
    response_text = generate_gemini_response(conversation_history, system_prompt)
    
    db.reference(f'conversations/{conversation_id}/{response_id}').set(response_text)