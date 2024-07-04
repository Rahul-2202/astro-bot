import os
import google.generativeai as genai
# from flask import Flask, request, jsonify

genai.configure(api_key="AIzaSyB1TrkVDp_xNrtT20v0rksuJUnqjESmWi4")

# Function to load Gemini Pro model and get responses
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def get_gemini_response(req):
  question = req.get_json().get("question")
  response = chat.send_message(question, stream=False)
  return {"response": response.text}

# # If you want to test the function locally
# if __name__ == "__main__":

#   app = Flask(__name__)

#   @app.route("/", methods=["POST"])
#   def handle_request():
#     return jsonify(get_gemini_response(request))

#   app.run()