extends CharacterBody2D

signal log_collected

var velocity = Vector2.ZERO
var logs_collected = 0

@export var speed = 200  

@onready var axe = get_node("axe")
@onready var axe_animation = axe.get_node("axe_animation")


# this is so the player moves isometricly in a grid
func cartision_to_isometric(cartision):
	return Vector2(cartision.x - cartision.y, (cartision.x + cartision.y) / 2)

# getting input from the player
func get_movement_input():
	velocity = Vector2.ZERO

	velocity.x = Input.get_action_strength("right") - Input.get_action_strength("left")
	velocity.y = Input.get_action_strength("down") - Input.get_action_strength("up")

	velocity = velocity.normalized() * speed
	velocity = cartision_to_isometric(velocity)
	
func _input(event):
	if Input.is_action_pressed("attack") and not axe_animation.is_playing():
		axe_animation.play("axe_animation")

# all the players pysics
func _physics_process(delta):
	get_movement_input()
	set_velocity(velocity)
	move_and_slide()
	velocity = velocity
	
func add_log():
	emit_signal("log_collected")
	logs_collected += 1
	print("colected log! Number of logs: ", logs_collected)
	
	if logs_collected == 3:
		get_tree().change_scene_to_file("res://you_win.tscn")
		print("you win")
