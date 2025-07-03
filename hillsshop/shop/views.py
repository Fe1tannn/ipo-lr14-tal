from django.http import HttpResponse
from django.shortcuts import render
from .models import Establishment
import json
import re

def load_establishments():
    document = """
    <DOCUMENT filename="dump.json">
    [
        {
            "model": "data.establishment",
            "pk": 1,
            "fields": {
                "title": "Минский государственный колледж цифровых технологий",
                "short_title": "МГКЦТ",
                "desc": "Колледж имеет в городе и республике положительный имидж и важно это состояние удержать...",
                "adress": "г. Минск, ул. Казинца, 91",
                "tel": "+375 17 374 11 62",
                "email": "mgke@minskedu.gov.by",
                "wsite": "https://mgkct.minskedu.gov.by/",
                "wtel": "https://t.me/mgkelektron",
                "wvk": null,
                "winsta": null,
                "wface": null,
                "wtwit": null,
                "wtic": null,
                "wother": null,
                "icon": "est/1.gif",
                "prev": "",
                "promo_medio": "",
                "coords": "53.848216, 27.509740"
            }
        },
        {
            "model": "data.establishment",
            "pk": 2,
            "fields": {
                "title": "Минский государственный колледж ремесленничества и дизайна имени Н.А. Кедышко",
                "short_title": "МГКРиД",
                "desc": "Глава администрации Советского района Сергей Хильман 10 ноября вручил благодарственные письма...",
                "adress": "г. Минск, ул. Сурганова, 45/1",
                "tel": "+375173794355",
                "email": "ptk-dpi@minskedu.gov.by",
                "wsite": "https://kedyshko-college.by/",
                "wtel": "https://t.me/ptkdpi",
                "wvk": null,
                "winsta": null,
                "wface": null,
                "wtwit": null,
                "wtic": null,
                "wother": null,
                "icon": "est/2.png",
                "prev": "",
                "promo_medio": "",
                "coords": "53.926709, 27.587812"
            }
        },
        ...(остальные записи усечены для краткости)...
    ]
    </DOCUMENT>
    """
    # Извлечение JSON с помощью регулярного выражения
    json_str = re.search(r'\[\s*(.*?)\s*\]', document, re.DOTALL)
    if json_str:
        try:
            data = json.loads(json_str.group(0))
            establishments = [item["fields"] for item in data if item["model"] == "data.establishment"]
            for est in establishments:
                Establishment.objects.update_or_create(
                    id=est["pk"],  # Используем id вместо pk
                    defaults={
                        "title": est["title"],
                        "short_title": est["short_title"],
                        "desc": est["desc"],
                        "adress": est["adress"],
                        "tel": est["tel"],
                        "email": est["email"],
                        "wsite": est["wsite"],
                        "wtel": est["wtel"],
                        "wvk": est["wvk"],
                        "winsta": est["winsta"],
                        "wface": est["wface"],
                        "wtwit": est["wtwit"],
                        "wtic": est["wtic"],
                        "wother": est["wother"],
                        "icon": est["icon"],
                        "prev": est["prev"],
                        "promo_medio": est["promo_medio"],
                        "coords": est["coords"]
                    }
                )
            return establishments
        except json.JSONDecodeError as e:
            print(f"Ошибка декодирования JSON: {e}")
            return []
    return []

def spec_list(request):
    load_establishments()
    establishments = Establishment.objects.all()
    return render(request, 'shop/spec_list.html', {'establishments': establishments})

def spec_detail(request, id):
    try:
        establishment = Establishment.objects.get(id=id)
        return render(request, 'shop/spec_detail.html', {'establishment': establishment})
    except Establishment.DoesNotExist:
        return HttpResponse("Ошибка: Учреждение с указанным ID не найдено.")