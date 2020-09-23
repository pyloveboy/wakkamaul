# This is code :
hero.moveUp()
while True:
    hero.moveLeft()
    enemy = hero.findNearestEnemy()
    if enemy:    
        hero.attack(enemy)
    hero.say("scout")
