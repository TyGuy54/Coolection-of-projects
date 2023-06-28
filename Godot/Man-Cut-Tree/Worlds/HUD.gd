extends CanvasLayer

var num_of_logs = 0

func _ready():
	$num_of_logs.text = String(num_of_logs)

func _on_log_collected():
	num_of_logs += 1
	print(num_of_logs)
	_ready()
