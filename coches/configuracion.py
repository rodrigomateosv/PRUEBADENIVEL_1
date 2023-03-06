import sys

DATABASE_PATH = "vehículos.csv"

if "pytest" in sys.argv[0]:
    DATABASE_PATH = "tests/vehiculos_test.csv"