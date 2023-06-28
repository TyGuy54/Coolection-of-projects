extends KinematicBody2D

const UP_DIR = Vector2.UP

export var speed = 600.0
export var jump_str = 1500.0
export var maximum_jumps = 2
export var double_jump_str = 1200.0
export var gravity = 4500.0

var friction = 0.1
var acceleration = 0.5

var jumps_made = 0
var velocity = Vector2.ZERO

# checking if a player is on a slope 
# if the player is then the player will roll
func is_on_slope():
	pass

# makes the player roll when the
# player moves to the left or roght
func rolling(dir):
	if dir == 1:
		rotate(.1)
	if dir == -1:
		rotate(-.1)
	else:
		rotate(0)

# a built in function for cool physics stuff
func _physics_process(delta):
	# player movemnt for the left and right
	var horizontal_dir = (
		Input.get_action_strength("right") - 
		Input.get_action_strength("left")
	)
	
	# making the player move and roll
	#velocity.x = horizontal_dir * speed
	if horizontal_dir !=  0:
		# accelerate when there's input
		velocity.x = lerp(velocity.x, horizontal_dir * speed, acceleration)
	else:
		# slow down when there's no input
		velocity.x = lerp(velocity.x, 0, friction)
		
	velocity.y += gravity * delta
	
	rolling(horizontal_dir)
	
		
	# a collection of player jumping physics varables
	var is_falling = velocity.y > 0.0 and not is_on_floor()
	var is_jumping = Input.is_action_just_pressed("jump") and is_on_floor()
	var is_double_jumping = Input.is_action_just_pressed("jump") and is_falling
	var is_jump_cancled = Input.is_action_just_pressed("jump") and velocity.y < 0.0
	var is_idling = is_on_floor() and is_zero_approx(velocity.x)
	var is_running = is_on_floor() and not is_zero_approx(velocity.x)

	# making the player jump
	if is_jumping:
		jumps_made += 1
		velocity.y = -jump_str
	elif is_double_jumping:
		jumps_made += 1
		if jumps_made <= maximum_jumps:
			velocity.y = -double_jump_str
	elif is_jump_cancled:
		velocity.y = 0.0
	elif is_idling or is_running:
		jumps_made = 0
	
	
	velocity = move_and_slide(velocity, UP_DIR)
