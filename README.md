# vex-python
Various pieces of code that I use in my Vex Robotics projects

# Docs
## [Event Handler](https://github.com/SkyTheCodeMaster/vex-python/blob/master/events.py)

The event handler abstracts adding functions as callbacks into a simple decorator interface.
In order to use it, you must copy the `EventHandler` class into your code.
Examples:
```py
MyEvents = EventHandler(controller_1)

@MyEvents.on("controllerAxis1")
def PrintAxis(pos):
  print(pos)
```
<details>
  <summary>Event Reference</summary>
  
  | Event Name                      | Argument 1 | Argument 2 |
|---------------------------------|------------|------------|
| `controllerAxis1`               | `pos`      |            |
| `controllerAxis2`               | `pos`      |            |
| `controllerAxis3`               | `pos`      |            |
| `controllerAxis4`               | `pos`      |            |
|                                 |            |            |
| `controllerButtonAPressed`      |            |            |
| `controllerButtonBPressed`      |            |            |
| `controllerButtonXPressed`      |            |            |
| `controllerButtonYPressed`      |            |            |
| `controllerButtonUpPressed`     |            |            |
| `controllerButtonDownPressed`   |            |            |
| `controllerButtonLeftPressed`   |            |            |
| `controllerButtonRightPressed`  |            |            |
| `controllerButtonL1Pressed`     |            |            |
| `controllerButtonL2Pressed`     |            |            |
| `controllerButtonR1Pressed`     |            |            |
| `controllerButtonR2Pressed`     |            |            |
|                                 |            |            |
| `controllerButtonAReleased`     |            |            |
| `controllerButtonBReleased`     |            |            |
| `controllerButtonXReleased`     |            |            |
| `controllerButtonYReleased`     |            |            |
| `controllerButtonUpReleased`    |            |            |
| `controllerButtonDownReleased`  |            |            |
| `controllerButtonLeftReleased`  |            |            |
| `controllerButtonRightReleased` |            |            |
| `controllerButtonL1Released`    |            |            |
| `controllerButtonL2Released`    |            |            |
| `controllerButtonR1Released`    |            |            |
| `controllerButtonR2Released`    |            |            |
|                                 |            |            |
| `screenPressed`                 | `x`        | `y`        |
| `screenReleased`                | `x`        | `y`        |
</details>
