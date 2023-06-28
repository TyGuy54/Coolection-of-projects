from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):

    def on_event_created(self, event, file_name):
        print(f"The file {event.src_path} has been created")

        if 'pokemon' in file_name:
            print("ooo a pokemon file")

    def on_any_event(self, event):
        file_name = event.src_path.split('/').lower()       

        if event.is_directory:
            return None
        elif event.event_type == 'created':
            self.on_event_created(event, file_name[4])
        elif event.event_type == "deleted":
            print(f"The file {event.src_path} has been deleted")