import json
from google.cloud import firestore
from flask import jsonify, make_response

# Initialize Firestore client
db = firestore.Client()

def counter(request):
    # Set CORS headers for the preflight request
    if request.method == 'OPTIONS':
        # Allows GET and POST requests from any origin with the Content-Type header
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET,POST',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600'
        }
        return ('', 204, headers)
    
    # Reference to the visitor count document in Firestore
    doc_ref = db.collection('visits').document('visitor-count')
    headers = {'Access-Control-Allow-Origin': '*'}

    if request.method == 'GET':
        # Get the current visitor count
        doc = doc_ref.get()
        if doc.exists:
            count = doc.to_dict().get('count', 0)
        else:
            count = 0
        response = make_response(jsonify({"count": count}))
        response.headers = headers
        return response
    
    elif request.method == 'POST':
        # Increment the visitor count by 1
        doc_ref.update({"count": firestore.Increment(1)})
        response = make_response(jsonify({"message": "Visitor count updated"}))
        response.headers = headers
        return response
