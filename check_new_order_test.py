# Алексей Малышев, 8-а когорта — Дипломный проект. Инженер по тестированию плюс

import sender_stand_request



def positive_assert():
    response_get_order = sender_stand_request.get_order()

    assert response_get_order.status_code == 200


def test_check_status_200_response():
    positive_assert()










