extends Node2D

@onready var main_menu = $CanvasLayer/Main_Menu
@onready var address_entry = $CanvasLayer/Main_Menu/MarginContainer/VBoxContainer/Address_Entry

const Player = preload("res://Sceans/player.tscn")
const PORT = 9999
var enut_peer = ENetMultiplayerPeer.new()


func _on_host_pressed() -> void:
	main_menu.hide()
	$level_1.visible = true
	
	enut_peer.create_server(PORT)
	multiplayer.multiplayer_peer = enut_peer
	multiplayer.peer_connected.connect(add_player)
	
	add_player(multiplayer.get_unique_id())


func _on_join_pressed() -> void:
	main_menu.hide()
	$level_1.visible = true
	
	enut_peer.create_client("localhost", PORT)
	multiplayer.multiplayer_peer = enut_peer

func add_player(peer_id):
	var player = Player.instantiate()
	player.name = str(peer_id)
	add_child(player)
