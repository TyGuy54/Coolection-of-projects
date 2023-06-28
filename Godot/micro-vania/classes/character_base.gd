extends CharacterBody2D
class_name Character_Base

@export var move_speed: int = 200.0
@export var hp: int = 0

#var velocity: Vector2 = Vector2.ZERO

@export var jump_height : float
@export var jump_time_to_peak : float
@export var jump_time_to_descent : float

@onready var jump_velocity : float = ((2.0 * jump_height) / jump_time_to_peak) * -1.0
@onready var jump_gravity : float = ((-2.0 * jump_height) / (jump_time_to_peak * jump_time_to_peak)) * -1.0
@onready var fall_gravity : float = ((-2.0 * jump_height) / (jump_time_to_descent * jump_time_to_descent)) * -1.0


func character_physics(delta: float, get_input) -> void:
	velocity.y += get_gravity() * delta
	velocity.x = get_input * move_speed
	
	move_and_slide()
	
func get_gravity() -> float:
	return jump_gravity if velocity.y < 0.0 else fall_gravity
	
	
func jump(buffer=null):
	velocity.y = jump_velocity
	
	if buffer != null:
		buffer.stop()
