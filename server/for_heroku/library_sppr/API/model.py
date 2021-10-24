"""
FakeAPI модели
"""

from django.http import JsonResponse



def get_recomend_and_history(request):
    """
    fakeApi
    :param int id_user:
    :return: json
    """
    id_user = request.GET.get("user_id", None)
    id_user = int(id_user[0]) if id_user else 0
    response = JsonResponse(get_data(id_user))
    return response


def get_data(user_id):
    users_data = {
        1: {
            "recomendations": [
                {
                    "id": 789,
                    "title": "Красная шапочка",
                    "author": "Перро"
                },
                {
                    "id": 101112,
                    "title": "Сказки",
                    "author": "Народ"
                }
            ],
            "history": [
                {
                    "id": 123,
                    "title": "Незнайка на луне",
                    "author": "Носов"
                },
                {
                    "id": 456,
                    "title": "Золотой ключик",
                    "author": "Толстой"
                }
            ]
        },
        2: {

        }
    }

    result = users_data.get(user_id) or {}
    try:
        from .advisor_model import search
        res_search = search(user_id)
        result = res_search
    except Exception as e:
        result.update({'exception': str(e)})

    return result or {}
