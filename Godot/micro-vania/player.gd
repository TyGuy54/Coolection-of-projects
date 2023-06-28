extends Character_Base # class the player is inheriting from

@onready var animation= $Sprite
@onready var jump_buffer: Timer = $jump_buffer
#@onready var weapon = $weapon


# the proccess function runs once per frame
func _process(delta: float) -> void:
	var mouse_direction = (get_global_mouse_position() - global_position).normalized()
	
	#if mouse_direction.x > 0 and animation.flip_h:
		#animation.flip_h = false
	#elif mouse_direction.x < 0 and not animation.flip_h:
		#animation.flip_h = true
		
	#weapon.rotation = mouse_direction.angle()
	
	#if weapon.scale.y == 1 and mouse_direction.x < 0:
		#weapon.scale.y = -1
		#print(weapon.scale.y)
	#elif weapon.scale.y == -1 and mouse_direction.x > 0:
		#weapon.scale.y = 1
		#print(weapon.scale.y)
	

# processes physics, in this cases it process 2D physics
func _physics_process(delta: float) -> void:
	# the base character class that has generic code for 
	# any character like movement physics, jumping and health
	character_physics(delta, get_input())
	handle_jump()
	#wall_jump()
	
# player inputs for moveing left and right
func get_input():
	var horizontal := 0.0
	
	if Input.is_action_pressed("ui_left"):
		animation.flip_h = true
		horizontal -= 1.0
	
	elif Input.is_action_pressed("ui_right"):
		animation.flip_h = false
		horizontal += 1.0
		
	else:
		animation.play("idle")

	return horizontal

# funtion to handle the players jump inputs 
# and other special jumping funtionality
func handle_jump():
	if Input.is_action_just_pressed("ui_accept"):
		jump_buffer.start()
	
	if is_on_floor():
		if !jump_buffer.is_stopped():
			jump(jump_buffer)
		
	else:
		# play player's jump animation
		pass
	
	# if the player press the space bar they will jump
	if Input.is_action_just_released("ui_accept") and velocity.y < jump_height * 0.3:
			velocity.y = jump_height * 0.3
			velocity.y = jump_time_to_peak * 0.3
			velocity.y = jump_time_to_descent * 0.3
			
#func wall_jump():
	# possable wall jumping?!?!
	#if is_on_wall():
		#velocity.y = jump_time_to_descent * 0.1
		
	#if Input.is_action_just_pressed("ui_accept") and velocity.y < jump_height * 0.3:
		#jump()
