class Departamento:

    def __init__(self, nombre: str, cantidad_camas: int, pacientes: list):
        self.nombre = nombre
        self.cantidad_camas = cantidad_camas
        self.pacientes = pacientes

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def cantidad_camas(self) -> int:
        return self._cantidad_camas

    @property
    def pacientes(self) -> list:
        return self._pacientes

    @nombre.setter
    def nombre(self, nombre: str) -> None:
        self._nombre = nombre

    @cantidad_camas.setter
    def cantidad_camas(self, cantidad_camas: int) -> None:
        self._cantidad_camas = cantidad_camas

    @pacientes.setter
    def pacientes(self, pacientes: list) -> None:
        self._pacientes = pacientes