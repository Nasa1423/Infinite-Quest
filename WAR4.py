from random import *
from colorama import Fore, Back, Style, init
import random
import time
import os
init()
inventory = 0;
xp = 0
level = 0
person = [100,10,150]
ork = [50,2,0]
heal = 0
save = 0
BOSS = [2000,20,0]
Monster = [1000,10,0]
meindamage = [0]
fortime1 = ['']
fortime2 = ['']
line1 = ['','','']
line2 = ['','','']
line11 = ['','','']
line22 = ['','','']
line12 = ['','','']
line21 = ['','','']
money = 150
damage = 10
abilitye = []
tapes = []
chose = ["","",""]
healthmymax = 100
healthmy = 100
healthenemy = 50
healthenemyhard = 2000
healthenemymedium = 1000
lastrandom1 = -1
lastrandom2 = -1
weapon = 'рук'
power = 0
iitems = []
nameiitems = []
cost = [50,70,110,150,80,250,400,200]
damag = [30,20,50,60,45,80,75,0]
items = ('Меч','Лук','Зелье силы','Дубина','Кинжал','Волшебная Чекушка','Пистоль','Зелье Здоровья')
places = ('Облачный город','Город орков','Деревня гоблинов','Эльфийский лес')
meet = ('Орк','Ларек с пивом', 'Квестовый персонаж','БОСС',)
stage = 0
hard = False
work = False
enemy = -1
while 1:
	if stage == 0:
		heal = 0
		inventory = 0;
		xp = 0
		level = 0
		person = (100,10,150)
		ork = (50,2,0)
		save = 0
		BOSS = (2000,20,0)
		Monster = (1000,10,0)
		money = 150
		damage = 10
		chose = ["","",""]
		healthmymax = 100
		healthmy = 100
		healthenemy = 50
		healthenemyhard = 2000
		healthenemymedium = 1000
		lastrandom1 = -1
		lastrandom2 = -1
		weapon = 'рук'
		power = 0
		iitems = []
		number=['','','']
		cost = [50,70,110,150,80,250,400,200]
		damag = [30,20,50,60,45,80,75,0]
		items = ('Меч','Лук','Зелье силы','Дубина','Кинжал','Волшебная Чекушка','Пистоль','Зелье Здоровья')
		places = ('Облачный город','Город орков','Деревня гоблинов','Эльфийский лес')
		meet = ('Орк','Ларек с пивом', 'Квестовый персонаж','БОСС',)
		stage = 0
		hard = False
		work = False
		enemy = -1
		os.system("cls")
		print(Fore.RED)
		print('Infinite quest (Alpha 0.01)')
		print(Style.RESET_ALL)
		print(Fore.WHITE)
		print(Back.RED)
		print('1)Start')
		print()
		print('2)Exit')
		print(Style.RESET_ALL)
		i = input('Enter a number what to do:  ')
		if i == '1':
			stage = 1
		if i == '2':
			break
	elif stage == 1:
		while stage == 1:
			r = random.randint(0,3)
			while r == lastrandom1:
				r = random.randint(0,3)
			os.system("cls")
			print('Вы входите в', places[r])
			if r == 1 or r == 2:
				print(Style.RESET_ALL)
				print(Fore.RED)
				print(Back.WHITE)
				print('Персонаж: Это место выглядит опасно...')
				hard = True
			else:
				print()
				print(Style.RESET_ALL)
				print(Fore.GREEN)
				print(Back.BLUE)
				print('Персонаж: Здесь довольно уютно и безопасно')
				hard = False
			time.sleep(1)
			if hard == True:
				enemizer = random.randint(0,6)
				print(Style.RESET_ALL)
				if enemizer >= 1 and enemizer <= 2:
					print ('Вы встречаете'+Fore.RED+ ' Орка')
					healthenemy = ork[0]
					work = True
					while work == True and healthenemy>0 and healthmy > 0:
						print(Fore.RED)
						print('1)Attack')
						print(Fore.GREEN)
						print('2)Use heal')
						print(Fore.YELLOW)
						print('3)inventory')
						print(Fore.BLUE)
						print('4)Leave')
						print(Style.RESET_ALL)
						i = input('Do your choose:  ')
						if i == '1':
							healthenemy = healthenemy - damage
							#time.sleep(1)
							print()
							os.system("cls")
							print('Вы нанесли противнику '+ str(damage)+' урона c помощью '+weapon+'. Остаток HP противника равен '+ str(healthenemy))
							healthmy = healthmy - ork[1]
							#time.sleep(1)
							print()
							print('Противник нанес вам '+ str(ork[1])+ ' урона. У вас осталось '+ str(healthmy))
						elif i == '2':
							os.system("cls")
							if inventory > 0:
								if healthmy < healthmymax:
									healthmy = healthmy + 15
									print()
									inventory -= 1
									print('Вы выпили бутылку пива. У вас осталось '+ str(inventory)+' бутылок')
									healthmy = healthmy - ork[1]
								else:
									print('У вас максимум HP')
							else:
								print()
								print('У вас нет бутылок с пивасом')
						elif i == '3':
							os.system("cls")
							n=0
							print('Вооружиться:')
							for h in nameiitems:
								n=n+1
								print(str(n)+')'+str(h))
							print('Тем же, что и было(stay)')
							l = input('Сделай выбор: ')
							if l != 'stay':
								g = int(l)-1
							if l == 'stay':
								continue
								weapon = 'рук'
							else:
								if iitems[g] == 'Зелье Здоровья' and heal == 0:
									healthmymax = healthmymax + 50
									heal = 1
									print('Ваше максимальное здоровье увеличилось, теперь оно равно '+ str(healthmymax))
									print('Ваше действительное здоровье равно '+ healthmy)
								elif iitems[g] == 'Зелье силы':
									power = 1
									damage+=50
								else:
									damage = 10+ 50*power
									damage = damage + (damag[items.index(iitems[g])]) + meindamage[int(l)]
									weapon = nameiitems[g]
							os.system("cls")
						elif i == '4':
							os.system("cls")
							healthmy = healthmy - ork[1]
							print('Вы начали убегать')
							print('Пока вы убегали, орк снес вам '+ str(ork[1])+' HP')
							print('У вас осталось'+str(healthmy)+'HP')
							work = False
						else:
								os.system('cls')
								print('Неправильный ввод!')
						if healthenemy <= 0:
							print(Fore.RED+'В'+Fore.GREEN+'ы '+Fore.BLUE+'п'+Fore.YELLOW+'о'+Fore.GREEN+'б'+Fore.BLUE+'е'+Fore.RED+'д'+Fore.GREEN+'и'+Fore.BLUE+'л'+Fore.RED+'и '+Fore.YELLOW+ 'в'+Fore.GREEN+'р'+Fore.BLUE+'а'+Fore.YELLOW+'г'+Fore.RED+'а'+Fore.GREEN+'!')
							add = random.randint(20,100)
							print('Вы получили '+ str(add) +' монет!')
							xp+= 20
							print('Вы получили 20 xp')
							level = xp // 50
							print('Ваш lvl равен '+ str(level))
							money = money + add
							work = False
						if healthmy <= 0:
							print(Style.RESET_ALL)
							os.system("cls")
							print(Fore.RED+'ВЫ ПОГИБЛИ! Возврат в главное меню!')
							work = False
							stage = 0
					healthmy = ork[0]
				elif enemizer == 3 and level > 10:
					print ('Вы встречаете'+Fore.RED+ ' БОССА')
					healthenemyhard = BOSS[0]
					work = True
					while work == True and healthenemyhard>0 and healthmy > 0:
						print(Fore.RED)
						print('1)Attack')
						print(Fore.GREEN)
						print('2)Use heal')
						print(Fore.YELLOW)
						print('3)inventory')
						print(Fore.BLUE)
						print('4)Leave')
						print(Style.RESET_ALL)
						i = input('Do your choose:  ')
						if i == '1':
							os.system("cls")
							trial = random.randint(1,3)
							if trial == 1 or trial == 2:
								healthenemyhard = healthenemyhard - damage
								#time.sleep(1)
								print()
								os.system("cls")
								print('Вы нанесли противнику '+ str(damage)+' урона c помощью '+weapon+'. Остаток HP противника равен '+ str(healthenemyhard))
								healthmy = healthmy - BOSS[1]
							#time.sleep(1)
							print()
							print('Противник нанес вам '+ str(BOSS[1])+ ' урона. У вас осталось '+ str(healthmy))
						elif i == '2':
							os.system("cls")
							if inventory > 0:
								if healthmy < healthmymax:
									healthmy = healthmy + 15
									print()
									inventory -= 1
									print('Вы выпили бутылку пива. У вас осталось '+ str(inventory)+' бутылок')
									healthmy = healthmy - ork[1]
								else:
									print('У вас максимум HP')
							else:
								print()
								print('У вас нет бутылок с пивасом')
						elif i == '3':
							os.system("cls")
							n=0
							print('Вооружиться:')
							for h in nameiitems:
								n=n+1
								print(str(n)+')'+str(h))
							print('Тем же, что и было(stay)')
							l = input('Сделай выбор: ')
							if l != 'stay':
								g = int(l)-1
							if l == 'stay':
								continue
								weapon = 'рук'
							else:
								if iitems[g] == 'Зелье Здоровья' and heal == 0:
									healthmymax = healthmymax + 50
									heal = 1
									print('Ваше максимальное здоровье увеличилось, теперь оно равно '+ str(healthmymax))
									print('Ваше действительное здоровье равно '+ healthmy)
								elif iitems[g] == 'Зелье силы':
									power = 1
									damage+=50
								else:
									damage = 10+ 50*power
									damage = damage + (damag[items.index(iitems[g])]) + meindamage[int(l)]
									weapon = nameiitems[g]	
						elif i == '4':
							os.system("cls")
							healthmy = healthmy - BOSS[1]
							print('Вы начали убегать')
							print('Пока вы убегали, БОСС снес вам '+ str(BOSS[1])+'  HP')
							print('У вас осталось'+str(healthmy)+'HP')
							work = False
						else:
								os.system('cls')
								print('Неправильный ввод!')
						if healthenemyhard <= 0:
							print(Fore.RED+'В'+Fore.GREEN+'ы '+Fore.BLUE+'п'+Fore.YELLOW+'о'+Fore.GREEN+'б'+Fore.BLUE+'е'+Fore.RED+'д'+Fore.GREEN+'и'+Fore.BLUE+'л'+Fore.RED+'и '+Fore.YELLOW+ 'в'+Fore.GREEN+'р'+Fore.BLUE+'а'+Fore.YELLOW+'г'+Fore.RED+'а'+Fore.GREEN+'!')
							add = random.randint(200,500)
							print('Вы получили '+ str(add) +' монет!')
							xp += 100
							print()
							print('Вы получили 100 xp')
							level = xp // 50
							print('Ваш lvl равен '+ level)
							money = money + add
							work = False
						if healthmy <= 0:
							print(Style.RESET_ALL)
							os.system("cls")
							print(Fore.RED+'ВЫ ПОГИБЛИ! Возврат в главное меню!')
							work = False
							stage = 0
					healthenemyhard = BOSS[0]
				elif enemizer >= 4 and enemizer <= 6 and level > 5:
					print ('Вы встречаете'+Fore.RED+ ' Монстра')
					healthenemymedium = Monster[0]
					work = True
					while (work == True) and (healthenemymedium>0) and (healthmy > 0):
						print(Fore.RED)
						print('1)Attack')
						print(Fore.GREEN)
						print('2)Use heal')
						print(Fore.YELLOW)
						print('3)inventory')
						print(Fore.BLUE)
						print('4)Leave')
						print(Style.RESET_ALL)
						i = input('Do your choose:  ')
						if i == '1':
							os.system("cls")
							healthenemymedium = healthenemymedium - damage
							#time.sleep(1)
							print()
							os.system("cls")
							print('Вы нанесли противнику '+ str(damage)+' урона c помощью '+weapon+'. Остаток HP противника равен '+ str(healthenemymedium))
							healthmy = healthmy - Monster[1]
							#time.sleep(1)
							print()
							print('Противник нанес вам '+ str(Monster[1])+ ' урона. У вас осталось '+ str(healthmy))
						elif i == '2':
							os.system("cls")
							if inventory > 0:
								os.system("cls")
								if healthmy < healthmymax:
									healthmy = healthmy + 15
									print()
									inventory -= 1
									print('Вы выпили бутылку пива. У вас осталось '+ str(inventory)+' бутылок')
									healthmy = healthmy - Monster[1]
								else:
									print('У вас максимум HP')
							else:
								print()
								print('У вас нет бутылок с пивасом')
						elif i == '3':
							os.system("cls")
							n=0
							print('Вооружиться:')
							for h in nameiitems:
								n=n+1
								print(str(n)+')'+str(h))
							print('Тем же, что и было(stay)')
							l = input('Сделай выбор: ')
							if l != 'stay':
								g = int(l)-1
							if l == 'stay' or l == '':
								continue
								weapon = 'рук'
							else:
								if iitems[g] == 'Зелье Здоровья' and heal == 0:
									healthmymax = healthmymax + 50
									heal = 1
									print('Ваше максимальное здоровье увеличилось, теперь оно равно '+ str(healthmymax))
									print('Ваше действительное здоровье равно '+ healthmy)
								elif iitems[g] == 'Зелье силы':
									print('Зелье силы активировано-+50 к урону')
									power = 1
									damage+=50
								else:
									damage = 10+ 50*power
									damage = damage + (damag[items.index(iitems[g])]) + meindamage[int(l)]
									weapon = nameiitems[g]
						elif i == '4':
							os.system("cls")
							healthmy = healthmy - Monster[1]
							print('Вы начали убегать')
							print('Пока вы убегали, Монстр снес вам  '+ str(Monster[1])+' HP')
							print('У вас осталось'+str(healthmy)+'HP')
							work = False
						else:
								os.system('cls')
								print('Неправильный ввод!')
						if healthenemymedium <= 0:
							print(Fore.RED+'В'+Fore.GREEN+'ы '+Fore.BLUE+'п'+Fore.YELLOW+'о'+Fore.GREEN+'б'+Fore.BLUE+'е'+Fore.RED+'д'+Fore.GREEN+'и'+Fore.BLUE+'л'+Fore.RED+'и '+Fore.YELLOW+ 'в'+Fore.GREEN+'р'+Fore.BLUE+'а'+Fore.YELLOW+'г'+Fore.RED+'а'+Fore.GREEN+'!')
							add = random.randint(100,200)
							print('Вы получили '+ str(add) +' монет!')
							xp+= 50
							print('Вы получили 50 xp')
							level = xp // 50
							print('Ваш lvl равен '+ str(level))
							money = money + add
							work = False
						if healthmy <= 0:
							print(Style.RESET_ALL)
							os.system("cls")
							print(Fore.RED+'ВЫ ПОГИБЛИ! Возврат в главное меню!')
							work = False
							stage = 0
					healthenemymedium = Monster[0]
			else:
				p = random.randint(1,2)
				os.system("cls")
				print ('Вам по пути встречается ',meet[p])
				work = True
				if p == 1:
					while work == True:
						os.system("cls")
						print(Fore.RED)
						print('Продавец:Таки добрый день! Хотите что-то купить. Сразу говорю, я могу что-то из своих вещей не продавать')
						print(Fore.GREEN)
						print('Вы можете купить пиво, одна бутылка стоит 15 монет, а у вас их '+Fore.YELLOW+str(money))
						print(Style.RESET_ALL)
						print(Fore.GREEN)
						print('1)Buy beer ')
						print(Fore.YELLOW)
						print('2)Buy items')
						print(Fore.RED)
						print('3)Leave')
						print(Style.RESET_ALL)
						inp = input('Choose your way:  ')
						if inp == '1':
							am = input('Print amount ')
							testmoney1 = money - (int(am) * 15)
							if testmoney1 >= 0:
								inventory = int(inventory) + int(am)
								money = int(money) - int(am) * 15
							elif money == 0:
								print(Style.RESET_ALL)
								print('У вас нет деняк')
							else:
								print(Style.RESET_ALL)
								print('Кассирша: У вас не хватает, берите меньше')
						elif inp == '2':
							for i in range(3):
								chose[i] = choice(items)
								number[i] = items.index(chose[i])
								line2[i] = random.choice(open('type.txt').readlines())
								line1[i] = random.choice(open('ability.txt').readlines())
								fortime1 = line1[i].split(' ')
								fortime2 = line2[i].split(' ')
								line11[i] = fortime1[0]
								line12[i] = fortime1[1]
								line21[i] = fortime2[0]
								line22[i] = fortime2[1]
								n = i + 1
								print()
								print(n,')',line11[i] + ' ' + line21[i] +' '+chose[i],'(',cost[number[i]],')')
							print()
							print('Выбирай!')
							chois = input()
							if chois == '1' or chois == '2' or chois == '3':
								chhh = int(chois) - 1
							if chois == '1':
								if money >= cost[number[int(chois)]]:
									money = money - cost[number[int(chois)]]
									print('Покупка совершена, ваш остаток '+ str(money) + ' монет')
									iitems.append(items[number[1]])
									nameiitems.append(line11[chhh] +line21[chhh] +items[number[chhh]])
									meindamage.append(int(line12[chhh])+int(line22[chhh]))
								else:
									print('У вас недостаточно денег')
							elif chois == '2':
								if money >= cost[number[int(chois)]]:
									money = money - cost[number[int(chois)]]
									print('Покупка совершена, ваш остаток '+ str(money) + ' монет')
									iitems.append(items[number[2]])
									nameiitems.append(line11[chhh] +line21[chhh] +items[number[chhh]])
									meindamage.append(int(line12[chhh])+int(line22[chhh]))
								else:
									print('У вас недостаточно денег')
							elif chois == '3':
								if money >= cost[number[int(chois)]]:
									money = money - cost[number[int(chois)]]
									print(Style.RESET_ALL+'Покупка совершена, ваш остаток '+Fore.YELLOW+ str(money) +Style.RESET_ALL+ ' монет')
									iitems.append(items[number[3]])
									nameiitems.append(line11[chhh] +line21[chhh] +items[number[chhh]])
									meindamage.append(int(line12[chhh])+int(line22[chhh]))

								else:
									print(Fore.RED+'У вас недостаточно денег')
							elif chois == '':
								print()
							else:
								print('Неправильный ввод!')
						elif inp == '3':
							work = False
				elif p == 2:
					while work == True:
						print(Style.RESET_ALL)
						print('Увы, ваш уровень меньше 10000, идите дальше фармите!')
						work = False
						print(Style.RESET_ALL)
			choose = input('Вы хотите продолжить?(y/n)')
			#save++
			#if save >= 10:
				#f = open('save.txt','w')
				#w = file.read()
				#q = w.split(' ')
				#q.append(healthmy)
				#q.append(healthmymax)
				#q.append(healthmy)
				#q.append(healthmy)
				#q.append(healthmy)
			if choose == 'no':
				os.system("cls")
				stage = 0

			





        
