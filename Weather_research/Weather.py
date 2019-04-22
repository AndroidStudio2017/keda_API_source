import requests
from bs4 import BeautifulSoup


def weather_get(city):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
    }
    urls = [
        'http://www.weather.com.cn/textFC/hb.shtml',
        'http://www.weather.com.cn/textFC/db.shtml',
        'http://www.weather.com.cn/textFC/hz.shtml',
        'http://www.weather.com.cn/textFC/hn.shtml',
        'http://www.weather.com.cn/textFC/hd.shtml',
        'http://www.weather.com.cn/textFC/xb.shtml',
        'http://www.weather.com.cn/textFC/xn.shtml',
        'http://www.weather.com.cn/textFC/gat.shtml'
    ]
    weather_info = {}
    _City = [city]

    for url in urls:
        response = requests.get(url, headers=headers)
        text = response.content.decode('utf-8')
        soup = BeautifulSoup(text, 'html5lib')
        conMidtab = soup.find('div', class_='conMidtab')
        tables = conMidtab.find_all('table')

        for table in tables:
            trs = table.find_all('tr')[2:]
            for index, tr in enumerate(trs):
                _weather_info = {'city': [], 'weather': [], 'wind': [], 'speed': [], 'low': []}
                tds = tr.find_all('td')

                city_td = tds[0]
                weather_td = tds[-4]
                low_td = tds[-2]
                wind_sp = tds[-3].find_all('span')

                if index == 0:
                    city_td = tds[1]

                _city = list(city_td.stripped_strings)[0]
                _weather_info['city'].append(_city)

                if _weather_info['city'] == _City:

                    _weather = list(weather_td.stripped_strings)[0]
                    _weather_info['weather'].append(_weather)

                    _wind = list(wind_sp[0].stripped_strings)[0]
                    _weather_info['wind'].append(_wind)

                    _speed = list(wind_sp[1].stripped_strings)[0]
                    _weather_info['speed'].append(_speed)

                    _low = list(low_td.stripped_strings)[0]
                    _weather_info['low'].append(_low)

                    weather_info = _weather_info

                    break

    return weather_info


def weather_report(city):
    info = weather_get(city)
    report = info['city'][0] + "今日" + info['weather'][0] +"," + str(info['wind'][0]) + str(info['speed'][0])+"," + "最低温度" + str(info['low'][0]) + "摄氏度，祝您生活愉快"
    print(report)
    return report




