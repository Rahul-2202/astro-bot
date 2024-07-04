import requests
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Initialize Firebase Admin SDK
cred = credentials.Certificate("path/to/serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# Function to send message to LLM model
def send_message_to_llm(message):
  # Make HTTP request to LLM model
  response = requests.post("https://llm-model-url", json={"message": message})
  return response.json()

# Firebase Cloud Function to handle chat messages
def handle_chat_message(request):
  # Get message and user ID from request body
  message = request.get_json().get("message")
  user_id = request.get_json().get("user_id")

  # Store message in user's chat history
  chat_history_ref=db.collection("users").document(user_id).collection("chat_history")
  chat_doc_ref = chat_history_ref.document()
  chat_doc_ref.set({"message": message})

  # Get chat history for current user
  chat_history = [doc.to_dict()["message"] for doc in db.collection("users").document(user_id).collection("chat_history").stream()]

  # Pass chat history to LLM model
  llm_response = send_message_to_llm(chat_history)

  # Return LLM response
  return llm_response



# AIzaSyB1TrkVDp_xNrtT20v0rksuJUnqjESmWi4 genai