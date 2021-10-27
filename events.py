# Decorator style event handler
class EventHandler:
  def __init__(self,controller):
    self.c = controller
    self.events = {
      "controllerAxis1":[],
      "controllerAxis2":[],
      "controllerAxis3":[],
      "controllerAxis4":[],

      "controllerButtonAPressed":[],
      "controllerButtonBPressed":[],
      "controllerButtonXPressed":[],
      "controllerButtonYPressed":[],
      "controllerButtonUpPressed":[],
      "controllerButtonDownPressed":[],
      "controllerButtonLeftPressed":[],
      "controllerButtonRightPressed":[],
      "controllerButtonL1Pressed":[],
      "controllerButtonL2Pressed":[],
      "controllerButtonR1Pressed":[],
      "controllerButtonR2Pressed":[],

      "controllerButtonAReleased":[],
      "controllerButtonBReleased":[],
      "controllerButtonXReleased":[],
      "controllerButtonYReleased":[],
      "controllerButtonUpReleased":[],
      "controllerButtonDownReleased":[],
      "controllerButtonLeftReleased":[],
      "controllerButtonRightReleased":[],
      "controllerButtonL1Released":[],
      "controllerButtonL2Released":[],
      "controllerButtonR1Released":[],
      "controllerButtonR2Released":[],
      
      "screenPressed":[],
      "screenReleased":[],
    }

    # Brain Screen
    brain.screen.pressed(self.sp)
    brain.screen.released(self.sr)
    # Controller Button Pressed
    self.c.buttonA.pressed(self.cbap)
    self.c.buttonB.pressed(self.cbbp)
    self.c.buttonX.pressed(self.cbxp)
    self.c.buttonY.pressed(self.cbyp)
    self.c.buttonUp.pressed(self.cbup)
    self.c.buttonDown.pressed(self.cbdp)
    self.c.buttonLeft.pressed(self.cblp)
    self.c.buttonRight.pressed(self.cbrp)
    self.c.buttonL1.pressed(self.cbl1p)
    self.c.buttonL2.pressed(self.cbl2p)
    self.c.buttonR1.pressed(self.cbr1p)
    self.c.buttonR2.pressed(self.cbr2p)
    # Controller Button Released
    self.c.buttonA.pressed(self.cbar)
    self.c.buttonB.pressed(self.cbbr)
    self.c.buttonX.pressed(self.cbxr)
    self.c.buttonY.pressed(self.cbyr)
    self.c.buttonUp.pressed(self.cbur)
    self.c.buttonDown.pressed(self.cbdr)
    self.c.buttonLeft.pressed(self.cblr)
    self.c.buttonRight.pressed(self.cbrr)
    self.c.buttonL1.pressed(self.cbl1r)
    self.c.buttonL2.pressed(self.cbl2r)
    self.c.buttonR1.pressed(self.cbr1r)
    self.c.buttonR2.pressed(self.cbr2r)
    # Controller axis
    self.c.axis1.changed(self.a1c)
    self.c.axis1.changed(self.a2c)
    self.c.axis1.changed(self.a2c)
    self.c.axis1.changed(self.a2c)

  def on(self,name=None):
    def decorator(func):
      eventName = name or func.__name__
      if eventName in self.events:
        self.events[eventName].append(func)
      return func
    return decorator

  def ca1(self):
    pos = self.c.axis1.position()
    for func in self.events["controllerAxis1"]:
      func(pos)

  def ca2(self):
    pos = self.c.axis2.position()
    for func in self.events["controllerAxis2"]:
      func(pos)

  def ca3(self):
    pos = self.c.axis3.position()
    for func in self.events["controllerAxis3"]:
      func(pos)

  def ca4(self):
    pos = self.c.axis4.position()
    for func in self.events["controllerAxis4"]:
      func(pos)

  def cbap(self):
    for func in self.events["controllerButtonAPressed"]: func()

  def cbbp(self):
    for func in self.events["controllerButtonBPressed"]: func()

  def cbxp(self):
    for func in self.events["controllerButtonXPressed"]: func()

  def cbyp(self):
    for func in self.events["controllerButtonYPressed"]: func()

  def cbup(self):
    for func in self.events["controllerButtonUpPressed"]: func()

  def cbdp(self):
    for func in self.events["controllerButtonDownPressed"]: func()

  def cblp(self):
    for func in self.events["controllerButtonLeftPressed"]: func()

  def cbrp(self):
    for func in self.events["controllerButtonRightPressed"]: func()

  def cbl1p(self):
    for func in self.events["controllerButtonL1Pressed"]: func()

  def cbl2p(self):
    for func in self.events["controllerButtonL2Pressed"]: func()

  def cbr1p(self):
    for func in self.events["controllerButtonR1Pressed"]: func()

  def cbr2p(self):
    for func in self.events["controllerButtonR2Pressed"]: func()

  def cbar(self):
    for func in self.events["controllerButtonAReleased"]: func()

  def cbbr(self):
    for func in self.events["controllerButtonBReleased"]: func()

  def cbxr(self):
    for func in self.events["controllerButtonXReleased"]: func()

  def cbyr(self):
    for func in self.events["controllerButtonYReleased"]: func()

  def cbur(self):
    for func in self.events["controllerButtonUpReleased"]: func()

  def cbdr(self):
    for func in self.events["controllerButtonDownReleased"]: func()

  def cblr(self):
    for func in self.events["controllerButtonLeftReleased"]: func()

  def cbrr(self):
    for func in self.events["controllerButtonRightReleased"]: func()

  def cbl1r(self):
    for func in self.events["controllerButtonL1Released"]: func()

  def cbl2r(self):
    for func in self.events["controllerButtonL2Released"]: func()

  def cbr1r(self):
    for func in self.events["controllerButtonR1Released"]: func()

  def cbr2r(self):
    for func in self.events["controllerButtonR2Released"]: func()

  def sp(self):
    x,y = brain.screen.x_position(),brain.screen.y_position()
    for func in self.events["screenPressed"]: func(x,y)

  def sr(self):
    x,y = brain.screen.x_position(),brain.screen.y_position()
    for func in self.events["screenReleased"]: func(x,y)

  def a1c(self):
    pos = self.c.axis1.position()
    for func in self.events["controllerAxis1"]: func(pos)
  
  def a2c(self):
    pos = self.c.axis2.position()
    for func in self.events["controllerAxis2"]: func(pos)
  
  def a3c(self):
    pos = self.c.axis3.position()
    for func in self.events["controllerAxis3"]: func(pos)
  
  def a4c(self):
    pos = self.c.axis4.position()
    for func in self.events["controllerAxis4"]: func(pos)
    
  # COPY THE ABOVE TO USE THE CODE IN YOUR PROGRAM
  # EXAMPLES:
  MyEvents = EventHandler(controller_1)
  
  @MyEvents.on()
  def controllerAxis2(pos):
    motor_1.spin(FORWARD)
    motor_1.set_velocity(pos,PERCENT)
    
  @MyEvents.on("controllerAxis2")
  def leftMotor(pos):
    motor_2.spin(FORWARD)
    motor_1.set_velocity(pos,PERCENT)
    
# DOCS:
# This event handler abstracts callbacks and functions into simple decorator registers.
# You can either name your function the event, or pass a string with the name of the event into the `on` function.
# When the event occurs, the function(s) will be called, with some events providing arguments (Like the controller axis position)

# Events:
# A list of events and their arguments to the functions (if any)

# Controller axis changed events
# controllerAxis1 - Passes a `pos` argument
# controllerAxis2 - Passes a `pos` argument
# controllerAxis3 - Passes a `pos` argument
# controllerAxis4 - Passes a `pos` argument

# Controller button pressed events
# controllerButtonAPressed
# controllerButtonBPressed
# controllerButtonXPressed
# controllerButtonYPressed
# controllerButtonUpPressed
# controllerButtonDownPressed
# controllerButtonLeftPressed
# controllerButtonRightPressed
# controllerButtonL1Pressed
# controllerButtonL2Pressed
# controllerButtonR1Pressed
# controllerButtonR2Pressed

# Controller button released events
# controllerButtonAReleased
# controllerButtonBReleased
# controllerButtonXReleased
# controllerButtonYReleased
# controllerButtonUpReleased
# controllerButtonDownReleased
# controllerButtonLeftReleased
# controllerButtonRightReleased
# controllerButtonL1Released
# controllerButtonL2Released
# controllerButtonR1Released
# controllerButtonR2Released
# 
# Brain Screen events
# screenPressed - Passes an X and a Y argument
# screenReleased - Passes an X and a Y argument
