f = m = a = 0.0  # force, mass, accelleration


def force(m,a):
  return m*a

def mass(f,a):
  return f/a

def accel(f,m):
  return f/m

def set_force():
  global f
  f = float(raw_input("force >"))

def set_mass():
  global m
  m = float(raw_input("mass >"))

def set_accel():
  global a
  a = float(raw_input("accel >"))

def proc_user_select(i):
  if i == 1:
    set_mass()
    set_accel() 
    return force(m,a)
  elif i == 2:
    set_force()
    set_accel()
    return mass(f,a)
  elif i == 3:
    set_force()
    set_mass()
    return accel(f,m)

def user_select():
  fma = ["force", "mass", "accel"]
  print("force, mass, acceleration calculator")
  print("select one")
  print("1. "+fma[0]+"\n2. "+fma[1]+"\n3. "+fma[2])
  user_input = int(raw_input("> "))
  ans = str(proc_user_select(user_input))
  print(fma[user_input-1]+" = "+ans)

# main  
user_select()