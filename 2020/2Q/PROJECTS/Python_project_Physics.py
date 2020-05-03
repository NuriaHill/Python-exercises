train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1
#1.TEMPERATURE
def f_to_c (f_temp):
  c_temp = (f_temp -32) * 5/9 
  return c_temp

temp1 = f_to_c(100)
print(temp1)#37.77777777777778

def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32 
  return f_temp

temp2 = c_to_f(0)
print(temp2)#32.0

#2.FORCE

def get_force(mass, acceleration):
  force = mass * acceleration
  return mass

train_force = get_force(train_mass, train_acceleration)
print(train_force)#22680

print("The GE train supplies " + str(train_force) + " Newtons of force")#The GE train supplies 22680 Newtons of force

#3.ENERGY
c = 3*10**8
def get_energy(mass, c):
  energy = mass*(c**2)
  return energy

bomb_energy = get_energy (bomb_mass, c)
print(bomb_energy)#90000000000000000
print ("A 1kg bomb suplies "+ str(bomb_energy)+ " Joules")#A 1kg bomb suplies 90000000000000000 Joules

#4.WORK
def get_work(mass, acceleration, distance):
  force = get_force(mass,acceleration)
  work = force * distance
  return work

train_work = get_work(train_mass, train_acceleration, train_distance)

print(train_work)#2268000
print("The GE train does "+ str(train_work)+ " of work over "+ str(train_distance)+ " meters.")#The GE train does 2268000 of work over 100 meters.