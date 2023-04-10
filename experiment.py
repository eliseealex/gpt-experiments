import requests
import json

def invoke(method, **params):
    request_data = json.dumps({
        'action': method,
        'params': params,
        'version': 6
    })

    response = requests.post('http://localhost:8765', data=request_data)
    response_data = json.loads(response.text)

    if response_data.get('error'):
        raise Exception(f"Error: {response_data['error']}")
    else:
        return response_data['result']

def get_all_reviewed_notes():
    all_decks = invoke('deckNames')
    all_reviewed_note_ids = []

    for deck in all_decks:
        reviewed_card_ids = invoke('findCards', query=f'rated:1')
        reviewed_note_ids = [invoke('cardInfo', cardId=card_id)['note']['id'] for card_id in reviewed_card_ids]

        all_reviewed_note_ids.extend(reviewed_note_ids)

    return list(set(all_reviewed_note_ids))

def main():
    reviewed_notes = get_all_reviewed_notes()
    print(f"Reviewed notes count: {len(reviewed_notes)}")
    print("Reviewed notes IDs:", reviewed_notes)

if __name__ == "__main__":
    main()