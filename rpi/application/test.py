import settings.file_manager

global node_settings
global identity
node_settings = settings.file_manager.load_factory_settings()
identity = settings.file_manager.load_settings()

print node_settings
print identity
