extends Area2D

func _on_log_body_entered(body):
	body.add_log()
	queue_free()
