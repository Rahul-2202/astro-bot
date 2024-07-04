from google.cloud import aiplatform
aiplatform.init(project='swoop-prod-fc', location='us-central1')



API_ENDPOINT="us-central1-aiplatform.googleapis.com"
PROJECT_ID="swoop-fc-prod"
LOCATION_ID="us-central1"
MODEL_ID="gemini-1.0-pro-002"



# Error message: "Permission 'aiplatform.endpoints.predict' denied on resource '//aiplatform.googleapis.com/projects/swoop-fc-prod/locations/us-central1/publishers/google/models/gemini-1.5-flash-001' (or it may not exist)."

# Status: 403 Error code: 7 Reason: IAM_PERMISSION_DENIED

# Request ID: 17412677994429160377