import fire
import pkgutil
import importlib





def find_and_run_plugins(plugin_prefix):
    plugins = {}

    print(f"Discovering plugins with prefix: {plugin_prefix}")
    for _, name, _ in pkgutil.iter_modules():
        if name.startwith(plugin_prefix):
            module = importlib.import_module(name)
            plugins[name] = module

    for name, module in plugins.items():
        print(f"Running plugin {name}")
        module.run()

if __name__ == '__main__':
    fire.Fire()