# https://deepnote.com/@rmi-ppin/Faie-un-singleton-en-python-0d187a73-2f24-4c49-b2aa-bbbf4a45ace6

class MetaSingleton(type):
    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in MetaSingleton.__instances:
            MetaSingleton.__instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return MetaSingleton.__instances[cls]

# Exemple d'utilisation
# class Service(metaclass=MetaSingleton):
#     pass
