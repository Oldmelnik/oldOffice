import requests

def get():
	f = requests.get('https://yandex.ru/pogoda/moscow?lat=55.56891632&lon=37.57052612')
	data = f.text
	f.close()

	curr_temp_start = data.find('<div class="temp fact__temp fact__temp_size_s" role="text"><span class="temp__value">', 0, len(data))
	curr_temp_end = data.find('</span>', curr_temp_start, curr_temp_start+160)
	curr_temp = data[curr_temp_start+85:curr_temp_end]+"°C"
	curr_temp = curr_temp.replace("−", "-")

	situation_prestart = data.find('<div class="link__condition day-anchor i-bem"', curr_temp_start, len(data))
	situation_start = data.find('>', situation_prestart, situation_prestart+150)
	situation_end = data.find('</div>', situation_start, situation_start+70)
	situation = data[situation_start+1:situation_end]

	wind_start = data.find('class="wind-speed">', curr_temp_end, len(data))
	wind_end = data.find('</span>', wind_start, wind_start+70)
	wind = data[wind_start+19:wind_end]

	ans = u"Сейчас на улице " + situation.lower() +u"\nТемпература: " + curr_temp + u"\nВетер: " + wind + u" м/с"
	# print(ans)

	return ans

if __name__ == '__main__':
	print(get())
