from flask import Flask, jsonify, make_response
import flask
from spiffworkflow_backend.routes import process_models_controller
app = Flask(__name__)

#@app.route('/deployment/create', methods=["POST"])
def create_deployment(
    modified_process_model_identifier: str,
) -> flask.wrappers.Response:

    request_param = modified_process_model_identifier
      # Receiving data from Create Process Model API
    request_payload = process_models_controller.process_model_file_create(request_param)
    
     # Mapping values to variables
    name = request_payload.get('name', '')
    type = request_payload.get('type', '')
    content_type = request_payload.get('content_type', '')
    last_modified = request_payload.get('last_modified', '')
    size = request_payload.get('size', '')
    references = request_payload.get('references', '')
    file_contents = request_payload.get('file_contents', '')
    process_model_id = request_payload.get('process_model_id', '')
    bpmn_process_ids = request_payload.get('bpmn_process_ids', '')
    file_contents_hash = request_payload.get('file_contents_hash', '')
    sort_index = request_payload.get('sort_index', '')
    key = process_model_id.split('/')[0],
    
    # Returning response using make_response
    response_data = {
        'id': process_model_id,
        'key': key,
        'name': name,
        'type': type,
        'resource': sort_index,
        'deploymentTime': last_modified,
        'content_type': content_type,
        'size': size,
        'references': references,
        'file_contents': file_contents,
        'bpmn_process_ids': bpmn_process_ids,
        'file_contents_hash': file_contents_hash   

    }
    return make_response(jsonify(response_data), 201)

    