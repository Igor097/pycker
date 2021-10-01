import docker

"""
    The class responsible for managing containers
"""
class Pycker(object):
    def __init__(self):
        self.__client = docker.from_env()

    def container_list(self,
                       all_container: bool = False) -> None:
        pass

    def list_images(self,
                    all_images: bool = False) -> None:
        pass

    def list_network_interface(self,
                               details_network: bool = False,
                               driver_type: str = 'bridge') -> None:
        pass

    def list_volumes(self,
                     volume_type: str = 'local') -> None:
        pass

if __name__ == '__name__':
    ctn = Pycker()


