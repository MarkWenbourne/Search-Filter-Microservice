from __future__ import annotations


def keyword_search_payload(payload: dict) -> dict:
    items = payload['items']
    query = payload['query'].strip().lower()
    if not query:
        return {'query': payload['query'], 'results': items, 'count': len(items)}

    ranked = []
    for item in items:
        text = ' '.join(str(v) for v in item.values()).lower()
        score = text.count(query)
        if score > 0:
            ranked.append((score, item))

    ranked.sort(key=lambda pair: (-pair[0], str(pair[1])))
    results = [item for _, item in ranked]
    return {'query': payload['query'], 'results': results, 'count': len(results)}


def filter_items_payload(payload: dict) -> dict:
    items = payload['items']
    rules = payload['filters']
    filtered = [item for item in items if _matches(item, rules)]
    return {'filters': rules, 'results': filtered, 'count': len(filtered)}


def _matches(item: dict, rules: dict) -> bool:
    for key, expected in rules.items():
        actual = item.get(key)
        if isinstance(expected, list):
            if actual not in expected:
                return False
        else:
            if actual != expected:
                return False
    return True
