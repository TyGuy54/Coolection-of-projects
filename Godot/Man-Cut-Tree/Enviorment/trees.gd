extends StaticBody2D

@export var tree_health = 25

@onready var log_item = preload("res://Drops/tree_drops/log.tscn")

func handle_hit():
	tree_health -= 5
	print('Tree Health ', tree_health)
	if tree_health <= 0:
		dropped_item()
		print("droped item: log")
		queue_free()

func dropped_item():
	var item = log_item.instantiate()
	item.position = $Marker2D.global_position
	get_parent().call_deferred("add_child", item)
