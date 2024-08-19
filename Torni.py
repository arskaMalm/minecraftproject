loops.forever(function () {
    agent.move(UP, 1)
    agent.place(DOWN)
    agent.setItem(ENDSTONE, 1, 1)
})
player.onChat("run", function () {
	
})
agent.teleportToPlayer()
