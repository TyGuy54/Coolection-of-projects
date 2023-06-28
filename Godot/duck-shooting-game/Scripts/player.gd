extends CharacterBody2D

@export var Bullet = preload("res://Sceans/bullet.tscn")
@onready var gun = $gun
@onready var camrea = $Camera2D
const SPEED = 300.0

func _enter_tree():
	set_multiplayer_authority(str(name).to_int())
	
func _ready():
	if not get_multiplayer_authority():
		return
		

func _process(delta):
	if not get_multiplayer_authority():
		return
		
	# storing the result of subtracking the global mouse position and the players global position
	# then normalizing it to get nicer numbers
	# (print get_global_mouse_position() and global_position to see what I mean the numbers are vary large)
	var mouse_direction = (get_global_mouse_position() - global_position).normalized()
	#var sprite = $Player
	
	# if the players mouse is less that or grater than the players position (right around the middle of the players sprite)
	# then flip the player sprite to look towrd the mouse
	#if mouse_direction.x > 0 and sprite.flip_h:
		#sprite.flip_h = false
	#elif mouse_direction.x < 0 and not sprite.flip_h:
		#sprite.flip_h = true
		
	# sword.rotation stores the mouse_directions angle relative to the sword node
	gun.rotation = mouse_direction.angle() 
	#sword_hitbox.knockback_direction = mouse_direction
	# print(sword.rotation)
	if gun.scale.y == 1 and  mouse_direction.x < 0:
		gun.scale.y = -1 
	elif gun.scale.y == -1 and  mouse_direction.x > 0:
		gun.scale.y = 1 



func _physics_process(delta: float) -> void:
	if not get_multiplayer_authority():
		return
		
	var input_dir = Input.get_vector("left", "right", "up", "down")
	velocity = input_dir * SPEED
	move_and_slide() 
	
	if Input.is_action_just_pressed("ui_accept"):
		shoot()
		
func shoot():
	var b = Bullet.instantiate()
	add_child(b)
	b.transform = $gun/Muzzle.global_transform
