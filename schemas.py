from __future__ import annotations


def validate_request(endpoint: str, payload):
    if not isinstance(payload, dict):
        return False, error('Request body must be a JSON object.')

    if endpoint == 'search':
        required = ['items', 'query']
        missing = [field for field in required if field not in payload]
        if missing:
            return False, error('Missing required fields.', {'missing': missing})
        if not isinstance(payload['items'], list):
            return False, error('items must be a list.', {'field': 'items'})
        return True, payload

    if endpoint == 'filter':
        required = ['items', 'filters']
        missing = [field for field in required if field not in payload]
        if missing:
            return False, error('Missing required fields.', {'missing': missing})
        if not isinstance(payload['items'], list):
            return False, error('items must be a list.', {'field': 'items'})
        if not isinstance(payload['filters'], dict):
            return False, error('filters must be an object.', {'field': 'filters'})
        return True, payload

    return False, error('Unknown endpoint validation request.')


def error(message: str, details: dict | None = None):
    body = {'errorCode': 'INVALID_REQUEST', 'message': message}
    if details:
        body['details'] = details
    return body
