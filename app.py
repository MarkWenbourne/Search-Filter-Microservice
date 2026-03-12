from __future__ import annotations

from flask import Flask, jsonify, request

from engine import keyword_search_payload, filter_items_payload
from schemas import validate_request

app = Flask(__name__)


@app.get('/health')
def health():
    return jsonify({'status': 'ok'}), 200


@app.post('/search')
def search():
    payload = request.get_json(silent=True)
    ok, result = validate_request('search', payload)
    if not ok:
        return jsonify(result), 400
    return jsonify(keyword_search_payload(result)), 200


@app.post('/filter')
def filter_items():
    payload = request.get_json(silent=True)
    ok, result = validate_request('filter', payload)
    if not ok:
        return jsonify(result), 400
    return jsonify(filter_items_payload(result)), 200


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5003, debug=True)
