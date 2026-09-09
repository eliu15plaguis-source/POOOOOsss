class Paciente:

    PREVISIONES: set[str] = {"Fonasa", "Isapre"}

    def _init_(self, rut: str, nombre: str, edad: int, prevision: str):
        self.rut = rut
        self.nombre = nombre
        self.edad = edad
        self.prevision = prevision

    @property
    def rut(self) -> str:
        return

    @rut.setter
    def rut(self, rut: str)-> None:
        self.rut = rut