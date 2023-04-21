import sender_stand_request

# добываем трек
track = sender_stand_request.track

# проверяем статус код
def status_code_info_order(track):
    response = sender_stand_request.info_order(track)
    assert response.status_code == 200

# Teст №1
# Проверяем, что код статуса 200
def test_status_code():
    status_code_info_order(track)

