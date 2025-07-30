class Kostka:

    def __init__(self, pocet_sten=6):
        self._pocet_sten = pocet_sten

    def __str__(self):
        return str(f"Kostka s {self._pocet_sten} stěnami.")

    def vrat_pocet_sten(self):
        return self._pocet_sten

    def hod(self):
        import random as _random
        return _random.randint(1, self._pocet_sten)

    def __repr__(self):
        return f"Kostka({self._pocet_sten})"