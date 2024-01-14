# LK ICS.2 Room Temperature Control System
This is a Home Assistant custom component that communicates with the LK ICS.2 Room Temperature Control System using Modbus RS485/RTU.

The flow will scan your ICS.2 system and discover control units and zones and add them in a hiearchy representing your system setup. The ICS.2 system supports up to eight control units with a maximum of eight room thermostats totaling 64 possible zones, or rooms.

All entities will have default names but you can easily change name in Home Assistant to make it more user friendly. If you have multiple control units connected the first control unit is named Section 1 and will contain Zones 1-8 and Actuators 1-8. The second section will contain Zones 9-16, Actuators 9-16 and so on.

The hierarcy that you will get in Home Assistant looks like this:

* Section 1
  * Climate Control entities for defined zones with current temperature, temperature setpoint, heating status and possibility to change the temperature
  * Error status sensors
  * Actuator 1
    * Error status sensors
  * Actuator 2
  * Actuator N
  * Zone 1 (Room sensor)
    * Error status sensors
    * Battery status
    * Floor target temperature
    * Floor temperature
    * Heating status
    * Link quality
    * Preset mode
    * Regulation output
    * Room target temperature
    * Room temperature
  * Zone 2
  * Zone N
* Section 2
* Section N
