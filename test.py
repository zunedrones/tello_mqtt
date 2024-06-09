from tello import Swarm

swarm = Swarm(['wlp2s0',
               'wlx002e2dc04580'])

swarm.takeoff()
swarm.land()
