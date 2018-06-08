import random
import time
inventory = 0;
person = (100,10,150)
ork = (50,2,0)
money = 150
healthmy = 100
healthenemy = 50
lastrandom1 = -1
lastrandom2 = -1
places = ('Облачный город','Город орков','Деревня гоблинов','Эльфийский лес')
meet = ('Орк','Ларек с пивом', 'Квестовый персонаж')
stage = 0
hard = False
work = False
enemy = -1
while 1:
	if stage == 0:
		print()
		print('Infinite quest')
		print()
		print('1)Start')
		print()
		print('2)Exit')
		print()
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
			print('Вы входите в', places[r])
			if r == 1 or r == 2:
				print()
				print('Персонаж: Это место выглядит опасно...')
				hard = True
			else:
				print()
				print('Персонаж: Здесь довольно уютно и безопасно')
				hard = False
			time.sleep(1)
			if hard == True:
				print()
				print ('Вы встречаете Орка')
				healthenemy = ork[0]
				work = True
				while work == True or healthenemy>0:
					print()
					print('1)Attack')
					print()
					print('2)Use heal')
					print()
					print('3)Leave')
					print()
					i = input('Do your choose:  ')
					if i == '1':
						healthenemy = healthenemy - person[1]
						#time.sleep(1)
						print()
						print('Вы нанесли противнику '+ str(person[1])+' урона. Остаток HP противника равен '+ str(healthenemy))
						healthmy = healthmy - ork[1]
						#time.sleep(1)
						print()
						print('Противник нанес вам '+ str(ork[1])+ ' урона. У вас осталось '+ str(healthmy))
					elif i == '2':
						if inventory > 0:
							healthmy = healthmy + 15
							print()
							print('Вы выпили бутылку пива. У вас осталось '+ str(inventory)+' бутылок')
							healthmy = healthmy - ork[1]
						else:
							print()
							print('У вас нет бутылок с пивасом')
					elif i == '3':
						healthmy = healthmy - ork[1]
						print('Вы начали убегать')
						print('Пока вы убегали, орк снес вам '+ str(ork[1])+' HP')
						work = False
					if healthenemy <= 0:
						print('Вы победили врага!')
						work = False
			else:
				p = random.randint(1,2)
				while p == lastrandom2:
					p = random.randint(1,2)
				print ('Вам по пути встречается ',meet[p])
				work = True
				if p == 1:
					while work == True:
						print('Вы можете купить пиво, одна бутылка стоит 15 монет, а у вас их ',money)
						print()
						print('1)Buy beer ')
						print('2)Leave')
						inp = input('Choose your way:  ')
						if inp == '1':
							am = input('Print amount ')
							testmoney1 = money - (int(am) * 15)
							if testmoney1 >= 0:
								inventory = int(inventory) + int(am)
								money = int(money) - int(am) * 15
							elif money == 0:
								print()
								print('У вас нет деняк')
							else:
								print()
								print('Кассирша: У вас не хватает, берите меньше')
						elif inp == '2':
							work = False
				elif p == 2:
					while work == True:
						print()
						print('Увы, у странника нет квестов, поэтому персонаж идет дальше')
						work = False
						print()
			choose = input('Вы хотите продолжить?(y/n)')
			if choose == 'no':
				stage = 0

			





        
